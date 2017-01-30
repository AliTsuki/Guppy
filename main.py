#import
import re #for regex expression below
from collections import Counter

#main
with open("text.txt") as rawData:    #Open text file and create a datastream
    rawText = rawData.read()    #Read through the stream and create a string containing the text
rawData.close()    #Close the datastream
rawText = rawText.replace('\n', ' ')    #Remove newline characters from text
rawText = rawText.replace('\r', ' ')    #Remove newline characters from text
rawText = rawText.replace('--', ' -- ')    #Break up blah--blah words so it can read 2 separate words blah -- blah
pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)    #Regex pattern for grabbing everthing before a sentence ending punctuation
sentenceList = []    #Initialize list for sentences in text
sentenceList = pat.findall(rawText)    #Apply regex pattern to string to create a list of all the sentences in the text
firstWordList = []    #Initialize the list for the first word in each sentence
for index, firstWord in enumerate(sentenceList):    #Enumerate through the sentence list
    sentenceIndex = int(index)    #Get the index for below operation
    firstWord = sentenceList[sentenceIndex].split(' ')[0]    #Use split to only grab the first word in each sentence
    firstWordList.append(firstWord)    #Append each sentence starting word to first word list
rawText = rawText.replace(', ', ' , ')    #Break up punctuation so they are not considered part of words
rawText = rawText.replace('. ', ' . ')    #Break up punctuation so they are not considered part of words
rawText = rawText.replace('"', ' " ')    #Break up punctuation so they are not considered part of words
sentenceListForWords = []    #Initialize sentence list for parsing words
sentenceListForWords = pat.findall(rawText)    #Run the regex pattern again this time with the punctuation broken up by spaces
wordsInSentenceList = []    #Initialize list for all of the words that appear in each sentence
for index, words in enumerate(sentenceList):    #Enumerate through sentence list
    sentenceIndex = int(index)    #Grab the index for below operation
    words = sentenceList[sentenceIndex].split(' ')    #Split up the words in each sentence so we have a nested lists that contain each word in each sentence
    wordsInSentenceList.append(words)    #Append above described to the list
wordList = []    #Initialize list of all words
wordList = rawText.split(' ')    #Create list of all words by splitting the entire text by spaces
wordList = list(filter(None, wordList))    #Use filter to get rid of empty strings in the list
nxt = iter(wordList)    #Set nxt as an iteration of word list
next(nxt, None)    #Use next keyword to get next item in word list for below tuple
unorderedWordDoubleListDict = (Counter(zip(wordList, nxt)).items())    #Create a dict using Counter that zips a tuple of wordlist and next item in wordlist with the number of times that tuple exists in the text

#sentenceList = List of all sentences
#firstWordList = List of words that start sentencelist
#sentenceListForWords = List of all sentences mutated for ease of extracting words
#wordsInSentenceList = List of lists containing all of the words in each sentence
#wordList = List of all words
#unorderedWordDoubleListDict = Dict of all unique word pairs in a tuple plus the count of times that unique pair appears in the text

#sample data source
#http://www.gutenberg.org/cache/epub/61/pg61.txt
