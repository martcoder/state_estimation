#!/usr/bin/python3

import os
import sys
import matplotlib
import matplotlib.pyplot as plot
import statistics

#format to run is: python3 pmf.py <filename> <decimalplaces> <doPlot? y or n>
filename = sys.argv[1]
filenames = ["Lidar15psi.datavarholder.data","Lidar20psi.datavarholder.data","Lidar25psi.datavarholder.data","Lidar30psi.datavarholder.data","Lidar35psi.datavarholder.data","Lidar40psi.datavarholder.data",
"Lidar45psi.datavarholder.data","Lidar50psi.datavarholder.data","Lidar55psi.datavarholder.data","Lidar60psi.datavarholder.data"]
for filename in filenames:
 decimalPlaces = int(sys.argv[2])
 doplot = sys.argv[3]
 varholder = open(filename,"r")
 Lines = varholder.readlines() 
 # Now create a dictionary with custom scaling bin sizes 
 varholderdict = dict()
 varholderdict[0.0] = 0.0
 varholderdict[0.05] = 0.0
 varholderdict[0.1] = 0.0
 varholderdict[0.2] = 0.0
 varholderdict[0.3] = 0.0
 varholderdict[0.4] = 0.0
 varholderdict[0.5] = 0.0
 varholderdict[0.6] = 0.0
 varholderdict[0.7] = 0.0
 varholderdict[0.8] = 0.0
 varholderdict[0.9] = 0.0
 varholderdict[1.0] = 0.0
 varholderdict[1.5] = 0.0
 varholderdict[2.0] = 0.0
 varholderdict[2.5] = 0.0
 varholderdict[3.0] = 0.0
 varholderdict[4.0] = 0.0
 varholderdict[5.0] = 0.0
 varholderdict[6.0] = 0.0
 varholderdict[7.0] = 0.0
 varholderdict[8.0] = 0.0
 varholderdict[9.0] = 0.0
 varholderdict[10.0] = 0.0
 varholderdict[11.0] = 0.0
 varholderdict[12.0] = 0.0
 varholderdict[13.0] = 0.0
 varholderdict[14.0] = 0.0
 varholderdict[15.0] = 0.0
 varholderdict[16.0] = 0.0
 varholderdict[17.0] = 0.0
 varholderdict[18.0] = 0.0
 varholderdict[19.0] = 0.0
 varholderdict[20.0] = 0.0
 varholderdict[30.0] = 0.0
 varholderdict[40.0] = 0.0
 varholderdict[50.0] = 0.0
 varholderdict[60.0] = 0.0
 varholderdict[70.0] = 0.0
 varholderdict[80.0] = 0.0
 varholderdict[90.0] = 0.0
 varholderdict[100.0] = 0.0
 varholderdict[200.0] = 0.0
 varholderdict[300.0] = 0.0
 varholderdict[400.0] = 0.0
 varholderdict[500.0] = 0.0
 varholderdict[600.0] = 0.0
 varholderdict[700.0] = 0.0
 varholderdict[800.0] = 0.0
 varholderdict[900.0] = 0.0
 varholderdict[1000.0] = 0.0
 varholderdict[1200.0] = 0.0
 varholderdict[1400.0] = 0.0
 varholderdict[1600.0] = 0.0
 varholderdict[1800.0] = 0.0
 varholderdict[2000.0] = 0.0
 varholderdict[2500.0] = 0.0
 varholderdict[3000.0] = 0.0
 varholderdict[3500.0] = 0.0
 varholderdict[4000.0] = 0.0
 varholderdict[4500.0] = 0.0
 varholderdict[5000.0] = 0.0
 #varholderx15dict[1] = 0.1
 #varholderx15dict[2] = 0.34
 #varholderx15dict[3] = 0.12
 #print(varholderx15dict)
 for line in Lines:
  #print(line)
  val = float(line)
  # Add to the dictionary based on the scaled bins
  if val < 0.05: 
   varholderdict[0.0] = varholderdict[0.0] + 1.0
  elif (val >= 0.05) and (val < 0.1):
   varholderdict[0.05] = varholderdict[0.05] + 1.0
  elif (val >= 0.1) and (val < 0.2):
   varholderdict[0.1] += 1.0
  elif (val >= 0.2) and (val < 0.3):
   varholderdict[0.2] += 1.0
  elif (val >= 0.3) and (val < 0.4):
   varholderdict[0.3] += 1.0
  elif (val >= 0.4) and (val < 0.5):
   varholderdict[0.4] += 1.0
  elif (val >= 0.5) and (val < 0.6):
   varholderdict[0.5] += 1.0
  elif (val >= 0.6) and (val < 0.7):
   varholderdict[0.6] += 1.0
  elif (val >= 0.7) and (val < 0.8):
   varholderdict[0.7] += 1.0
  elif (val >= 0.8) and (val < 0.9):
   varholderdict[0.8] += 1.0
  elif (val >= 0.9) and (val < 1.0):
   varholderdict[0.9] += 1.0
  elif (val >= 1.0) and (val <1.5):
   varholderdict[1.0] += 1.0
  elif (val >= 1.5) and (val < 2.0):
   varholderdict[1.5] += 1.0
  elif (val >= 2.0) and (val < 2.5):
   varholderdict[2.0] += 1.0
  elif (val >= 2.5) and (val < 3.0):
   varholderdict[2.5] += 1.0
  elif (val >= 3.0) and (val < 4.0):
   varholderdict[3.0] += 1.0
  elif (val >= 4.0) and (val < 5.0):
   varholderdict[4.0] += 1.0
  elif (val >= 5.0) and (val < 6.0):
   varholderdict[5.0] += 1.0
  elif (val >= 6.0) and (val < 7.0): 
   varholderdict[6.0] += 1.00
  elif (val >= 7.0) and (val < 8.0):
   varholderdict[7.0] += 1.0
  elif (val >= 8.0) and (val < 9.0):
   varholderdict[8.0] += 1.0
  elif (val >= 9.0) and (val < 10.0):
   varholderdict[9.0] += 1.0
  elif (val >= 10.0) and (val < 11.0):
   varholderdict[10.0] += 1.0
  elif (val >= 11.0) and (val < 12.0):
   varholderdict[11.0] += 1.0
  elif (val >= 12.0) and (val < 13.0):
   varholderdict[12.0] += 1.0
  elif (val >= 13.0) and (val < 14.0):
   varholderdict[13.0] += 1.0
  elif (val >= 14.0) and (val < 15.0):
   varholderdict[14.0] += 1.0
  elif (val >= 15.0) and (val < 16.0):
   varholderdict[15.0] += 1.0
  elif (val >= 16.0) and (val < 17.0): 
   varholderdict[16.0] += 1.0
  elif (val >= 17.0) and (val < 18.0): 
   varholderdict[17.0] += 1.0
  elif (val >= 18.0) and (val < 19.0):
   varholderdict[18.0] += 1.0
  elif (val >= 19.0) and (val < 20.0):
   varholderdict[19.0] += 1.0
  elif (val >= 20.0) and (val < 30.0):
   varholderdict[20.0] += 1.0
  elif (val >= 30.0) and (val < 40.0):
   varholderdict[30.0] += 1.0
  elif (val >= 40.0) and (val < 50.0):
   varholderdict[40.0] += 1.0
  elif (val >= 50.0) and (val < 60.0):
   varholderdict[50.0] += 1.0
  elif (val >= 60.0) and (val < 70.0):
   varholderdict[60.0] += 1.00
  elif (val >= 70.0) and (val < 80.0):
   varholderdict[70.0] += 1.0
  elif (val >= 80.0) and (val < 90.0):
   varholderdict[80.0] += 1.0
  elif (val >= 90.0) and (val < 100.0):
   varholderdict[90.0] += 1.0
  elif (val >= 100.0) and (val < 200.0):
   varholderdict[100.0] += 1.0
  elif (val >= 200.0) and (val < 300.0):
   varholderdict[200.0] += 1.0
  elif (val >= 300.0) and (val < 400.0):
   varholderdict[300.0] += 1.0
  elif (val >= 400.0) and (val < 500.0):
   varholderdict[400.0] += 1.0
  elif (val >= 500.0) and (val < 600.0):
   varholderdict[500.0] += 1.0
  elif (val >= 600.0) and (val < 700.0):
   varholderdict[600.0] += 1.0
  elif (val >= 700.0) and (val < 800.0):
   varholderdict[700.0] += 1.0
  elif (val >= 800.0) and (val < 900.0):
   varholderdict[800.0] += 1.0
  elif (val >= 900.0) and (val < 1000.0):
   varholderdict[900.0] += 1.0
  elif (val >= 1000.0) and (val < 1200.0):
   varholderdict[1000.0] += 1.0
  elif (val >= 1200.0) and (val < 1400.0):
   varholderdict[1200.0] += 1.0
  elif (val >= 1400.0) and (val < 1600.0):
   varholderdict[1400.0] += 1.0
  elif (val >= 1600.0) and (val < 1800.0):
   varholderdict[1600.0] += 1.0
  elif (val >= 1800.0) and (val < 2000.0):
   varholderdict[1800.0] += 1.0
  elif (val >= 2000.0) and (val < 2200.0):
   varholderdict[2000.0] += 1.0
  elif (val >= 2500.0) and (val < 3000.0):
   varholderdict[2500.0] += 1.0
  elif (val >= 3000.0) and (val < 3500.0):
   varholderdict[3000.0] += 1.0
  elif (val >= 3500.0) and (val < 4000.0):
   varholderdict[3500.0] += 1.0
  elif (val >= 4000.0) and (val < 4500.0):
   varholderdict[4000.0] += 1.0
  elif (val >= 4500.0) and (val < 5000.0):
   varholderdict[4500.0] += 1.0
  elif (val >= 5000.0):
   varholderdict[5000.0] += 1.0

  #try:
  # varholderdict[val] = varholderdict[val] + 1
  #except KeyError: 
  # varholderdict[val] = 1
 #for loop ends here

 sortedVarholderdict = dict(sorted(varholderdict.items(),key= lambda x:x[1]))
 print(sortedVarholderdict)

 #Now normalise the histogram
 normalisedHist = dict(sortedVarholderdict)
 #Find the max value...
 max = 0
 for x in sortedVarholderdict.items():
  if x[1] > max:
   max = x[1]
 for kv in normalisedHist.items():
   normalisedHist[kv[0]] = kv[1]/max

 #Now write to file as keys in 1st column, values in 2nd column
 try:
  os.remove(filename+"varhistogram.data")
 except FileNotFoundError:
  pass
 writerVars = open(filename+"varhistogram.data","a")
 for x in list(normalisedHist.items()):
  writerVars.write(str(x[0])+","+str(x[1])+"\n")

 lastFew = list(sortedVarholderdict.items())
 print(lastFew[-1][0])
 lastFewKeys = [float(lastFew[-1][0]) , float(lastFew[-2][0]) , float(lastFew[-3][0]) , float(lastFew[-4][0]) , 
float(lastFew[-5][0]) , float(lastFew[-6][0]) , float(lastFew[-7][0]) , float(lastFew[-8][0]) , 
float(lastFew[-9][0]) , float(lastFew[-10][0]), float(lastFew[-11][0]), float(lastFew[-12][0]), float(lastFew[-13][0]), 
float(lastFew[-14][0]), float(lastFew[-15][0]), float(lastFew[-16][0]), float(lastFew[-17][0]), float(lastFew[-18][0]), 
float(lastFew[-19][0]), float(lastFew[-20][0])  ]
 lastFewSum = (float(lastFew[-1][0]) + float(lastFew[-2][0]) + float(lastFew[-3][0]) + float(lastFew[-4][0]) + 
float(lastFew[-5][0]) + float(lastFew[-6][0]) + float(lastFew[-7][0]) + float(lastFew[-8][0]) + 
float(lastFew[-9][0]) + float(lastFew[-10][0]) + float(lastFew[-11][0]) + float(lastFew[-12][0]) + float(lastFew[-13][0]) 
+ float(lastFew[-14][0]) + float(lastFew[-15][0]) + float(lastFew[-16][0]) + float(lastFew[-17][0]) + float(lastFew[-18][0]) 
+ float(lastFew[-19][0]) + float(lastFew[-20][0])  )
 lastFewVar = statistics.variance(lastFewKeys) #float(lastFewSum) / 10.0;
 #https://stackoverflow.com/questions/10543303/number-of-values-in-a-list-greater-than-a-certain-number
 countLessThan1 = 0
 for m in lastFewKeys:
  print("key is "+str(m))
  if( m < 1.0 ):
     countLessThan1 += 1

 print('Last 20 Sum is: '+str(lastFewSum)+' and last20 Var is: '+str(lastFewVar)+' for '+filename +
 ', and key < 1: '+str(countLessThan1))

 if(doplot == "y"):
   plot.stem(list(normalisedHist.keys()),list(normalisedHist.values()))
   plot.show()

