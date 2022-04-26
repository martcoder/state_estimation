#!/bin/python3

import matplotlib.pyplot as plot
import statistics
import numpy

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

f60last10 = []
f40last10 = []
f20last10 = []

f60means = []
f40means = []
f20means = []
fmeansX = []

xval = 0
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
  if len(f60last10) < 10:
    f60last10.append( float(f60psi[1])  )
  else:
    f60last10 = f60last10[1:10] #truncate by 1
    f60last10.append( float(f60psi[1])  ) #append new value
  f60means.append( statistics.mean(f60last10)  )

  f40.append( float(f40psi[1])  )
  if len(f40last10) < 10:
    f40last10.append( float(f40psi[1])  )
  else:
    f40last10 = f40last10[1:10] #truncate by 1
    f40last10.append( float(f40psi[1])  ) #append new value
  f40means.append( statistics.mean(f40last10)  )

  f20.append( float(f20psi[1])  )
  if len(f20last10) < 10:
    f20last10.append( float(f20psi[1])  )
  else:
    f20last10 = f20last10[1:10] #truncate by 1
    f20last10.append( float(f20psi[1])  ) #append new value
  f20means.append( statistics.mean(f20last10)  )
 
  #create x values for matplotlib
  fmeansX.append(xval)
  xval = xval + 1

  f60a.append( float(f60psiA[1]) )
  f40a.append( float(f40psiA[1]) )
  f20a.append( float(f20psiA[1]) )

  f60l.append( float(f60psiL[1]) )
  f40l.append( float(f40psiL[1]) )
  f20l.append( float(f20psiL[1]) )


print("First half 60 avg prob: "+str(statistics.mean(f60[0:30000]))+"\n")
print("Second half 60 avg prob: "+str(statistics.mean(f60[30000:60000]))+"\n")
print("First half 40 avg prob: "+str(statistics.mean(f40[0:30000]))+"\n")
print("Second half 40 avg prob: "+str(statistics.mean(f40[30000:60000]))+"\n")
print("First half 20 avg prob: "+str(statistics.mean(f20[0:30000]))+"\n")
print("Second half 20 avg prob: "+str(statistics.mean(f20[30000:60000]))+"\n")


  #print( str(f60psi[1])+" "+str(f40psi[1])+" "+str(f20psi[1]) )

plot.plot(f40,'x',color='orange',label = "40psi predictions")
plot.plot(f60,'x',color='blue',label = "60psi predictions")
plot.plot(f20,'x',color='lime',label = "20psi predictions")
z60 = numpy.polyfit(fmeansX,f60, 1)
p60 = numpy.poly1d(z60)
plot.plot(fmeansX,p60(fmeansX),"--",color="dodgerblue",label = "60psi trend")
z40 = numpy.polyfit(fmeansX,f40, 1)
p40 = numpy.poly1d(z40)
plot.plot(fmeansX,p40(fmeansX),"r--",label = "40psi trend")
z20 = numpy.polyfit(fmeansX,f20, 1)
p20 = numpy.poly1d(z20)
plot.plot(fmeansX,p20(fmeansX),"--",color="darkgreen",label = "20psi trend")
plot.legend()
plot.xlabel('Number of predictions')
plot.ylabel('Prediction Probability')
plot.title('Sensor Fusion Predictions for pressure drop of 60psi to 15psi')
plot.show()

plot.plot(f40means,'x',color='orange',label = "40psi predictions")
plot.plot(f60means,'x',color='blue',label = "60psi predictions")
plot.plot(f20means,'x',color='lime',label = "20psi predictions")
z = numpy.polyfit(fmeansX,f60means, 1)
p = numpy.poly1d(z)
plot.plot(fmeansX,p(fmeansX),"--",color="dodgerblue",label = "60psi trend")
z40 = numpy.polyfit(fmeansX,f40means, 1)
p40 = numpy.poly1d(z40)
plot.plot(fmeansX,p40(fmeansX),"r--",label = "40psi trend")

z20 = numpy.polyfit(fmeansX,f20means, 1)
p20 = numpy.poly1d(z20)
plot.plot(fmeansX,p20(fmeansX),"--",color="darkgreen",label = "20psi trend")
plot.legend()
plot.xlabel('Number of predictions')
plot.ylabel('Average Prediction Probability For Last 10 Values')
plot.title('Running Averages: Sensor Fusion Predictions for pressure drop of 60psi to 15psi')
plot.show()

plot.plot(f60a,'x',color='blue',label = "60psi predictions")
plot.plot(f40a,'x',color='orange',label = "40psi predictions")
plot.plot(f20a,'x',color='lime',label = "20psi predictions")
z60 = numpy.polyfit(fmeansX,f60a, 1)
p60 = numpy.poly1d(z60)
plot.plot(fmeansX,p60(fmeansX),"--",color="dodgerblue",label = "60psi trend")
z40 = numpy.polyfit(fmeansX,f40a, 1)
p40 = numpy.poly1d(z40)
plot.plot(fmeansX,p40(fmeansX),"r--",label = "40psi trend")
z20 = numpy.polyfit(fmeansX,f20a, 1)
p20 = numpy.poly1d(z20)
plot.plot(fmeansX,p20(fmeansX),"--",color="darkgreen",label = "20psi trend")
plot.legend()
plot.xlabel('Number of predictions')
plot.ylabel('Prediction Probability')
plot.title('Accelerometer Predictions for pressure drop of 60psi to 15psi')
plot.show()

plot.plot(f60l,'x',color='blue',label = "60psi predictions")
plot.plot(f40l,'x',color='orange',label = "40psi predictions")
plot.plot(f20l,'x',color='lime',label = "20psi predictions")
z60 = numpy.polyfit(fmeansX,f60l, 1)
p60 = numpy.poly1d(z60)
plot.plot(fmeansX,p60(fmeansX),"--",color="dodgerblue",label = "60psi trend")
z40 = numpy.polyfit(fmeansX,f40l, 1)
p40 = numpy.poly1d(z40)
plot.plot(fmeansX,p40(fmeansX),"r--",label = "40psi trend")
z20 = numpy.polyfit(fmeansX,f20l, 1)
p20 = numpy.poly1d(z20)
plot.plot(fmeansX,p20(fmeansX),"--",color="darkgreen",label = "20psi trend")
plot.legend()
plot.xlabel('Number of predictions')
plot.ylabel('Prediction Probability')
plot.title('Lidar Predictions for pressure drop of 60psi to 15psi')
plot.show()



