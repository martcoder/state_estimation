#!/bin/python3

import matplotlib.pyplot as plot

print("Enter the filename to analyse >")
logname = input()
log = open(logname)

f60 = []
f40 = []
f20 = []

f60a = []
f40a = []
f20a = []

f60l = []
f40l = []
f20l = []

for line in log:
  cleaned = line.replace(" ","") #remove whitespace
  #print(cleaned)
  sep = cleaned.split(',')
  #states = sep.split(':')
  f60psi = sep[0].split(':')
  f40psi = sep[1].split(':')
  f20psi = sep[2].split(':')

  f60psiA = sep[3].split(':')
  f40psiA = sep[4].split(':')
  f20psiA = sep[5].split(':')

  f60psiL = sep[6].split(':')
  f40psiL = sep[7].split(':')
  f20psiL = sep[8].split(':')

  f60.append( float(f60psi[1])  )
  f40.append( float(f40psi[1])  )
  f20.append( float(f20psi[1])  )

  f60a.append( float(f60psiA[1]) )
  f40a.append( float(f40psiA[1]) )
  f20a.append( float(f20psiA[1]) )

  f60l.append( float(f60psiL[1]) )
  f40l.append( float(f40psiL[1]) )
  f20l.append( float(f20psiL[1]) )


  #print( str(f60psi[1])+" "+str(f40psi[1])+" "+str(f20psi[1]) )

plot.plot(f20,'o',color='green',label = "60psi predictions")
plot.plot(f40,'o',color='orange',label = "40psi predictions")
plot.plot(f60,'o',color='blue',label = "20psi predictions")
plot.legend()
plot.xlabel('Number of predictions')
plot.ylabel('Prediction Probability')
plot.title('Sensor Fusion Predictions for 60psi')
plot.show()

plot.plot(f20a,'o',color='green',label = "60psi predictions")
plot.plot(f40a,'o',color='orange',label = "40psi predictions")
plot.plot(f60a,'o',color='blue',label = "20psi predictions")
plot.legend()
plot.xlabel('Number of predictions')
plot.ylabel('Prediction Probability')
plot.title('Accelerometer Predictions for 60psi')
plot.show()

plot.plot(f20l,'o',color='green',label = "60psi predictions")
plot.plot(f40l,'o',color='orange',label = "40psi predictions")
plot.plot(f60l,'o',color='blue',label = "20psi predictions")
plot.legend()
plot.xlabel('Number of predictions')
plot.ylabel('Prediction Probability')
plot.title('Lidar Predictions for 60psi')
plot.show()



