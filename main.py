<<<<<<< HEAD
# imports
import re  # for regex expression below
from collections import Counter  # import Counter from collections for Counter call below, for counting...
import random  # import random for doing random functions below


# main
def parseIntoRawText(textDatabase):
    with open(textDatabase, encoding="utf8") as rawData:  # Open text file and create a data stream
        rawTextForMethod = rawData.read()  # Read through the stream and create a string containing the text
    rawData.close()  # Close the data stream
    replacementTextToText = [
        ['\n', '\r', '\t', '--', ',', ';', '.', '!', '?', '"', '”', '“', ':', '#', '(', ')', '[', ']', '_', '/', '0',
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '=', '‖', 'I.', 'II.', 'III.', 'IV.', 'V.', ' i.', ' ii.',
         ' iii.', ' iv.', ' v.', '  ', '   '],
        [' ', ' ', ' ', ' -- ', ' , ', ' ; ', ' . ', ' ! ', ' ? ', ' ', ' ', ' ', ' : ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', ' ']]
    for index, char in enumerate(replacementTextToText[0]):
        charIndex = int(index)
        rawTextForMethod = rawTextForMethod.replace(replacementTextToText[0][charIndex], replacementTextToText[1][charIndex])
    return rawTextForMethod


def parseIntoSentenceList(rawTextForSentences):
    regexPattern = re.compile(r'([A-Z][^.!?]*[.!?])', re.M)  # Regex pattern for grabbing everything before a sentence ending punctuation mark
    sentenceListForMethod = regexPattern.findall(rawTextForSentences)  # Apply regex pattern to the string to create a list of all the sentences in the text
    return sentenceListForMethod


def parseIntoFirstWordList(sentenceListForMethod):
    firstWordListForMethod = []  # Initialize the list for the first word in each sentence
    for index, firstWord in enumerate(sentenceListForMethod):  # Enumerate through the sentenceList
        sentenceIndex = int(index)  # Get the index for below operation
        firstWord = sentenceListForMethod[sentenceIndex].split(' ')[0]  # Use split to only grab the first word in each sentence
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
    while count < len(
            unorderedWordListCall):  # Loop through count while it is less than the total length of the unorderedWordList
        wordTuple = unorderedWordListCall[count]  # Grab the tuple located at current count index
        firstTupleWord = wordTuple[0]  # Grab the first word of the grabbed tuple
        secondTupleWord = wordTuple[1]  # Grab the second word of the grabbed tuple
        integerCount = unorderedWordListCall[count + 1]  # Grab the integer count of the grabbed tuple
        containedUnorderedWordListForMethod.append(firstTupleWord)  # Append the first word
        containedUnorderedWordListForMethod.append(secondTupleWord)  # Append the second word
        containedUnorderedWordListForMethod.append(integerCount)  # Append the integer
        count += 2  # Jump the count ahead 2 spaces to next set of tuple and integer
    return containedUnorderedWordListForMethod


def weightedChoice(choices):  # Create a method for selecting an option randomly but including weighting
    total = sum(weight for choice, weight in choices)  # Black magic
    r = random.uniform(0, total)  # Black magic
    upTo = 0  # Black magic
    for choice, weight in choices:  # Black magic
        if upTo + weight >= r:  # Black magic
            return choice  # Black magic
        upTo += weight  # Black magic
    assert False, "Fuck you"  # Black magic


