import sys
import json
import operator
import subprocess
import re

def findRatoofUniquetoDuplicate(file):
    data={}
    uniqueWordsCount = 0
    duplicateWordsCount = 0
    ratioofUniquetoDuplicate = 0
    with open(file) as fp:
      for line in fp:
        if 'created_at' in json.loads(line).keys():
            hashtags=json.loads(line)['entities']['hashtags']
            for word in hashtags:
                if word['text'].lower().encode('utf-8') in data.keys():
                   data[word['text'].lower().encode('utf-8')]+=1;
                else:
                   data[word['text'].lower().encode('utf-8')]=1
    sortedData = sorted(data.items(), key=operator.itemgetter(1),reverse=True)
    for i in range(0,len(sortedData)):
        if sortedData[i][1] > 1:
            duplicateWordsCount = duplicateWordsCount + 1
        elif sortedData[i][1] == 1:
            uniqueWordsCount = uniqueWordsCount + 1
    print("Unique words count : ",uniqueWordsCount)
    print("Duplicate Words Count : ",duplicateWordsCount)
    ratio = uniqueWordsCount/duplicateWordsCount
    print("Ratio of number of Unique words to number of words with duplicates : ",int(ratio))

def main():
    tweet_file = open(sys.argv[1])
    findRatoofUniquetoDuplicate(sys.argv[1])

if __name__ == '__main__':
    main()
    

