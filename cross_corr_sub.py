import numpy as np
import serial,time

def find_index(c):  # find index of maximum value
  mc=np.amax(c)
  for i in range(len(c)):
    if c[i]==mc:
      im=i
      break
  return im
  
def curv0(i):
  if 1<=i<25:
    ret=0
  elif 25<=i<35:
    ret=np.sin((i-25)*np.pi/10.)
  else:
    ret=0.
  return ret
  
def curv1(i):
  if 45<=i<55:
    ret=0
  elif 55<=i<65:
    ret=np.sin((i-55)*np.pi/10.)
  else:
    ret=0.
  return ret

def cross_corr(x,q):
  time.sleep(10)
  i=0
  d1=np.empty(0)
  d2=np.empty(0)
  while True:
    r0=curv0(i)
    r1=curv1(i)
    if i<100:
      d1=np.append(d1,np.float32(r0))
      d2=np.append(d2,np.float32(r1))
      i=i+1
    else:
      if len(d1)!=0:
        c=1.0/(np.linalg.norm(d1)*np.linalg.norm(d2)) 
        f1=np.fft.fft(d1)
        f2=np.conjugate(np.fft.fft(d2))
        ff=f1*f2
        corrf=np.real(np.fft.ifft(ff))*c
        ix=find_index(corrf)
        break
  q.put(ix)