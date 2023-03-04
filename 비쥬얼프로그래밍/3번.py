from datetime import datetime,time
from time import sleep
filename='time.txt'
try:
    f=open(filename,'r')
except IOError:
    f1=open(filename,'w')
    f1.write('0:00:00\n')
    f1.close()
    f=open(filename,'r')
firsttime=f.readline()
f.close()
timestamp=datetime.strptime(firsttime, '%H:%M:%S')
while True:#위에 처리시간 ms단위라서 무시
    time1=datetime.now()
    sleep(1)
    time2=datetime.now()
    time=timestamp+time2-time1
    print(time)
    f=open(filename,'w')
    f.write('%s\n'%str(time))
    f.close
    