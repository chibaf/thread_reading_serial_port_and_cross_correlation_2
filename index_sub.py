def find_index(c):  # find index of maximum value
  import numpy as np
  mc=np.amax(c)
  for i in range(len(c)):
    if c[i]==mc:
      indx=i
      break
  return indx
