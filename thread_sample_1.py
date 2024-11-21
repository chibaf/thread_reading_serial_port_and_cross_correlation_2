import threading
import queue  # library for queu operation
import time

def thread1(i,q): # class body
  import time
  time.sleep(1)
  ret = i*i  # return value
  q.put(ret)   # set return value to queu
  return

i=1   # counter
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=thread1, args=(i,q),daemon=True)
# setting of thread
th.start() # start thread
while True:  # infinite loop
  if th.is_alive()==False:  #when thread ends
    result = q.get()  # take queu values
    print("thread: "+str(i)+" "+str(result))
    i=i+1
    if i>5:  # execute total five thread 
      break;  # exit loop
    th = threading.Thread(target=thread1, args=(i,q),daemon=True)
    # setting the next thread
    th.start() # start thread
  time.sleep(2)  #do other tasks

exit()
