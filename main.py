# import
import re  # for regex expression below
from collections import Counter  # import Counter from collections for Counter call below, for counting...
from operator import itemgetter  # import itemgetter from operator for itemgetter in sorted operation below
import random  # import random for doing random functions below


# main
def weightedChoice(choices):  # Create a method for selecting an option randomly but including weighting
    total = sum(weight for choice, weight in choices)  # Black magic
    r = random.uniform(0, total)  # Black magic
    upTo = 0  # Black magic
    for choice, weight in choices:  # Black magic
        if upTo + weight >= r:  # Black magic
            return choice  # Black magic
        upTo += weight  # Black magic
    assert False, "Fuck you"  # Black magic


def createSentence(database):
    minLengthOfSentence = 32  # Initialize minLengthOfSentence to a specific integer length of characters
    sentence = ' '  # Initialize sentence to a string with one space in it
        rawText = rawData.read()  # Read through the stream and create a string containing the text
    rawData.close()  # Close the data stream
    rawText = rawText.replace('\n', ' ')  # Remove newline characters from text
    rawText = rawText.replace('\r', ' ')  # Remove newline characters from text
    rawText = rawText.replace('\t', ' ')  # Remove tab characters from text
    rawText = rawText.replace('--', ' -- ')  # Break up blah--blah words so it can read 2 separate words "blah -- blah"
    rawText = rawText.replace(',', ' , ')  # Break up non-words to separate them from words
    rawText = rawText.replace(';', ' ; ')  # Break up non-words to separate them from words
    rawText = rawText.replace('.', ' . ')  # Break up non-words to separate them from words
    rawText = rawText.replace('!', ' ! ')  # Break up non-words to separate them from words
    rawText = rawText.replace('?', ' ? ')  # Break up non-words to separate them from words
    rawText = rawText.replace('"', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('”', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('“', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace(':', ' : ')  # Break up non-words to separate them from words
    rawText = rawText.replace('#', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('(', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace(')', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('[', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace(']', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('_', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('/', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('0', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('1', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('2', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('3', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('4', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('5', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('6', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('7', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('8', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('9', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('+', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('=', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('‖', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('I.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('II.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('III.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('IV.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('V.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace(' i.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace(' ii.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace(' iii.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace(' iv.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace(' v.', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('  ', ' ')  # Break up non-words to separate them from words
    rawText = rawText.replace('   ', ' ')  # Break up non-words to separate them from words
    pat = re.compile(r'([A-Z][^.!?]*[.!?])',
                     re.M)  # Regex pattern for grabbing everything before a sentence ending punctuation mark
    sentenceList = pat.findall(
        rawText)  # Apply regex pattern to the string to create a list of all the sentences in the text
    firstWordList = []  # Initialize the list for the first word in each sentence
    for index, firstWord in enumerate(sentenceList):  # Enumerate through the sentenceList
        sentenceIndex = int(index)  # Get the index for below operation
        firstWord = sentenceList[sentenceIndex].split(' ')[0]  # Use split to only grab the first word in each sentence
        firstWordList.append(firstWord)  # Append each sentence starting word to firstWordList
    wordsInSentenceList = []  # Initialize list for all of the words that appear in each sentence
    for index, words in enumerate(sentenceList):  # Enumerate through sentenceList
        sentenceIndex = int(index)  # Grab the index for below operation
        words = sentenceList[sentenceIndex].split(
            ' ')  # Split up the words in each sentence so we have a list that contains each word in each sentence
        wordsInSentenceList.append(words)  # Append above described to the list
    wordList = rawText.split(' ')  # Create list of all words by splitting the entire text by spaces
    wordList = list(filter(None, wordList))  # Use filter to get rid of empty strings in the list
    lowercaseWordList = []  # Initialize the lowercaseWordList
    for word in wordList:  # Loop through the wordList
        lowercaseWordList.append(
            word.lower())  # Append the lowercase version of the item in word list to the lowercaseWordList
    nxt = iter(lowercaseWordList)  # Set nxt as an iteration of wordList
    next(nxt, None)  # Use next keyword to get next item in wordList for below tuple
    unorderedWordDoubleDict = (Counter(zip(lowercaseWordList,
                                           nxt)).items())  # Create a dict using Counter that zips a tuple of wordList and next item in wordList with the number of times that tuple exists in the text
    unorderedWordList = []  # Initialize the unorderedWordList that will contain both the keys and values in list format instead of dict format
    for key, value in unorderedWordDoubleDict:  # Loop through the unorderedWordDoubleDict grabbing keys and values
        unorderedWordList.append(key)  # Append keys to unorderedWordList
        unorderedWordList.append(value)  # Append values to unorderedWordList
    containedUnorderedWordList = []  # Initialize the containedUnorderedWordList that will contain each word in the tuples and the integer counts
    count = 0  # Initialize count to 0
    while count < len(
            unorderedWordList):  # Loop through count while it is less than the total length of the unorderedWordList
        wordTuple = unorderedWordList[count]  # Grab the tuple located at current count index
        firstTupleWord = wordTuple[0]  # Grab the first word of the grabbed tuple
        secondTupleWord = wordTuple[1]  # Grab the second word of the grabbed tuple
        integerCount = unorderedWordList[count + 1]  # Grab the integer count of the grabbed tuple
        containedUnorderedWordList.append(firstTupleWord)  # Append the first word
        containedUnorderedWordList.append(secondTupleWord)  # Append the second word
        containedUnorderedWordList.append(integerCount)  # Append the integer
        count += 2  # Jump the count ahead 2 spaces to next set of tuple and integer
    l = containedUnorderedWordList  # Set the list to be the containedUnorderedWordList
    n = 3  # Set the size of the chunks to 3
    unorderedTupleList = [l[i:i + n] for i in range(0, len(l), n)]  # Break up the l list into tuples of n length
    orderedTupleList = sorted(unorderedTupleList, key=itemgetter(0, 2),
                              reverse=True)  # Set ordered tuple list as unordered tuple list sorted first by first word, second by integer count, reverse so that integer goes high to low
    while len(sentence) < minLengthOfSentence:  # Repeat this until we get a sentence of a minimum specified length
        firstWordListIndexRandom = int(random.uniform(0, len(
            firstWordList)))  # Randomly select an index from 0 through the length of firstWordList
        firstWordOfSentence = ''  # Initialize firstWordOfSentence as an empty string
        firstWordOfSentence = firstWordList[
            firstWordListIndexRandom]  # Set firstWordOfSentence to the actual word at the random index from above
        firstWordOfSentenceForSearching = firstWordOfSentence.lower()  # Set firstWordOfSentence for searching to lowercase to match the actual list we need to search
        firstWordOfSentenceTupleIndexes = [x for x, y in enumerate(orderedTupleList) if y[
            0] == firstWordOfSentenceForSearching]  # Get the indexes of all of the tuples that contain the first word as the first word in the tuple
        firstWordOfSentenceTuples = []  # Initialize firstWordOfSentenceTuples as an empty list
        for index in firstWordOfSentenceTupleIndexes:  # Loop through the indexes of those tuples
            firstWordOfSentenceTuples.append(
                orderedTupleList[index])  # Append the actual tuples to firstWordOfSentenceTuples
        firstWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in
                                                   firstWordOfSentenceTuples]  # Take out the first word so it is a list of tuples of words that follow the previous word plus their integer weight
        nextWord = ''  # Initialize nextWord to empty string
        sentence = ''  # Initialize the sentence as an empty string
        sentence += firstWordOfSentence  # Add the firstWordOfSentence to the sentence
        sentence += ' '  # Add a space character to sentence
        nextWord = weightedChoice(
            firstWordOfSentenceTuplesMinusFirstWord)  # Grab the next word by weight using weightedChoice()
        while nextWord != '.' and nextWord != '!' and nextWord != '?':  # Keep going through nextWord until you hit the end of a sentence marked by punctuation
            nextWordOfSentenceTupleIndexes = [x for x, y in enumerate(orderedTupleList) if y[
                0] == nextWord]  # Get the indexes of all of the tuples that contain the first word as the first word in the tuple
            nextWordOfSentenceTuples = []  # Initialize nextWordOfSentenceTuples as an empty list
            for index in nextWordOfSentenceTupleIndexes:  # Loop through the indexes of those tuples
                nextWordOfSentenceTuples.append(
                    orderedTupleList[index])  # Append the actual tuples to firstWordOfSentenceTuples
            nextWordOfSentenceTuplesMinusFirstWord = [x[1:] for x in
                                                      nextWordOfSentenceTuples]  # Take out the first word so it is a list of tuples of words that follow the previous word plus their integer weight
            nextWord = weightedChoice(
                nextWordOfSentenceTuplesMinusFirstWord)  # Get the nextWord by doing a weightedChoice of the options
            sentence += nextWord  # Add the nextWord to the sentence
            sentence += ' '  # Add a space character after the nextWord
        sentence = sentence.replace(' ,', ',')  # Fix punctuation mistakes
        sentence = sentence.replace(' :', ':')  # Fix punctuation mistakes
        sentence = sentence.replace(' ;', ';')  # Fix punctuation mistakes
        sentence = sentence.replace(' )', ')')  # Fix punctuation mistakes
        sentence = sentence.replace(' (', '(')  # Fix punctuation mistakes
        sentence = sentence.replace(' "', '"')  # Fix punctuation mistakes
        sentence = sentence.replace(' .', '.')  # Fix punctuation mistakes
        sentence = sentence.replace(' !', '!')  # Fix punctuation mistakes
        sentence = sentence.replace(' ?', '?')  # Fix punctuation mistakes
    print(sentence)  # Print final sentence


createSentence("text.txt")  # Run the method and pass it the text file

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
