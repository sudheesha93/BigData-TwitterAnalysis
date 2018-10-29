import sys
import json
import operator
import subprocess
import re
import os
    
for root,directories, filenames in os.walk("/Sample"):
    for directory in directories:
        print(os.path.join(root,directory))
        print(os.listdir("/Tweets"))
    for filename in filenames:
        print(os.path.join(root,filename))
            
       
def freq(file,keyword):
    data={}
    count=0
    with open(file) as fp:
      for line in fp:
        if 'created_at' in json.loads(line).keys():
            a=json.loads(line)['entities']['hashtags']

            for word in a:
                if keyword in str(word['text'].lower().encode('utf-8')):
                   count=count+1;
                
    print(count)
    

def main():
    tweet_file = open(sys.argv[1])
    freq(sys.argv[1],sys.argv[2])


if __name__ == '__main__':
    main()