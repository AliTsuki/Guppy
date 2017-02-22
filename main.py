# Imports
import re  # Import for regex expression below
from collections import Counter  # Import Counter from collections for Counter call below, for counting...
import random  # Import random for doing random functions below
from numpy.random import choice  # Import numpy for numerical python operations
import sys  # Import sys for exit statement below

# Globals and Initializations
rawText = ''
sentenceList = []
lowercaseSentenceList = []
firstWordList = []
lowercaseWordList = []
unorderedWordDoubleDict = {}
unorderedWordList = []
containedUnorderedWordList = []
unorderedTupleList = []


# Main file functions
def parseIntoRawText(textDatabase):  # (parseIntoRawText) Method when passed a text file (textDatabase) will turn it into a string (rawTextFromMethod)
    with open(textDatabase, 'r+', encoding='utf8') as rawData:  # Open text file, give read and write permissions, read as utf8 encoded, and create a data stream of all the data
        rawTextFromMethod = rawData.read()  # Create a (rawTextFromMethod) and assign it the entire string from the data stream of all data (rawData.read())
    rawData.close()  # Close the data stream so it can be cleaned from memory
    replacementTextToText = [
        ['\n', '\r', '\t', '--', ',', ';', '.', '!', '?', '"', '”', '“', ':', '#', '(', ')', '[', ']', '_', '/', '0',
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '=', '‖', 'I.', 'II.', 'III.', 'IV.', 'V.', ' i.', ' ii.',
         ' iii.', ' iv.', ' v.', '  ', '   '],
        [' ', ' ', ' ', ' -- ', ' , ', ' ; ', ' . ', ' ! ', ' ? ', ' ', ' ', ' ', ' : ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ',
         ' ']]  # A list of all the punctuation to be fixed in [0] and the text to replace them in [1], this mostly turns unnecessary punctuation into spaces or adds spaces around punctuation so that the punctuation isn't considered a character of each word for later
    for index, char in enumerate(replacementTextToText[0]):  # Enumerate through the text replacements (replacementTextToText[0])
        rawTextFromMethod = rawTextFromMethod.replace(replacementTextToText[0][index], replacementTextToText[1][index])  # Update raw text (rawTextFromMethod) to have all its items in the (replacementTextToText[0]) with the item in (replacementTextToText[1]) of the same index
    return rawTextFromMethod  # Return the (rawTextFromMethod) string as the answer when method is called


def parseIntoSentenceList(rawTextForSentences):  # (parseIntoSentenceList) Method when passed text string (rawTextForSentences) turns it into a list of sentences (sentenceListFromMethod)
    regexPattern = re.compile(r'([A-Z][^.!?]*[.!?])', re.M)  # Compile regex pattern for grabbing everything before a sentence [A-Z] ending in a punctuation mark [.!?]
    sentenceListFromMethod = regexPattern.findall(rawTextForSentences)  # Apply regex pattern to the raw text string (rawTextForSentences) to create a list of all the sentences in the text and store in (sentenceListFromMethod)
    sentenceListFromMethod = list(filter(None, sentenceListFromMethod))  # Use filter to get rid of empty strings in the list (None) in (sentenceListFromMethod) and reassign changes to (sentenceListFromMethod)
    return sentenceListFromMethod  # Return the list of sentences in the text as (sentenceListFromMethod)


def parseIntoLowercaseSentenceList(sentenceListForLowercase):    # (parseIntoLowercaseSentenceList) Method takes a list of sentences (sentenceListForLowercase) and makes a list of those same sentences but in lowercase and returns it as (lowercaseSentenceListFromMethod)
    lowercaseSentenceListFromMethod = []    # Initialize (lowercaseSentenceListFromMethod) to contain lowercase sentences
    for sntnce in sentenceListForLowercase:    # For each sentence (sntnce) in (sentenceListForLowercase) do below
        lowercaseSentenceListFromMethod.append(sntnce.lower())    # Append the lowercase (.lower()) version of the sentence (sntnce) to the list (lowercaseSentenceListFromMethod)
    return lowercaseSentenceListFromMethod    # Return the list of lowercase sentences as (lowercaseSentenceListFromMethod)
    
    
