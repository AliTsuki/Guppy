#import
import re

#main
with open("text.txt") as rawdata:
    rawtext = rawdata.read()
rawdata.close()
rawtext = rawtext.replace('\n', ' ')
rawtext = rawtext.replace('\r', ' ')
rawtext = rawtext.replace('--', ' -- ')
pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
sentencelist = []
sentencelist = pat.findall(rawtext)
firstwordlist = []
for index, firstword in enumerate(sentencelist):
	sentenceindex = int(index)
	firstword = sentencelist[sentenceindex].split(' ')[0]
	firstwordlist.append(firstword)
rawtext = rawtext.replace(', ', ' , ')
rawtext = rawtext.replace('. ', ' . ')
rawtext = rawtext.replace('"', ' " ')
sentencelistforwords = []
sentencelistforwords = pat.findall(rawtext)
wordsinsentencelist = []
for index, words in enumerate(sentencelist):
	sentenceindex = int(index)
	words = sentencelist[sentenceindex].split(' ')
	wordsinsentencelist.append(words)
wordlist = []
wordlist = rawtext.split(' ')
wordlist = list(filter(None, wordlist))
wordlistdouble = [[], []]
for index, word in enumerate(wordlist):
	if(int(index) < int(len(wordlist))-1):
		wordlistindex1 = int(index)
		wordlistindex2 = int(index)+1
		wordlistdouble[0].append(wordlist[wordlistindex1])
		wordlistdouble[1].append(wordlist[wordlistindex2])
#for wordlistdouble[0]

#debugging prints
print('sentencelist = ')
print(sentencelist)
print('\n ---------------------------------  \n')
print('firstwordlist = ')
print(firstwordlist)
print('\n ---------------------------------  \n')
print('sentencelistforwords = ')
print(sentencelistforwords)
print('\n ---------------------------------  \n')
print('wordsinsentencelist = ')
print(wordsinsentencelist)
print('\n ---------------------------------  \n')
print('wordlist= ')
print(wordlist)
print('\n --------------------------------- \n')
print('wordlistdouble = ')
print(wordlistdouble)
print('\n --------------------------------- \n')
#debugging prints

#sentencelist = list of all sentences
#firstwordlist = list of words that start sentencelist
#sentencelistforwords = list of all sentences mutated for ease of extracting words
#wordsinsentencelist = list of lists containing all of the words in each sentence
#wordlist = list of all words
#wordlistdouble = dual list of all words plus the words that follow them

#sample data source
#http://www.gutenberg.org/cache/epub/61/pg61.txt
