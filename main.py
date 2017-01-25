#import
import re #for regex expression below

#main
with open("text.txt") as rawdata:    #open text file and create a datastream
    rawtext = rawdata.read()    #read through the stream and create a string containing the text
rawdata.close()    #close the datastream
rawtext = rawtext.replace('\n', ' ')    #remove newline characters from text
rawtext = rawtext.replace('\r', ' ')    #remove newline characters from text
rawtext = rawtext.replace('--', ' -- ')    #break up blah--blah words so it can read 2 separate words blah -- blah
pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)    #regex pattern for grabbing everthing before a sentence ending punctuation
sentencelist = []    #initialize list for sentences in text
sentencelist = pat.findall(rawtext)    #apply regex pattern to string to create a list of all the sentences in the text
firstwordlist = []    #initialize the list for the first word in each sentence
for index, firstword in enumerate(sentencelist):    #enumerate through the sentence list
    sentenceindex = int(index)    #get the index for below operation
    firstword = sentencelist[sentenceindex].split(' ')[0]    #use split to only grab the first word in each sentence
    firstwordlist.append(firstword)    #append each sentence starting word to first word list
rawtext = rawtext.replace(', ', ' , ')    #break up punctuation so they are not considered part of words
rawtext = rawtext.replace('. ', ' . ')    #break up punctuation so they are not considered part of words
rawtext = rawtext.replace('"', ' " ')    #break up punctuation so they are not considered part of words
sentencelistforwords = []    #initialize sentence list for parsing words
sentencelistforwords = pat.findall(rawtext)    #run the regex pattern again this time with the punctuation broken up by spaces
wordsinsentencelist = []    #initialize list for all of the words that appear in each sentence
for index, words in enumerate(sentencelist):    #enumerate through sentence list
    sentenceindex = int(index)    #grab the index for below operation
    words = sentencelist[sentenceindex].split(' ')    #split up the words in each sentence so we have a nested lists that contain each word in each sentence
    wordsinsentencelist.append(words)    #append above described to the list
wordlist = []    #initialize list of all words
wordlist = rawtext.split(' ')    #create list of all words by splitting the entire text by spaces
wordlist = list(filter(None, wordlist))    #use filter to get rid of empty strings in the list
wordlistdouble = [[], []]    #initialize the word list double to contain words and the words that follow them in sentences
for index, word in enumerate(wordlist):    #enumerate through word list
    if(int(index) < int(len(wordlist))-1):    #only go to 1 before the end of list so we don't get an index out of bounds error
        wordlistindex1 = int(index)    #grab index for first word
        wordlistindex2 = int(index)+1    #grab index for following word
        wordlistdouble[0].append(wordlist[wordlistindex1])    #append first word to first list of word list double
        wordlistdouble[1].append(wordlist[wordlistindex2])    #append following word to second list of word list double
wordlisttriple = [[], [], []]    #initialize word list triple
for index, unit in enumerate(wordlistdouble[0]):    #enumerate through word list double
    word1 = wordlistdouble[0][index]    #grab word at first list of word list double at the current index
    word2 = wordlistdouble[1][index]    #grab word at second list of word list double at the current index
    count = 0    #initialize word double data set counter
    wordlisttriple[0].append(word1)    #these need to be encapsulated in some kind of loop/if/for idk
    wordlisttriple[1].append(word2)    #these need to be encapsulated in some kind of loop/if/for idk
    wordlisttriple[2].append(count)    #these need to be encapsulated in some kind of loop/if/for idk
    #for index, unit1 in enumerate(wordlistdouble[0]):
        #if(wordlistdouble[0][int(index)] == word1 && wordlistdouble[1][int(index)+1] == word2):
            #count++

#sentencelist = list of all sentences
#firstwordlist = list of words that start sentencelist
#sentencelistforwords = list of all sentences mutated for ease of extracting words
#wordsinsentencelist = list of lists containing all of the words in each sentence
#wordlist = list of all words
#wordlistdouble = dual list of all words plus the words that follow them

#sample data source
#http://www.gutenberg.org/cache/epub/61/pg61.txt
