import sys
import json
import operator
import subprocess
import re

def findDuplicateWords(file):
    data={}
    with open(file) as fp:
      for line in fp:
        if 'created_at' in json.loads(line).keys():
            hashtags=json.loads(line)['entities']['hashtags']
            for word in hashtags:
                if word['text'].lower().encode('utf-8') in data.keys():
                   data[word['text'].lower().encode('utf-8')]+=1
                else:
                   data[word['text'].lower().encode('utf-8')]=1
    sortedData= sorted(data.items(), key=operator.itemgetter(1),reverse=True)
    f= open("dups.txt","w+")
    for i in range(0,len(sortedData)):
        if sortedData[i][1] > 1:
            f.write("".join(map(str,re.findall("'([^']*)'",str(sortedData[i][0])))))
            f.write("\n")
    f.close()
    print("dups.txt file created successfully")

def main():
    tweet_file = open(sys.argv[1])
    findDuplicateWords(sys.argv[1])

if __name__ == '__main__':
    main()
    

