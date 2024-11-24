class cross_corr_serial():

  def __init__(self,port,speed):
    import serial
    self.ser=serial.Serial(port,speed)

  def cross_corr(self,x,q):
    import numpy as np
    import serial,time
    import index_sub
    time.sleep(1)
    i=0
    d1=np.empty(0)
    d2=np.empty(0)
    while True:
      line = self.ser.readline()
      line2=line.strip().decode('utf-8',errors='replace')
      data = [str(val) for val in line2.split(",")]
      if i<100 and len(data)==11:
        d1=np.append(d1,np.float32(data[1]))
        d2=np.append(d2,np.float32(data[2]))
        i=i+1
      else:
        if len(d1)!=0:
          c=1.0/(np.linalg.norm(d1)*np.linalg.norm(d2)) 
          f1=np.fft.fft(d1)
          f2=np.conjugate(np.fft.fft(d2))
          ff=f1*f2
          corrf=np.real(np.fft.ifft(ff))*c
          ix=index_sub.find_index(corrf)
          break
    self.ser.close()
    q.put(ix)