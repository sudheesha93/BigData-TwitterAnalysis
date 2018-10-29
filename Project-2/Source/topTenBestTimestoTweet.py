import sys
import json
import operator
import subprocess
import re
from datetime import datetime 

def claculateBestTime(file):
    data={}
    with open(file) as fp:
      for line in fp:
        if 'created_at' in json.loads(line).keys():
            createdAt=json.loads(line)['created_at']
            date= datetime.strptime(createdAt, "%a %b %d %H:%M:%S +0000 %Y")
            hour= date.hour
            if date.minute in data.keys():
                data[date.minute]+=1;
            else:
                data[date.minute]=1;  
    sortedData=sorted(data.items(), key=operator.itemgetter(1),reverse=True) 
    print("Top 10 Best Times to Tweet :")
    for i in range(0,10):
        print(hour,":",sortedData[i][0],"-",hour,":",sortedData[i][0]+1)
def main():
    tweet_file = open(sys.argv[1])
    claculateBestTime(sys.argv[1])

if __name__ == '__main__':
    main()
    