def createSentence(firstWords, database):
    minLengthOfSentence = 32  # Initialize minLengthOfSentence to a specific integer length of characters
    sentence = ' '  # Initialize sentence to a string with one space in it
    while len(sentence) < minLengthOfSentence:  # Repeat this until we get a sentence of a minimum specified length
        firstWordListIndexRandom = int(random.uniform(0, len(firstWords)))  # Randomly select an index from 0 through the length of firstWordList
        firstWordOfSentence = firstWords[firstWordListIndexRandom]  # Set firstWordOfSentence to the actual word at the random index from above
        firstWordOfSentenceForSearching = firstWordOfSentence.lower()  # Set firstWordOfSentence for searching to lowercase to match the actual list we need to search
        firstWordOfSentenceTupleIndexes = [x for x, y in enumerate(database) if y[
            0] == firstWordOfSentenceForSearching]  # Get the indexes of all of the tuples that contain the first word as the first word in the tuple
        firstWordOfSentenceTuples = []  # Initialize firstWordOfSentenceTuples as an empty list
        for index in firstWordOfSentenceTupleIndexes:  # Loop through the indexes of those tuples
            firstWordOfSentenceTuples.append(database[index])  # Append the actual tuples to firstWordOfSentenceTuples
        firstWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in firstWordOfSentenceTuples]  # Take out the first word so it is a list of tuples of words that follow the previous word plus their integer weight
        sentence = ''  # Initialize the sentence as an empty string
        sentence += firstWordOfSentence  # Add the firstWordOfSentence to the sentence
        sentence += ' '  # Add a space character to sentence
        nextWord = weightedChoice(firstWordOfSentenceTuplesMinusFirstWord)  # Grab the next word by weight using weightedChoice()
        while nextWord != '.' and nextWord != '!' and nextWord != '?':  # Keep going through nextWord until you hit the end of a sentence marked by punctuation
            nextWordOfSentenceTupleIndexes = [x for x, y in enumerate(database) if y[0] == nextWord]  # Get the indexes of all of the tuples that contain the first word as the first word in the tuple
            nextWordOfSentenceTuples = []  # Initialize nextWordOfSentenceTuples as an empty list
            for index in nextWordOfSentenceTupleIndexes:  # Loop through the indexes of those tuples
                nextWordOfSentenceTuples.append(
                    database[index])  # Append the actual tuples to firstWordOfSentenceTuples
            nextWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in nextWordOfSentenceTuples]  # Take out the first word so it is a list of tuples of words that follow the previous word plus their integer weight
            nextWord = weightedChoice(
                nextWordOfSentenceTuplesMinusFirstWord)  # Get the nextWord by doing a weightedChoice of the options
            sentence += nextWord  # Add the nextWord to the sentence
            sentence += ' '  # Add a space character after the nextWord
        punctuationToFixList = [[' ,', ' :', ' ;', ' )', ' (', ' "', ' .', ' !', ' ?'],
                                [',', ':', ';', ')', '(', '"', '.', '!', '?']]
        for index, char in enumerate(punctuationToFixList[0]):
            charIndex = int(index)
            sentence = sentence.replace(punctuationToFixList[0][charIndex], punctuationToFixList[1][charIndex])
    print(sentence)  # Print final sentence


def prepareText(textFile):
    rawText = parseIntoRawText(textFile)
    sentenceList = parseIntoSentenceList(rawText)
    firstWordList = parseIntoFirstWordList(sentenceList)
    lowercaseWordList = parseIntoWordList(rawText)
    unorderedWordDoubleDict = parseIntoUnorderedWordDoubleDict(lowercaseWordList)
    unorderedWordList = parseIntoUnorderedWordList(unorderedWordDoubleDict)
    containedUnorderedWordList = parseIntoContainedUnorderedWordList(unorderedWordList)
    unorderedTupleList = [containedUnorderedWordList[i:i + 3] for i in range(0, len(containedUnorderedWordList), 3)]  # Break up the list into tuples of n length, 3
    createSentence(firstWordList, unorderedTupleList)  # Run the method and pass it the text file
prepareText("text.txt")
=======
# Imports
import re  # Import for regex expression below
from collections import Counter  # Import Counter from collections for Counter call below, for counting...
import random    # Import random for doing random functions below

# Globals and Initializations
rawText = ''
sentenceList = []
firstWordList = []
lowercaseWordList = []
unorderedWordDoubleDict = {}
unorderedWordList = []
containedUnorderedWordList = []
unorderedTupleList = []