def parseIntoFirstWordList(sentenceListForFirstWord):  # (parseIntoFirstWordList) Method that takes a list of sentences (sentenceListForFirstWord) and turns it into a list of all the first words of those sentences (firstWordListFromMethod)
    firstWordListFromMethod = []  # Initialize the empty list for the first word in each sentence (firstWordListFromMethod)
    for index, firstWord in enumerate(sentenceListForFirstWord):  # Enumerate through the (sentenceListForFirstWord) and grab the (index) and the (firstWord)
        firstWord = sentenceListForFirstWord[index].split(' ')[0]  # Use split to only grab the first word (.split(' ')[0]) in each sentence (sentenceList[index]) using the index to find each sentences (firstWord)
        firstWordListFromMethod.append(firstWord)  # Append each sentence starting word (firstWord) to (firstWordListFromMethod) from the (sentenceListForFirstWord)
    firstWordListFromMethod = list(filter(None, firstWordListFromMethod))  # Use filter to get rid of empty strings in the list (None) in (firstWordListFromMethod) and reassign changes to (firstWordListFromMethod)
    return firstWordListFromMethod  # Return the list of first words of sentences as (firstWordListFromMethod)


def parseIntoWordList(rawTextForWords):  # (parseIntoWordList) Method that takes raw text string (rawTextForWords) and turns it into a list of lowercase words (lowercaseWordListFromMethod)
    wordList = rawTextForWords.split(' ')  # Create list of all words by splitting the entire text string by the space character
    wordList = list(filter(None, wordList))  # Use filter to get rid of empty strings in the list (None) in (wordList) and reassign changes to (wordList)
    lowercaseWordListFromMethod = []  # Initialize the empty (lowercaseWordListFromMethod) list
    for word in wordList:  # Loop through the (wordList) and grab each (word)
        lowercaseWordListFromMethod.append(word.lower())  # Append the lowercase version of the item (.append(word.lower())) in (wordList) to the (lowercaseWordList)
    return lowercaseWordListFromMethod  # Return the list of all words in the text in their lowercase form (lowercaseWordListFromMethod)


def parseIntoUnorderedWordDoubleDict(lowercaseWordListForDict):  # (parseIntoUnorderedWordDoubleDict) Method that takes a list of words (lowercaseWordListForDict) and turns it into a dict of keys and values (unorderedWordDoubleDictFromMethod)
    nxt = iter(lowercaseWordListForDict)  # Set (nxt) as an iteration (iter) of the word list (lowercaseWordListForDict)
    next(nxt, None)  # Use (next) keyword to get next item (nxt, None) in word list (lowercaseWordListForDict) for below tuple
    unorderedWordDoubleDictFromMethod = (Counter(zip(lowercaseWordListForDict, nxt)).items())  # Create a dict using (Counter) that zips (zip) a tuple of word list (lowercaseWordListForDict) and next item in wordList (nxt) with the number of times that tuple exists in the text (.items())
    return unorderedWordDoubleDictFromMethod  # Returns a dictionary item (unorderedWordDoubleDictFromMethod) that has a tuple of words as the key, and the amount that tuple of words exists in the text as the value of those individual keys


def parseIntoUnorderedWordList(unorderedWordDoubleDictForList):  # (parseIntoUnorderedWordList) Method that turns the above described dict into a list (unorderedWordListFromMethod)
    unorderedWordListFromMethod = []  # Initialize the (unorderedWordListFromMethod) that will contain both the keys and values in list format instead of dict format
    for key, value in unorderedWordDoubleDictForList:  # Loop through the (unorderedWordDoubleDict) grabbing keys (key) and values (value)
        unorderedWordListFromMethod.append(key)  # Append keys (key) to (unorderedWordListFromMethod)
        unorderedWordListFromMethod.append(value)  # Append values (value) to (unorderedWordListFromMethod)
    return unorderedWordListFromMethod  # Return the unsorted list of word tuples and their count as individual items in a single list (unorderedWordListFromMethod)


