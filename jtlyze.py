import sys
import os
import pandas as pd
from datetime import datetime


inputfilename = sys.argv[1]
outputfilename = inputfilename.replace('jtl','txt')
outputdirname = 'out'


colnames=['timeStamp','elapsed','label','responseCode','responseMessage','threadName','dataType','success','failureMessage','bytes','sentBytes','grpThreads','allThreads','Latency','IdleTime','Connect'] 
df = pd.read_csv('logs/'+inputfilename, names=colnames, header=0)


if not os.path.exists(outputdirname):
    os.mkdir(outputdirname)
    print('Directory' , outputdirname ,  'Created.')
else:    
    print('Directory' , outputdirname ,  'already exists.')


successresponses = df[df.responseCode == 200].shape[0]
datalength = len(df.index)
responsesuccesspercentage = round((successresponses / datalength) * 100, 1)


df['endTime'] = df['timeStamp'] + df['elapsed']
starttime = df['timeStamp'].min()
endtime = df['endTime'].max()
totaltimeseconds = (endtime - starttime) /1000
totalsentbytes = df['sentBytes'].sum()
totalreceivedbytes = df['bytes'].sum()


sourcefile = open('out/'+outputfilename, 'w')
print(inputfilename, file = sourcefile)
print('Total number of threads: ', df['threadName'].nunique(), file = sourcefile)
print('OK response rate:', responsesuccesspercentage,'%', file = sourcefile)
print('Minimum request time:', df['elapsed'].min(), file = sourcefile)
print('Maximumm request time:', df['elapsed'].max(), file = sourcefile)
print('Average request time:', round(df['elapsed'].mean()), file = sourcefile)
print('Request time 90th percentile:', round(df['elapsed'].quantile(0.9)), file = sourcefile)
print('Request time standard deviation:', round(df['elapsed'].std(), 1), file = sourcefile)
print('Minimum latency:', df['Latency'].min(), file = sourcefile)
print('Maximumm latency:', df['Latency'].max(), file = sourcefile)
print('Average latency:', round(df['Latency'].mean()), file = sourcefile)
print('Latency 90th percentile:', round(df['Latency'].quantile(0.9)), file = sourcefile)
print('Latency standard deviation:', round(df['Latency'].std(), 1), file = sourcefile)
print('Total duration:', totaltimeseconds, 'seconds', file = sourcefile)
print('Total bytes sent:', totalsentbytes, file = sourcefile)
print('Total bytes received:', totalreceivedbytes, file = sourcefile)
print('Send rate:', round(((totalsentbytes / 1000) / totaltimeseconds), 1),'KB/sec', file = sourcefile)
print('Receive rate:', round(((totalreceivedbytes / 1000) / totaltimeseconds), 1),'KB/sec', file = sourcefile)
print('Throughput:', round(datalength / totaltimeseconds,2), 'requests per second' , file = sourcefile)
sourcefile.close()

print('File', outputfilename, 'has been written to', outputdirname, 'directory.')
