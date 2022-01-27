import numpy as np
import sys

file = None
if len(sys.argv) == 2:
  file = open(sys.argv[1],'r')
else:
  print("Need a filename argument when starting")
  exit()

datalist = file.readlines()

fourierTransform = np.fft.fft(datalist)

frequencies = np.fft.fftfreq( len(datalist), d=0.01)
print(frequencies)
