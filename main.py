# import
import re  # for regex expression below
from collections import Counter  # import Counter from collections for Counter call below, for counting...
import random    # import random for doing random functions below

# main
def parseIntoRawText(textDatabase):
	with open(textDatabase, encoding="utf8") as rawData:  # Open text file and create a data stream
	    rawTextForMethod = rawData.read()  # Read through the stream and create a string containing the text
	rawData.close()  # Close the data stream
	return rawTextForMethod

def parseIntoSentenceList(rawTextForSentences):
	replacementTextToText = [['\n', '\r', '\t', '--', ',', ';', '.', '!', '?', '"', '”', '“', ':', '#', '(', ')', '[', ']', '_', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '=', '‖', 'I.', 'II.', 'III.', 'IV.', 'V.', ' i.', ' ii.', ' iii.', ' iv.', ' v.', '  ', '   '],[' ', ' ', ' ', ' -- ', ' , ', ' ; ', ' . ', ' ! ', ' ? ', ' ', ' ', ' ', ' : ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
	for index, char in enumerate(replacementTextToText):
		rawTextForSentences = rawTextForSentences.replace(replacementTextToText[0][index], replacementTextToText[1][index])
	pat = re.compile(r'([A-Z][^.!?]*[.!?])', re.M)  # Regex pattern for grabbing everything before a sentence ending punctuation mark
	sentenceListForMethod = pat.findall(rawTextForSentences)  # Apply regex pattern to the string to create a list of all the sentences in the text
	return sentenceListForMethod
	
def parseIntoFirstWordList(sentenceListForMethod):
	firstWordListForMethod = []  # Initialize the list for the first word in each sentence
	for index, firstWord in enumerate(sentenceListForMethod):  # Enumerate through the sentenceList
	    sentenceIndex = int(index)  # Get the index for below operation
	    firstWord = sentenceList[sentenceIndex].split(' ')[0]  # Use split to only grab the first word in each sentence
	    firstWordListForMethod.append(firstWord)  # Append each sentence starting word to firstWordList
	return firstWordListForMethod
	
def parseIntoWordList(rawTextForWords):
	wordList = rawTextForWords.split(' ')  # Create list of all words by splitting the entire text by spaces
	wordList = list(filter(None, wordList))  # Use filter to get rid of empty strings in the list
	lowercaseWordListForMethod = []  # Initialize the lowercaseWordList
	for word in wordList:  # Loop through the wordList
	    lowercaseWordListForMethod.append(word.lower())  # Append the lowercase version of the item in word list to the lowercaseWordList
	return lowercaseWordListForMethod
	
def parseIntoUnorderedWordDoubleDict(lowercaseWordListForMethod):
	nxt = iter(lowercaseWordListForMethod)  # Set nxt as an iteration of wordList
	next(nxt, None)  # Use next keyword to get next item in wordList for below tuple
	unorderedWordDoubleDictForMethod = (Counter(zip(lowercaseWordListForMethod, nxt)).items())  # Create a dict using Counter that zips a tuple of wordList and next item in wordList with the number of times that tuple exists in the text
	return unorderedWordDoubleDictForMethod
	
def parseIntoUnorderedWordList(unorderedWordDoubleDictCall):
	unorderedWordListForMethod = []  # Initialize the unorderedWordList that will contain both the keys and values in list format instead of dict format
	for key, value in unorderedWordDoubleDictCall:  # Loop through the unorderedWordDoubleDict grabbing keys and values
	    unorderedWordListForMethod.append(key)  # Append keys to unorderedWordList
	    unorderedWordListForMethod.append(value)  # Append values to unorderedWordList
	return unorderedWordListForMethod
	
def parseIntoContainedUnorderedWordList(unorderedWordListCall):
	containedUnorderedWordListForMethod = []  # Initialize the containedUnorderedWordList that will contain each word in the tuples and the integer counts
	count = 0  # Initialize count to 0
	while count < len(unorderedWordListCall):  # Loop through count while it is less than the total length of the unorderedWordList
	    wordTuple = unorderedWordListCall[count]  # Grab the tuple located at current count index
	    firstTupleWord = wordTuple[0]  # Grab the first word of the grabbed tuple
	    secondTupleWord = wordTuple[1]  # Grab the second word of the grabbed tuple
	    integerCount = unorderedWordListCall[count + 1]  # Grab the integer count of the grabbed tuple
	    containedUnorderedWordListForMethod.append(firstTupleWord)  # Append the first word
	    containedUnorderedWordListForMethod.append(secondTupleWord)  # Append the second word
	    containedUnorderedWordListForMethod.append(integerCount)  # Append the integer
	    count += 2  # Jump the count ahead 2 spaces to next set of tuple and integer
	return containedUnorderedWordListForMethod

def weightedChoice(choices):    # Create a method for selecting an option randomly but including weighting
	total = sum(weight for choice, weight in choices)    # Black magic
	r = random.uniform(0, total)    # Black magic
	upto = 0    # Black magic
	for choice, weight in choices:    # Black magic
		if upto + weight >= r:    # Black magic
			return choice    # Black magic
		upto += weight    # Black magic
	assert False, "Fuck you"    # Black magic

def createSentence(firstWords, database):
	minLengthOfSentence = 32    # Initialize minLengthOfSentence to a specific integer length of characters
	sentence = ' '    # Initialize sentence to a string with one space in it
	while len(sentence) < minLengthOfSentence:    # Repeat this until we get a sentence of a minimum specified length
		firstWordListIndexRandom = int(random.uniform(0, len(firstWords)))    # Randomly select an index from 0 through the length of firstWordList
		firstWordOfSentence = ''    # Initialize firstWordOfSentence as an empty string
		firstWordOfSentence = firstWordList[firstWordListIndexRandom]    # Set firstWordOfSentence to the actual word at the random index from above
		firstWordOfSentenceForSearching = firstWordOfSentence.lower()    # Set firstWordOfSentence for searching to lowercase to match the actual list we need to search
		firstWordOfSentenceTupleIndexes = [x for x, y in enumerate(database) if y[0] == firstWordOfSentenceForSearching]    # Get the indexes of all of the tuples that contain the first word as the first word in the tuple
		firstWordOfSentenceTuples = []    # Initialize firstWordOfSentenceTuples as an empty list
		for index in firstWordOfSentenceTupleIndexes:    # Loop through the indexes of those tuples
			firstWordOfSentenceTuples.append(database[index])    # Append the actual tuples to firstWordOfSentenceTuples
		firstWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in firstWordOfSentenceTuples]    # Take out the first word so it is a list of tuples of words that follow the previous word plus their integer weight
		nextWord = ''    # Initialize nextWord to empty string
		sentence = ''    # Initialize the sentence as an empty string
		sentence += firstWordOfSentence    # Add the firstWordOfSentence to the sentence
		sentence += ' '    # Add a space character to sentence
		nextWord = weightedChoice(firstWordOfSentenceTuplesMinusFirstWord)    # Grab the next word by weight using weightedChoice()
		while nextWord != '.' and nextWord != '!' and nextWord != '?':    # Keep going through nextWord until you hit the end of a sentence marked by punctuation
			nextWordOfSentenceTupleIndexes = [x for x, y in enumerate(database) if y[0] == nextWord]    # Get the indexes of all of the tuples that contain the first word as the first word in the tuple 
			nextWordOfSentenceTuples = []    # Initialize nextWordOfSentenceTuples as an empty list
			for index in nextWordOfSentenceTupleIndexes:    # Loop through the indexes of those tuples
				nextWordOfSentenceTuples.append(database[index])    # Append the actual tuples to firstWordOfSentenceTuples
			nextWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in nextWordOfSentenceTuples]    # Take out the first word so it is a list of tuples of words that follow the previous word plus their integer weight
			nextWord = weightedChoice(nextWordOfSentenceTuplesMinusFirstWord)    # Get the nextWord by doing a weightedChoice of the options
			sentence += nextWord    # Add the nextWord to the sentence
			sentence += ' '    # Add a space character after the nextWord
		punctuationToFixList = [[' ,', ' :', ' ;', ' )', ' (', ' "', ' .', ' !', ' ?',],[',', ':', ';', ')', '(', '"', '.', '!', '?']]
		for index, char in punctuationToFixList:
			sentence = sentence.replace(punctuationToFixList[0][index], punctuationToFixList[1][index])
	print(sentence)    # Print final sentence

rawText = parseIntoRawText("text.txt")
sentenceList = parseIntoSentenceList(rawText)
firstWordList = parseIntoFirstWordList(sentenceList)
lowercaseWordList = parseIntoWordList(rawText)
unorderedWordDoubleDict = parseIntoUnorderedWordDoubleDict(lowercaseWordList)
unorderedWordList = parseIntoUnorderedWordList(unorderedWordDoubleDict)
containedUnorderedWordList = parseIntoContainedUnorderedWordList(unorderedWordList)
unorderedTupleList = [containedUnorderedWordList[i:i + 3] for i in range(0, len(containedUnorderedWordList), 3)]  # Break up the list into tuples of n length, 3

createSentence(firstWordList, unorderedTupleList)    # Run the method and pass it the text file

