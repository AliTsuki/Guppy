#import
import re

#main
with open("text.txt") as rawdata:
    rawtext = rawdata.read()
rawtext = rawtext.replace('\n', ' ')
rawtext = rawtext.replace('\r', ' ')
rawtext = rawtext.replace('--', ' -- ')
pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
sentencelist = pat.findall(rawtext)
for startingword in sentencelist:
	#dfdfd
rawtext = rawtext.replace(', ', ' , ')
rawtext = rawtext.replace('. ', ' . ')
rawtext = rawtext.replace('"', ' " ')
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
rawdata.close()

#sample data source
#http://www.gutenberg.org/cache/epub/61/pg61.txt