def parseIntoContainedUnorderedWordList(unorderedWordListForContainment):  # (parseIntoContainedUnorderedWordList) Method that turns an unsorted word list and their counts (unorderedWordListForContainment) with a list that contains its own lists containing the first and second word in the tuple and their integer count (containedUnorderedWordListFromMethod)
    containedUnorderedWordListFromMethod = []  # Initialize the empty (containedUnorderedWordListFromMethod) list that will contain each word in the tuples and their integer count (containedUnorderedWordListFromMethod)
    count = 0  # Initialize (count) to 0 to start at the beginning
    while count < len(unorderedWordListForContainment):  # Loop through (count) while it is less than the total length of the unorderedWordForContainment (< len(unorderedWordListForContainment))
        wordTuple = unorderedWordListForContainment[count]  # Grab the tuple (wordTuple) located at current (count) index of (unorderedWordListForContainment)
        firstTupleWord = wordTuple[0]  # Grab the first word (firstTupleWord) of the grabbed tuple (wordTuple[0])
        secondTupleWord = wordTuple[1]  # Grab the second word (secondTupleWord) of the grabbed tuple (wordTuple[1])
        integerCount = unorderedWordListForContainment[count + 1]    # Grab the integer count (integerCount) of the grabbed tuple (unorderedWordListForContainment[count + 1])
        containedUnorderedWordListFromMethod.append(firstTupleWord)  # Append the first word (.append(firstTupleWord) to (containedUnorderedWordListFromMethod)
        containedUnorderedWordListFromMethod.append(secondTupleWord)  # Append the second word (.append(secondTupleWord) to (containedUnorderedWordListFromMethod)
        containedUnorderedWordListFromMethod.append(integerCount)  # Append the integer (.append(integerCount)) to (containedUnorderedWordListForMethod)
        count += 2  # Jump the (count) ahead 2 spaces to next set of tuple and integer, 0 is first word, 1 is second word, 2 is integer count, so go ahead 2 to 3 which is next tuple in list
    return containedUnorderedWordListFromMethod  # Return the list that contains all of (firstTupleWord), (secondTupleWord), (integerCount), for each tuple as a list (containedUnorderedWordListFromMethod)


def getWordInSentenceCount(nxtWrd, sList):    # (getWordInSentenceCount) Method is passed (nxtWrd) and (sList) and returns the number of sentences (nxtWrd) appears in
    sentencesIncludingNextWord = [s for s in sList if nxtWrd in s]    # Set (sentencesIncludingNextWord) to a list containing all of the sentences containing (nxtWrd)
    oftennessOfWordInSentences = len(sentencesIncludingNextWord)    # Set (oftennessOfWordInSentences) to the number of sentences in the list
    return oftennessOfWordInSentences    # Return the number of sentences the next word appears in as (oftennessOfWordInSentences)
    # CHANGE THIS TO CREATE A DICT WHERE KEY IS EVERY WORD IN WORD LIST AND VALUE IS THE NUMBER OF SENTENCES THAT WORD APPEARS IN AND USE IN INITIAL PARSING

def getWordsInSentenceRate(wLst, sLst):
    for wrd in wLst:
        sentencesIncludingWord = [s for s in sLst if wrd in s]
        #while 
        #for index, w in enumerate(sentencesIncludingWord):
            
    # Make a method that makes a list of how often 2 words appear in a sentence, will need to restructure and have this called during Text Parsing, and then have the values accessed during weightedChoice()


def getFirstWord(fWordList):  # (getFirstWord) Method that grabs a first word from (fWordList) and returns it as (firstWordOfSentence)
    firstWordListIndexRandom = int(random.uniform(0, len(fWordList)))  # Randomly select an index from 0 through the length of (fWordList) (int(random.uniform(0, len(fWordList)))) and set to (firstWordListIndexRandom) which will be the index for the first word we will use
    firstWordOfSentence = fWordList[firstWordListIndexRandom]  # Set (firstWordOfSentence) to the actual word at the random index from above (fWordList[firstWordListIndexRandom])
    return firstWordOfSentence  # Return the (firstWordOfSentence)


