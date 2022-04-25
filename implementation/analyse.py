#!/bin/python3

import matplotlib.pyplot as plot

print("Enter the filename to analyse >")
logname = input()
log = open(logname)

f60 = []
f40 = []
f20 = []

for line in log:
  cleaned = line.replace(" ","") #remove whitespace
  #print(cleaned)
  sep = cleaned.split(',')
  #states = sep.split(':')
  f60psi = sep[0].split(':')
  f40psi = sep[1].split(':')
  f20psi = sep[2].split(':')

  f60.append( float(f60psi[1])  )
  f40.append( float(f40psi[1])  )
  f20.append( float(f20psi[1])  )

  #print( str(f60psi[1])+" "+str(f40psi[1])+" "+str(f20psi[1]) )

plot.plot(f60,'o',label = "60psi predictions")
plot.plot(f40,'o',label = "40psi predictions")
plot.plot(f20,'o',label = "20psi predictions")
plot.legend()
#plot.xlabel('')
plot.ylabel('Prediction Probability')
plot.show()
