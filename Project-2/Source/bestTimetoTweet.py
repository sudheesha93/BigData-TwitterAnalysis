import sys
import json
import operator
import subprocess
import re
from datetime import datetime 

def calculateBestTime(file):
    data={}
    with open(file) as fp:
      for line in fp:
        if 'created_at' in json.loads(line).keys():
            createdAt=json.loads(line)['created_at']
            date= datetime.strptime(createdAt, "%a %b %d %H:%M:%S +0000 %Y")
            hour = date.hour
            if date.hour in data.keys():
                data[date.hour]+=1;
            else:
                data[date.hour]=1;  
    sortedData=sorted(data.items(), key=operator.itemgetter(1),reverse=True)
    print(sortedData[0][0])
def main():
    tweet_file = open(sys.argv[1])
    calculateBestTime(sys.argv[1])

if __name__ == '__main__':
    main()
    

