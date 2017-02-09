# import
import re  # for regex expression below
from collections import Counter  # import Counter from collections for Counter call below, for counting...
from operator import itemgetter    # import itemgetter from operator for itemgetter in sorted operation below
import random    # import random for doing random functions below

# main
with open("text.txt") as rawData:  # Open text file and create a data stream
    rawText = rawData.read()  # Read through the stream and create a string containing the text
rawData.close()  # Close the data stream
rawText = rawText.replace('\n', ' ')  # Remove newline characters from text
rawText = rawText.replace('\r', ' ')  # Remove newline characters from text
rawText = rawText.replace('--', ' -- ')  # Break up blah--blah words so it can read 2 separate words blah -- blah
rawText = rawText.replace(',', ' , ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace(';', ' ; ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace('.', ' . ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace('!', ' ! ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace('?', ' ? ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace('"', ' " ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace(':', ' : ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace('#', ' # ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace('(', ' ( ')  # Break up punctuation so they are not considered part of words
rawText = rawText.replace(')', ' ) ')  # Break up punctuation so they are not considered part of words
pat = re.compile(r'([A-Z][^.!?]*[.!?])', re.M)  # Regex pattern for grabbing everything before a sentence ending punctuation
sentenceList = pat.findall(rawText)  # Apply regex pattern to string to create a list of all the sentences in the text
firstWordList = []  # Initialize the list for the first word in each sentence
for index, firstWord in enumerate(sentenceList):  # Enumerate through the sentence list
    sentenceIndex = int(index)  # Get the index for below operation
    firstWord = sentenceList[sentenceIndex].split(' ')[0]  # Use split to only grab the first word in each sentence
    firstWordList.append(firstWord)  # Append each sentence starting word to first word list
sentenceListForWords = pat.findall(rawText)  # Run the regex pattern again this time with the punctuation broken up by spaces
wordsInSentenceList = []  # Initialize list for all of the words that appear in each sentence
for index, words in enumerate(sentenceList):  # Enumerate through sentence list
    sentenceIndex = int(index)  # Grab the index for below operation
    words = sentenceList[sentenceIndex].split(' ')  # Split up the words in each sentence so we have a list that contains each word in each sentence
    wordsInSentenceList.append(words)  # Append above described to the list
wordList = rawText.split(' ')  # Create list of all words by splitting the entire text by spaces
wordList = list(filter(None, wordList))  # Use filter to get rid of empty strings in the list
lowercaseWordList = []  # Initialize the lowercase word list
for word in wordList:  # loop through the word list
    lowercaseWordList.append(word.lower())  # append the lowercase version of the item in word list to the lowercase word list
nxt = iter(lowercaseWordList)  # Set nxt as an iteration of word list
next(nxt, None)  # Use next keyword to get next item in word list for below tuple
unorderedWordDoubleDict = (Counter(zip(lowercaseWordList, nxt)).items())  # Create a dict using Counter that zips a tuple of word list and next item in word list with the number of times that tuple exists in the text
unorderedWordList = []  # Initialize the unordered word list that will contain both the keys and values in list format instead of dict format
for key, value in unorderedWordDoubleDict:  # Loop through the unordered word double dict grabbing keys and values
    unorderedWordList.append(key)  # Append keys to unordered word list
    unorderedWordList.append(value)  # Append values to unordered word list
containedUnorderedWordList = []  # Initialize the contained unordered word list that will contain each word in the tuples and the integer counts
count = 0  # Initialize count to 0
while count < len(unorderedWordList):  # Loop through count while it is less than the total length of the unordered word list
    wordTuple = unorderedWordList[count]  # Grab the tuple located at current count index
    firstTupleWord = wordTuple[0]  # Grab the first word of the grabbed tuple
    secondTupleWord = wordTuple[1]  # Grab the second word of the grabbed tuple
    integerCount = unorderedWordList[count + 1]  # Grab the integer count of the grabbed tuple
    containedUnorderedWordList.append(firstTupleWord)  # Append the first word
    containedUnorderedWordList.append(secondTupleWord)  # Append the second word
    containedUnorderedWordList.append(integerCount)  # Append the integer
    count += 2  # Jump the count ahead 2 spaces to next set of tuple and integer
l = containedUnorderedWordList  # Set the list to be the contained unordered word list
n = 3  # Set the size of the chunks to 3
unorderedTupleList = [l[i:i + n] for i in range(0, len(l), n)]  # Break up the l list into tuples of n length
orderedTupleList = sorted(unorderedTupleList, key = itemgetter(0, 2), reverse=True)    # set ordered tuple list as unordered tuple list sorted first by first word, second by integer count, reverse so that integer goes high to low
firstWordListIndexRandom = int(random.uniform(0, len(firstWordList)))    # Randomly select an index from 0 through the length of first word list
firstWordOfSentence = ''    # Initialize first word of sentence as an empty string
firstWordOfSentence = firstWordList[firstWordListIndexRandom]    # Set first word of sentence to the actual word at the random index from above
firstWordOfSentenceForSearching = firstWordOfSentence.lower()    # Set first word of sentence for searching to lowercase to match the actual list we need to search
firstWordOfSentenceTupleIndexes = [x for x, y in enumerate(orderedTupleList) if y[0] == firstWordOfSentenceForSearching]    # Get the indexes of all of the tuples that contain the first word as the first word in the tuple
firstWordOfSentenceTuples = []    # Initialize first word of sentence tuples as an empty list
for index in firstWordOfSentenceTupleIndexes:    # Loop through the indexes of those tuples
	firstWordOfSentenceTuples.append(orderedTupleList[index])    # Append the actual tuples to first word of sentence tuples


def weighted_choice(choices):    # Create a method for selecting an option randomly but including weighting
	total = sum(weight for choice, weight in choices)    # Black magic
	r = random.uniform(0, total)    # Black magic
	upto = 0    # Black magic
	for choice, weight in choices:    # Black magic
		if upto + weight >= r:    # Black magic
			return choice    # Black magic
		upto += weight    # Black magic
	assert False, "Fuck you"    # Black magic

# sentenceList = List of all sentences
# firstWordList = List of words that start sentence list
# sentenceListForWords = List of all sentences mutated for ease of extracting words
# wordsInSentenceList = List of lists containing all of the words in each sentence
# wordList = List of all words
# lowercaseWordList = List of all words in all lowercase
# unorderedWordDoubleDict = Dict of all unique word pairs in a tuple plus the count of times that unique pair appears in the text
# unorderedWordList = List of unordered word double dict, sorting works better on list not dict
# containedUnorderedWordList = List of every word in the tuple order and the integer count in a single list without tuples
# unorderedTupleList = List of tuples containing 3 parts, the first and second word and the integer count
# orderedTupleList = List of the tuple triplets ordered first by first word and second by integer count
# firstWordOfSentence = String containing the randomly selected first word of a sentence from first word List
# firstWordOfSentenceTuples = List of tuples containing first word as the first word in the tuple

# sample data source:
# http://www.gutenberg.org/cache/epub/61/pg61.txt
