# jtlyze
Python program for jtl log analysis.

Usage: Run using command line and give log file as argument, e.g. "python jtlyze.py log1.jtl"
Program should be in same location as Logs directory. Such as:

                  Directory
                    |-jtlyze.py
                    |-out
                    |-logs
                       |-log1.jtl
                       |-log2.jtl
                    
  
If no out directory exists, one will be created. Text file containing log analysys will be written into out directory with same name(but .txt extension) as input file.
Analysis file contains:
      Name of original JTL file
      Total number of threads
      OK response rate
      Minimum request time
      Maximumm request time
      Average request time
      Request time 90th percentile 
      Request time standard deviation 
      Minimum latency
      Maximumm latency
      Average latency
      Latency 90th percentile 
      Latency standard deviation
      Total duration
      Total bytes sent
      Total bytes received
      Send rate
      Receive rate  
      Throughput 


Requirements:
  Pandas
 
