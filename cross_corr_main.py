import threading
import queue
import random
import cross_corr_sub
#
i=0
x=0
y=0
q =queue.Queue()  # queue which stores a result of a thread
#
while True:
  if threading.active_count()==1:
    if i>0:
      indx = q.get()
      print(indx)
    if i>=10:
      break;
    x=random.randint(-5,5)
    y=random.randint(-5,5)
    th = threading.Thread(target=cross_corr_sub.cross_corr, args=(x,y,q),daemon=True)
    th.start()
    i=i+1
    print("start thread: "+str(i))
exit()