def getNextWord(nxtWord, dbase):  # (getNextWord) Method that chooses the best next word when passed (nxtWord) and (dbase)
    nextWordOfSentenceTupleIndexes = []  # Initialize the (nextWordOfSentenceTupleIndexes) as empty list
    if nxtWord and dbase:  # If (nxt) and (dbase) both contain information, do the below
        nxtWord = str(nxtWord).lower()  # (Set nxtWord to stringified (nxtWord) made lowercase
        for x, y in enumerate(dbase):  # Enumerate through (dbase) and grab both (x) and (y) values
            if y[0] == nxtWord:  # If the first word of the word tuple grabbed from (dbase) is equal to current (nxtWord) do below
                nextWordOfSentenceTupleIndexes.append(x)  # Append the index values from (x) to (nexWordOfSentenceTupleIndexes)
        if nextWordOfSentenceTupleIndexes:  # If (nextWordOfSentenceTupleIndexes has data do below
            nextWordOfSentenceTuples = []  # Initialize (nextWordOfSentenceTuples) as an empty list
            for indices in nextWordOfSentenceTupleIndexes:  # Loop through the indices of those tuples (nextWordOfSentenceTupleIndexes)
                nextWordOfSentenceTuples.append(dbase[indices])  # Append the actual tuples (.append(dbase[indices])) to (nextWordOfSentenceTuples)
            nextWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in nextWordOfSentenceTuples]  # Set (nextWordOfSentenceTuplesMinusFirstWord to a list of tuples consisting of the [1] and [2] values of the tuple
            if nextWordOfSentenceTuplesMinusFirstWord:  # If nextWordOfSentenceTuplesMinusFirstWord contains data do below
                nxtWord = weightedChoice(nxtWord, nextWordOfSentenceTuplesMinusFirstWord)  # Get the (nextWord) by doing a (weightedChoice) and passing it (nextWordOfSentenceTuplesMinusFirstWord)
            nxtWord = str(nxtWord[0])  # Set (nxtWord) to the stringified first value in the (nxtWord) list, there is only one value
            return nxtWord  # Return the string (nxtWord)
        else:  # If not
            print('Abandon Hope, All Ye Who Enter Here') # Exit the program (should be removed handled with error catcher etc.


def weightedChoice(nxtWrd, choices):  # (weightedChoice) Method for selecting a word option at random with a weight applied from what is passed as (choices), (choices) must currently be a list containing tuples of 2 with a word as index 0 and integer as index 1 of the tuples
    elements = [i[0] for i in choices]  # Set (elements) to all of the (i[0]) of (choices)
    probability = [i[1] for i in choices]  # Set (probability) to the (i[1]) of (choices)
    probabilityTotal = 0  # Initialize (probabilityTotal) to 0
    i = 0  # Initialize (i) to 0
    while i < len(probability):  # While (i) is less than the length of (probability)
        probabilityTotal += probability[i]  # Add the integer at probability[i] to (probabilityTotal)
        i += 1  # Add 1 to (i)
    probabilities = []  # Initialize (probabilities) to an empty list
    for index, integer in enumerate(probability):  # Enumerate through (probability) and grab the (index) and (integer)
        probabilities.append(probability[index] / probabilityTotal)  # Append (probability[index]) divided by (probabilityTotal) getting the probability percent to probabilities
    result = choice(elements, 1, p=probabilities)  # Set (result) to return of (choice()) that is passed the list of (elements), grab 1 element, use (probabilities) as percent
    return result  # Return the (result)


def parseTextTotal(textFile):  # (parseTextTotal) Method that parses all of the text in (textFile) and creates all the necessary databases
    global rawText  # Global keyword to alter global variable
    rawText = parseIntoRawText(textFile)  # Set (rawText) to the value returned by passing (textFile) to (parseIntoRawText) Method
    global sentenceList  # Global keyword to alter global variable
    sentenceList = parseIntoSentenceList(rawText)  # Set (sentenceList) to the value returned by passing (rawText) to (parseIntoSentenceList) Method
    global lowercaseSentenceList  # Global keyword to alter global variable
    lowercaseSentenceList = parseIntoLowercaseSentenceList(sentenceList)  # Set (lowercaseSentenceList) to the value returned by passing (sentenceList) to (parseIntoLowercaseSentenceList) Method
    global firstWordList  # Global keyword to alter global variable
    firstWordList = parseIntoFirstWordList(sentenceList)  # Set (firstWordList) to the value returned by passing (sentenceList) to (parseIntoFirstWordList) Method
    global lowercaseWordList  # Global keyword to alter global variable
    lowercaseWordList = parseIntoWordList(rawText)  # Set (lowercaseWordList) to the value returned by passing (rawText) to (parseIntoWordList) Method
    global unorderedWordDoubleDict  # Global keyword to alter global variable
    unorderedWordDoubleDict = parseIntoUnorderedWordDoubleDict(lowercaseWordList)  # Set (unorderedWordDoubleDict) to the value returned by passing (lowercaseWordList) to (parseIntoUnorderedWordDoubleDict) Method
    global unorderedWordList  # Global keyword to alter global variable
    unorderedWordList = parseIntoUnorderedWordList(unorderedWordDoubleDict)  # Set (unorderedWordList) to the value returned by passing (unorderedWordDoubleDict) to (parseIntoUnorderedWordList) Method
    global containedUnorderedWordList  # Global keyword to alter global variable
    containedUnorderedWordList = parseIntoContainedUnorderedWordList(unorderedWordList)  # Set (containedUnorderedWordList) to the value returned by passing (unorderedWordList) to (parseIntoContainedUnorderedWordList) Method
    global unorderedTupleList  # Global keyword to alter global variable
    unorderedTupleList = [containedUnorderedWordList[i:i + 3] for i in range(0, len(containedUnorderedWordList), 3)]  # Break up the list (containedUnorderedWordList) into tuples of length 3
    return firstWordList, unorderedTupleList  # Return both the (firstWordList) and (unorderedTupleList)


