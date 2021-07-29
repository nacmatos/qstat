
# qstat.py

Apache QPID statistics tool.  

## Getting Started

This script will return the server load and some Qpid broker usefull counters.  
Similar to dstat.  


## Usage

```
 $ ./qstat.py --help
 Usage: qstat.py deltat
 Options:
  -h, --help show this help message and exit
  -d DELTAT, --deltat=DELTAT

 $ ./qstat.py

           Timestamp        Load-1m     Enqueues/s     EnqBytes/s         MsgLen     Dequeues/s    DenqBytes/s       MsgDepth     Discards/s
 2021-07-29 12:09:23           0.91              1          1.53K           1528              1          1.53K              0              0
 2021-07-29 12:09:24           0.91              1          1.54K           1544              1          1.54K              0              0
 2021-07-29 12:09:25           0.91              1          1.54K           1544              1          1.54K              0              0
 2021-07-29 12:09:26           0.91              1          1.54K           1544              1          1.54K              0              0
 2021-07-29 12:09:27           0.83              1          1.54K           1544              1          1.54K              0              0
 ^C

```
## Author

Nereu Matos - nacmatos  

## License

This project is licensed under the MIT License.  
