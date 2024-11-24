import threading
import queue,time
import serial,sys
from cross_corr_via_serial_class import cross_corr_serial

i=0;k=1
q =queue.Queue()  # queue which stores a result of a thread
while True:
  if threading.active_count()==1:
    if i>0:
      ix = q.get()
      print(ix)
    i=i+1
    if i>5:
      break;
    serial_cross_corr=cross_corr_serial("/dev/ttyACM0",19200)
    th = threading.Thread(target=serial_cross_corr.cross_corr, args=(k,q),daemon=True)
    th.start()
    print("start thread: "+str(i))
exit()