def createSentence(firstWords, database):  # (createSentence) Method that takes an input of (firstWords=(firstWordList)) and (database=(unorderedTupleList)) and creates a sentence from the data using the first words to start with and follows it with the database of words and their weights of instance
    minLengthOfSentence = 100  # Initialize the minimum length of (sentence) in characters (minLengthOfSentence) to a specific integer length of characters
    maxLengthOfSentence = 140  # Initialize the maximum length of (sentence) in characters (maxLengthOfSentence) to a specific integer length of characters
    sentence = ' '  # Initialize (sentence) to a string with one space in it
    # Sentence Loop
    while len(sentence) < minLengthOfSentence or len(sentence) > maxLengthOfSentence:  # While the length of the sentence (len(sentence)) is less than the minimum and greater than the maximum do below, so it only creates sentences of length between the min and max
        firstWordOfSentence = str(getFirstWord(firstWords))
        nextWord = ''  # Initialize (nextWord) to an empty string
        sentence = ''  # Set (sentence) to an empty string
        sentence += firstWordOfSentence  # Add the (firstWordOfSentence) to the (sentence)
        sentence += ' '  # Add a space character to (sentence)
        nextWord = firstWordOfSentence.lower()  # Set (nextWord) to the lowercase of (firstWordOfSentence)
        # Next Word Loop
        while nextWord != '.' and nextWord != '!' and nextWord != '?':  # Keep going through nextWord until you hit the end of a sentence marked by hitting punctuation
            nextWord = str(getNextWord(nextWord, database))  # Set (nextWord) to the string of (getNextWord) by passing it (nextWord) and (database)
            sentence += nextWord  # Add the (nextWord) to the (sentence)
            sentence += ' '  # Add a space character after the (nextWord) into (sentence)
    punctuationToFixList = [[' ,', ' :', ' ;', ' )', ' (', ' "', ' .', ' !', ' ?'],
                            [',', ':', ';', ')', '(', '"', '.', '!',
                             '?']]  # A list of all the punctuation to be fixed in [0] and the text to replace them in [1] with the same indices, mostly getting rid of extra space characters
    for index, punctuation in enumerate(punctuationToFixList[0]):  # Go through the list of punctuationToFixList and grab the indices and character
        sentence = sentence.replace(punctuationToFixList[0][index], punctuationToFixList[1][index])  # Go through the sentence and take values in [0] and replace them with values from [1] at the same indices
    print(sentence)  # Print final (sentence) to console


parseTextTotal('text.txt')  # Run the (parseTextTotal) Method and pass it ('text.txt')

k = 0
while k < 10:
    createSentence(firstWordList, unorderedTupleList)  # Run the (createSentence) Method and pass it (firstWordList, unorderedTupleList)
    print(' ')
    k += 1

# Pull more text from http://marx.eserver.org/
# 1. Go through word list, check sentence list for word, create list of sentences that include word, count them, exclude punctuation use oftenness of word in word choice probablility algorithm.
# 2. Go through word list, check sentence list for word, create a list of all of the other words in the sentence, count each word to get rate of how often the two words appear in a sentence together not just next to eachother.

sys.exit()  # Exit the program (should be removed handled with error catcher etc.
