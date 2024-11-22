import threading
import queue,time
import serial,sys
import random
import cross_corr_sub

i=1
q =queue.Queue()  # queue which stores a result of a thread
x=0
y=0
th = threading.Thread(target=cross_corr_sub.cross_corr, args=(x,y,q),daemon=True)
th.start()
print("start thread: "+str(i))
#th.join()
while True:
  if threading.active_count()==1:
    ix = q.get()
    print(ix)
    i=i+1
    if i>11:
      break;
    x=random.randint(-5,5)
    y=random.randint(-5,5)
    th = threading.Thread(target=cross_corr_sub.cross_corr, args=(x,y,q),daemon=True)
    th.start()
    print("start thread: "+str(i))
exit()