# Main file functions
def parseIntoRawText(textDatabase):    # (parseIntoRawText) Method when passed a text file (textDatabase) will turn it into a string (rawTextFromMethod)
	with open(textDatabase, encoding="utf8") as rawData:  # Open text file, read as utf8 encoded, and create a data stream of all the data
	    rawTextFromMethod = rawData.read()  # Create a (rawTextFromMethod) and assign it the entire string from the data stream of all data (rawData.read())
	rawData.close()  # Close the data stream so it can be cleaned from memory
	replacementTextToText = [['\n', '\r', '\t', '--', ',', ';', '.', '!', '?', '"', '”', '“', ':', '#', '(', ')', '[', ']', '_', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '=', '‖', 'I.', 'II.', 'III.', 'IV.', 'V.', ' i.', ' ii.', ' iii.', ' iv.', ' v.', '  ', '   '],[' ', ' ', ' ', ' -- ', ' , ', ' ; ', ' . ', ' ! ', ' ? ', ' ', ' ', ' ', ' : ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]    # A list of all the punctuation to be fixed in [0] and the text to replace them in [1], this mostly turns unneccessary punctuation into spaces or adds spaces around punctuation so that the punctuation isn't considered a character of each word for later
	for index, char in enumerate(replacementTextToText[0]):    # Enumerate through the text replacements (replacementTextToText[0])
		charIndex = int(index)    # Set (charIndex) to be the integer type value of the (index)
		rawTextFromMethod = rawTextFromMethod.replace(replacementTextToText[0][charIndex], replacementTextToText[1][charIndex])    # Update raw text (rawTextFromMethod) to have all its items in the (replacementTextToText[0]) with the item in (replacementTextToText[1]) of the same index
	return rawTextFromMethod    # Return the (rawTextFromMethod) string as the answer when method is called

def parseIntoSentenceList(rawTextForSentences):    # (parseIntoSentenceList) Method when passed text string (rawTextForSentences) turns it into a list of sentences (sentenceListFromMethod)
	regexPattern = re.compile(r'([A-Z][^.!?]*[.!?])', re.M)  # Compile regex pattern for grabbing everything before a sentence [A-Z] ending in a punctuation mark [.!?]
	sentenceListFromMethod = regexPattern.findall(rawTextForSentences)  # Apply regex pattern to the raw text string (rawTextForSentences) to create a list of all the sentences in the text and store in (sentenceListFromMethod)
	return sentenceListFromMethod    # Return the list of sentences in the text as (sentenceListFromMethod)
	
def parseIntoFirstWordList(sentenceListForFirstWord):    # (parseIntoFirstWordList) Method that takes a list of sentences (sentenceListForFirstWord) and turns it into a list of all the first words of those sentences (firstWordListFromMethod)
	firstWordListFromMethod = []  # Initialize the empty list for the first word in each sentence (firstWordListFromMethod)
	for index, firstWord in enumerate(sentenceListForFirstWord):  # Enumerate through the (sentenceListForFirstWord) and grab the (index) and the (firstWord)
	    sentenceIndex = int(index)  # Set (sentenceIndex) to be the integer type value of the (index)
	    firstWord = sentenceListForFirstWord[sentenceIndex].split(' ')[0]  # Use split to only grab the first word (.split(' ')[0]) in each sentence (sentenceList[sentenceIndex]) using the index to find each sentences (firstWord)
	    firstWordListFromMethod.append(firstWord)  # Append each sentence starting word to (firstWordList) from the (sentenceListFromMethod) list
	return firstWordListFromMethod    # Return the list of first words of sentences as (firstWordListFromMethod)
	
def parseIntoWordList(rawTextForWords):    # (parseIntoWordList) Method that takes raw text string (rawTextForWords) and turns it into a list of lowercase words (lowercaseWordListFromMethod)
	wordList = rawTextForWords.split(' ')  # Create list of all words by splitting the entire text string by the space character
	wordList = list(filter(None, wordList))  # Use filter to get rid of empty strings in the list (None) in (wordList) and reassign changes to (wordList)
	lowercaseWordListFromMethod = []  # Initialize the empty (lowercaseWordList) list
	for word in wordList:  # Loop through the (wordList) and grab each (word)
	    lowercaseWordListFromMethod.append(word.lower())  # Append the lowercase version of the item (.append(word.lower())) in (wordList) to the (lowercaseWordList)
	return lowercaseWordListFromMethod    # Return the list of all words in the text in their lowercase form (lowercaseWordListFromMethod)
	
def parseIntoUnorderedWordDoubleDict(lowercaseWordListForDict):    # (parseIntoUnorderedWordDoubleDict) Method that takes a list of words (lowercaseWordListForDict) and turns it into a dict of keys and values (unorderedWordDoubleDictFromMethod)
	nxt = iter(lowercaseWordListForDict)  # Set (nxt) as an iteration (iter) of the word list (lowercaseWordListForDict)
	next(nxt, None)  # Use (next) keyword to get next item (nxt, None) in word list (lowercaseWordListForDict) for below tuple
	unorderedWordDoubleDictFromMethod = (Counter(zip(lowercaseWordListForDict, nxt)).items())  # Create a dict using (Counter) that zips (zip) a tuple of word list (lowercaseWordListForDict) and next item in wordList (nxt) with the number of times that tuple exists in the text (.items())
	return unorderedWordDoubleDictFromMethod    # Returns a dictionary item (unorderedWordDoubleDictFromMethod) that has a tuple of words as the key, and the amount that tuple of words exists in the text as the value of those individual keys
	
def parseIntoUnorderedWordList(unorderedWordDoubleDictForList):    # (parseIntoUnorderedWordList) Method that turns the above described dict into a list (unorderedWordListFromMethod)
	unorderedWordListFromMethod = []  # Initialize the (unorderedWordListFromMethod) that will contain both the keys and values in list format instead of dict format
	for key, value in unorderedWordDoubleDictForList:  # Loop through the (unorderedWordDoubleDict) grabbing keys (key) and values (value)
	    unorderedWordListFromMethod.append(key)  # Append keys (key) to (unorderedWordListFromMethod)
	    unorderedWordListFromMethod.append(value)  # Append values (value) to (unorderedWordListFromMethod)
	return unorderedWordListFromMethod    # Return the unsorted list of word tuples and their count as individual items in a single list (unorderedWordListFromMethod)
	
def parseIntoContainedUnorderedWordList(unorderedWordListForContainment):    # (parseIntoContainedUnorderedWordList) Method that turns an unsorted word list and their counts (unorderedWordListForContainment) with a list that contains its own lists containing the first and second word in the tuple and their integer count (containedUnorderedWordListFromMethod)
	containedUnorderedWordListFromMethod = []  # Initialize the empty (containedUnorderedWordListFromMethod) list that will contain each word in the tuples and their integer count (containedUnorderedWordListFromMethod)
	count = 0  # Initialize (count) to 0 to start at the beginning
	while count < len(unorderedWordListForContainment):  # Loop through (count) while it is less than the total length of the unorderedWordListCall (< len(unorderedWordListForContainment))
	    wordTuple = unorderedWordListForContainment[count]  # Grab the tuple (wordTuple) located at current (count) index of (unorderedWordListForContainment)
	    firstTupleWord = wordTuple[0]  # Grab the first word (firstTupleWord) of the grabbed tuple (wordTuple[0])
	    secondTupleWord = wordTuple[1]  # Grab the second word (secondTupleWord) of the grabbed tuple (wordTuple[1])
	    integerCount = unorderedWordListForContainment[count + 1]  # Grab the integer count (integerCount) of the grabbed tuple (unorderedWordListForContainment[count + 1])
	    containedUnorderedWordListFromMethod.append(firstTupleWord)  # Append the first word (.append(firstTupleWord) to (containedUnorderedWordListFromMethod)
	    containedUnorderedWordListFromMethod.append(secondTupleWord)  # Append the second word (.append(secondTupleWord) to (containedUnorderedWordListFromMethod)
	    containedUnorderedWordListFromMethod.append(integerCount)  # Append the integer (.append(integerCount) to (containedUnorderedWordListForMethod)
	    count += 2  # Jump the (count) ahead 2 spaces to next set of tuple and integer, 0 is first word, 1 is second word, 2 is integer count, so go ahead 2 to 3 which is next tuple in list
	return containedUnorderedWordListFromMethod    # Return the list that contains all of (firstTupleWord), (secondTupleWord), (integerCount), for each tuple as a list (containedUnorderedWordListFromMethod)

def weightedChoice(choices):    # (weightedChoice) Method for selecting a word option at random with a weight applied from what is passed as (choices), (choices) must currently be a list containing tuples of 2 with a word as index 0 and integer as index 1 of the tuples
	total = sum(weight for choice, weight in choices)    # Set (total) to (sum) of ...???
	r = random.uniform(0, total)    # Set (r) to a random number between 0 and (total) with (uniform) distribution
	upTo = 0    # Initialize upTo to 0
	for choice, weight in choices:    # For all of the choices (choice) in (choices) get (weight)
		if upTo + weight >= r:    # If (upTo) added to (weight) is greater than or equal to (r) then...
			return choice    # Return the string value of (choice)
		upTo += weight    # Set (upTo) to (upTo) plus (weight)
	assert False, "What fuckery have you committed??"    # You should not tread here, it means you fucked up royally
	
def parseTextTotal(textFile):
	global rawText    # Global keyword to alter global variable
	rawText = parseIntoRawText(textFile)    # Set (rawText) to the value returned by passing ("text.txt") to (parseIntoRawText) Method
	global sentenceList    # Global keyword to alter global variable
	sentenceList = parseIntoSentenceList(rawText)    # Set (sentenceList) to the value returned by passing (rawText) to (parseIntoSentenceList) Method
	global firstWordList    # Global keyword to alter global variable
	firstWordList = parseIntoFirstWordList(sentenceList)    # Set (firstWordList) to the value returned by passing (sentenceList) to (parseIntoFirstWordList) Method
	global lowercaseWordList    # Global keyword to alter global variable
	lowercaseWordList = parseIntoWordList(rawText)    # Set (lowercaseWordList) to the value returned by passing (rawText) to (parseIntoWordList) Method
	global unorderedWordDoubleDict    # Global keyword to alter global variable
	unorderedWordDoubleDict = parseIntoUnorderedWordDoubleDict(lowercaseWordList)    # Set (unorderedWordDoubleDict) to the value returned by passing (lowercaseWordList) to (parseIntoUnorderedWordDoubleDict) Method
	global unorderedWordList    # Global keyword to alter global variable
	unorderedWordList = parseIntoUnorderedWordList(unorderedWordDoubleDict)    # Set (unorderedWordList) to the value returned by passing (unorderedWordDoubleDict) to (parseIntoUnorderedWordList) Method
	global containedUnorderedWordList    # Global keyword to alter global variable
	containedUnorderedWordList = parseIntoContainedUnorderedWordList(unorderedWordList)    # Set (containedUnorderedWordList) to the value returned by passing (unorderedWordList) to (parseIntoContainedUnorderedWordList) Method
	global unorderedTupleList    # Global keyword to alter global variable
	unorderedTupleList = [containedUnorderedWordList[i:i + 3] for i in range(0, len(containedUnorderedWordList), 3)]  # Break up the list (containedUnorderedWordList) into tuples of length 3
	return firstWordList, unorderedTupleList    # Return both the (firstWordList) and (unorderedTupleList)
	
def createSentence(firstWords, database):    # (createSentence) Method that takes an input of (firstWords=(firstWordList)) and (database=(unorderedTupleList)) and creates a sentence from the data using the first words to start with and follows it with the database of words and their weights of instance
	minLengthOfSentence = 32    # Initialize the minimum length of (sentence) in characters (minLengthOfSentence) to a specific integer length of characters (32)
	maxLengthOfSentence = 140    # Initialize the maximum length of (sentence) in characters (maxLengthOfSentence) to a specific integer length of characters (140)
	sentence = ' '    # Initialize (sentence) to a string with one space in it
	# Sentence Loop
	while len(sentence) < minLengthOfSentence or len(sentence) > maxLengthOfSentence:    # While the length of the sentence (len(sentence)) is less than the minimum and greater than the maximum do below, so it only creates sentences of length between the min and max
		firstWordListIndexRandom = int(random.uniform(0, len(firstWords)))    # Randomly select an index from 0 through the length of firstWordList (int(random.uniform(0, len(firstWords)))) and set to (firstWordListIndexRandom) which will be the index for the first word we will use
		firstWordOfSentence = ''    # Initialize (firstWordOfSentence) as an empty string
		firstWordOfSentence = firstWords[firstWordListIndexRandom]    # Set (firstWordOfSentence) to the actual word at the random index from above (firstWords[firstWordListIndexRandom])
		firstWordOfSentenceForSearching = firstWordOfSentence.lower()    # Set (firstWordOfSentenceForSearching) for searching to lowercase (.lower()) to match the actual list we need to search, which is all in lowercase
		firstWordOfSentenceTupleIndexes = [x for x, y in enumerate(database) if y[0] == firstWordOfSentenceForSearching]    # Get the indexes of all of the tuples that contain the first word as the first word in their tuple and put those indices into (firstWordOfSentenceTupleIndexes)
		firstWordOfSentenceTuples = []    # Initialize (firstWordOfSentenceTuples) as an empty list
		for index in firstWordOfSentenceTupleIndexes:    # Loop through the indexes of those tuples (firstWordOfSentenceTupleIndexes)
			firstWordOfSentenceTuples.append(database[index])    # Append the actual tuples (.append(database[index])) to (firstWordOfSentenceTuples)
		firstWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in firstWordOfSentenceTuples]    # Take out the first word (x[1:]) so it is a list of tuples of words that follow the previous word plus their integer weight and set to (firstWordOfSentenceTuplesMinusFirstWord)
		nextWord = ''    # Initialize (nextWord) to an empty string
		sentence = ''    # Set (sentence) to an empty string
		sentence += firstWordOfSentence    # Add the (firstWordOfSentence) to the (sentence)
		sentence += ' '    # Add a space character to (sentence)
		nextWord = weightedChoice(firstWordOfSentenceTuplesMinusFirstWord)    # Grab the next word (nextWord) by weight using (weightedChoice) and passing it (firstWordOfSentenceTuplesMinusFirstWord)
		# Next Word Loop
		while nextWord != '.' and nextWord != '!' and nextWord != '?':    # Keep going through nextWord until you hit the end of a sentence marked by hitting punctuation
			nextWordOfSentenceTupleIndexes = [x for x, y in enumerate(database) if y[0] == nextWord]    # Get the indexes of all of the tuples that contain the word as the first word in the tuple 
			nextWordOfSentenceTuples = []    # Initialize (nextWordOfSentenceTuples) as an empty list
			for index in nextWordOfSentenceTupleIndexes:    # Loop through the indexes of those tuples (nextWordOfSentenceTupleIndexes)
				nextWordOfSentenceTuples.append(database[index])    # Append the actual tuples (.append(database[index])) to (firstWordOfSentenceTuples)
			nextWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in nextWordOfSentenceTuples]    # Take out the first word (x[1:]) so it is a list of tuples of words that follow the previous word plus their integer weight as (nextWordOfSentenceTuplesMinusFirstWord)
			nextWord = weightedChoice(nextWordOfSentenceTuplesMinusFirstWord)    # Get the (nextWord) by doing a (weightedChoice) and passing it (nextWordOfSentenceTuplesMinusFirstWord)
			sentence += nextWord    # Add the (nextWord) to the (sentence)
			sentence += ' '    # Add a space character after the (nextWord) into (sentence)
		punctuationToFixList = [[' ,', ' :', ' ;', ' )', ' (', ' "', ' .', ' !', ' ?'],[',', ':', ';', ')', '(', '"', '.', '!', '?']]    # A list of all the punctuation to be fixed in [0] and the text to replace them in [1] with the same indices, mostly getting rid of extra space characters
		for index, punctuation in enumerate(punctuationToFixList[0]):    # Go through the list of punctuationToFixList and grab the indices and character
			punctuationIndex = int(index)    # Turn the (index) into an integer type (int()) and assign it to (charIndex)
			sentence = sentence.replace(punctuationToFixList[0][punctuationIndex], punctuationToFixList[1][punctuationIndex])    # Go through the sentence and take values in [0] and replace them with values from [1] at the same indices
	print(sentence)    # Print final (sentence) to console

parseTextTotal('text.txt')    # Run the (parseTextTotal) Method and pass it ('text.txt')

i = 0
while i < 10:
	createSentence(firstWordList, unorderedTupleList)    # Run the (createSentence) Method and pass it (firstWordList, unorderedTupleList)
	print(' ')
	i += 1
	
# Pull more text from http://marx.eserver.org/
>>>>>>> origin/master
