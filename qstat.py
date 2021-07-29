#!/usr/bin/python
'''

 2021-07-24 Nereu

 Ver: https://qpid.apache.org/releases/qpid-cpp-1.39.0/cpp-broker/book/ch02s03.html#QMFPythonConsoleTutorial-CreatingaQMFConsoleSessionandAttachingtoaBroker

'''

from datetime import datetime
from optparse import OptionParser
from time import sleep

from qmf.console import Session

def human_format(num):
    ''' Retirado de https://stackoverflow.com/questions/579310/formatting-long-numbers-as-strings-in-python '''
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

parser = OptionParser(usage='%prog deltat')
parser.add_option('--deltat', '-d', type="int",default=1)
opts, args = parser.parse_args()

sess = Session()
broker = sess.addBroker("amqp://localhost")

br = sess.getObjects(_class="broker", _package="org.apache.qpid.broker")[0]

dt=float(opts.deltat)

d1 = (br.msgTotalEnqueues, br.byteTotalEnqueues, br.msgTotalDequeues, br.byteTotalDequeues, br.discardsNoRoute)

n=0

while True:
  try:

    if (n % 22)==0:
      print '\n{:>19} {:>14} {:>14} {:>14} {:>14} {:>14} {:>14} {:>14} {:>14}'.format(
        'Timestamp', 'Load-1m', 'Enqueues/s', 'EnqBytes/s', 'MsgLen', 'Dequeues/s', 'DenqBytes/s', 'MsgDepth', 'Discards/s'
      )

    br.update()

    d2 = (br.msgTotalEnqueues, br.byteTotalEnqueues, br.msgTotalDequeues, br.byteTotalDequeues, br.discardsNoRoute)

    with open('/proc/loadavg','r') as f: (l1, l5, l15, _, __)=f.read().split()

    if (d2[0] - d1[0]) > 0:
      msgLen = int( float(d2[1] - d1[1]) / float(d2[0] - d1[0]) + 0.5 )
    else:
      msgLen = 'N/A'
    

    print('{:>19} {:>14} {:>14} {:>14} {:>14} {:>14} {:>14} {:>14} {:>14}'.format(
            datetime.now().isoformat(sep=' ')[:-7], 
            l1,
            human_format(float(d2[0] - d1[0])/dt), 
            human_format(float(d2[1] - d1[1])/dt), 
            msgLen,
            human_format(float(d2[2] - d1[2])/dt), 
            human_format(float(d2[3] - d1[3])/dt), 
            br.msgDepth,
            human_format(float(d2[4] - d1[4])/dt) )
    )

    d1 = d2

    sleep(opts.deltat)

    n += 1
    

  except KeyboardInterrupt: 
    break
  except Exception as e:
    print(e)
    break
   

try:
 delBroker(broker)
 sess.close()
except:
 pass

