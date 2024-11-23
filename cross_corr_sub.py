import numpy as np
import serial,time

def find_index(c):  # find index of maximum value
  mc=np.amax(c)
  for i in range(len(c)):
    if c[i]==mc:
      im=i
      break
  return im
  
def curv0(i,x):
  if 1<=i<25+x:
    val=0.
  elif 25+x<=i<35+x:
    val=np.sin((i-25)*np.pi/10.)
  else:
    val=0.
  return val
  
def curv1(i,x):
  if 0<=i<55+x:
    val=0
  elif 55+x<=i<65+x:
    val=np.sin((i-55)*np.pi/10.)
  else:
    val=0.
  return val

def cross_corr(x,y,q):
  i=0
  d1=np.empty(0)
  d2=np.empty(0)
  while True:
    r0=curv0(i,x)
    r1=curv1(i,y)
    if i<100:
      d1=np.append(d1,np.float32(r0))
      d2=np.append(d2,np.float32(r1))
      i=i+1
    else:
      c=1.0/(np.linalg.norm(d1)*np.linalg.norm(d2)) 
      f1=np.fft.fft(d1)
      f2=np.conjugate(np.fft.fft(d2))
      ff=f1*f2
      corrf=np.real(np.fft.ifft(ff))*c
      indx=find_index(corrf)
      break
  q.put(indx)