import sys
import json
import operator
import subprocess
import re

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def freq(file):
    data={}
    with open(file) as fp:
      for line in fp:
        if 'created_at' in json.loads(line).keys():
            a=json.loads(line)['entities']['hashtags']

            for word in a:
                if word['text'].lower().encode('utf-8') in data.keys():
                   data[word['text'].lower().encode('utf-8')]+=1;
                else:
                   data[word['text'].lower().encode('utf-8')]=1
    d= sorted(data.items(), key=operator.itemgetter(1),reverse=True)
    #print d
    for i in range(0,10):
        print("".join(map(str,re.findall("'([^']*)'",str(d[i][0])))),d[i][1])
    list(d,file)
    
def list(d,file):
    data ={}
    with open(file) as fp:
      for line in fp:
        if 'created_at' in json.loads(line).keys():
            a=json.loads(line)['entities']['hashtags']
            if(a == []):
                f=open("/home/manasa/Documents/Tweets/tweetsData-None.txt","w+")
                f.write(line)
                     
            for word in a:
                for i in range(0,10):
                    if word['text'].lower().encode('utf-8') == d[i][0].lower():
                        f=open("/home/manasa/Documents/Tweets/tweetsData-"+''.join(map(str,re.findall("'([^']*)'",str(d[i][0]))))+".txt","w+")
                        f.write(line)
                    else: 
                        f=open("/home/manasa/Documents/Tweets/tweetsData-Other.txt","w+")
                        f.write(line) 
    subprocess.getoutput('hdfs dfs -mkdir /Tweets')
    for i in range(0,10):
        subprocess.getoutput('hdfs dfs -mkdir /Tweets/'+''.join(map(str,re.findall("'([^']*)'",str(d[i][0])))))
        subprocess.getoutput('hdfs dfs -copyFromLocal /home/pujita/Documents/Tweets/tweetsData-'+''.join(map(str,re.findall("'([^']*)'",str(d[i][0]))))+'.txt /Tweets/'+''.join(map(str,re.findall("'([^']*)'",str(d[i][0])))))
    subprocess.getoutput('hdfs dfs -mkdir /Tweets/Other')
    subprocess.getoutput('hdfs dfs -copyFromLocal /home/pujita/Documents/Tweets/tweetsData-Other.txt /Tweets/Other')
    subprocess.getoutput('hdfs dfs -mkdir /Tweets/None')
    subprocess.getoutput('hdfs dfs -copyFromLocal /home/pujita/Documents/Tweets/tweetsData-None.txt /Tweets/None')
                           

def main():
    tweet_file = open(sys.argv[1])
    freq(sys.argv[1])


if __name__ == '__main__':
    main()
    

