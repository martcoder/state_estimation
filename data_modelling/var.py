#!/usr/bin/python3

import sys
import matplotlib
import matplotlib.pyplot as plot
import statistics

 #format to run is: python3 var.py <decimalplaces> <doPlot? y or n>
filenames = ["Accel15psi.data","Accel20psi.data","Accel25psi.data","Accel30psi.data","Accel35psi.data","Accel40psi.data",
"Accel45psi.data","Accel50psi.data","Accel55psi.data","Accel60psi.data"]
AccelMeansX = []
AccelModesX = []
AccelVarsX = []
AccelMeansY = []
AccelModesY = []
AccelVarsY = []

for filename in filenames:
 #filename = sys.argv[1]
 decimalPlaces = int(sys.argv[1])
 doplot = sys.argv[2]
 fileholder = open(filename,"r")
 Lines = fileholder.readlines() 
 varholderdict = dict()
 xList = []
 yList = []
 #varholderx15dict[1] = 0.1
 #varholderx15dict[2] = 0.34
 #varholderx15dict[3] = 0.12
 #print(varholderx15dict)
 #Populate x and y lists
 for line in Lines:
  linevals = line.split(',')
  xval = float(linevals[0])
  if xval >= 0:
    xList.append(float(linevals[0])) # x value
  yval = float(linevals[1])
  if yval >= 0:
    yList.append(float(linevals[1])) # y value

 #first let's just check the entire dataset variance.... 
 print("Before processing....\n")
 print("Total Var for X: "+str( statistics.variance(xList) )+"\n" )
 print("Total Var for Y: "+str( statistics.variance(yList) )+"\n" )

 #Now go over the data and do short-time variance :)
 window = 5
 lower = 0
 upper = window
 xVariances = []
 yVariances = []
 while upper < len(xList):
   xVariances.append( statistics.variance(xList[lower:upper]) )
   #yVariances.append( statistics.variance(yList[lower:upper]) )
   lower = lower + window
   upper = upper + window

 lower = 0
 upper = window
 while upper < len(yList):
   #xVariances.append( statistics.variance(xList[lower:upper]) )
   yVariances.append( statistics.variance(yList[lower:upper]) )
   lower = lower + window
   upper = upper + window



 logger = "log.txt"
 writer = open(logger,"a")
 writer.write( "For data: "+filename+"\n")
 writer.write( "Mode: "+str(statistics.mode(xVariances) )+"\n")
 writer.write( "Mean: "+str(statistics.mean(xVariances))  +"\n")
 writer.write( "Var: "+str(statistics.variance(xVariances))  +"\n\n")

 AccelMeansX.append(statistics.mean(xVariances))
 AccelModesX.append(statistics.mode(xVariances))
 AccelVarsX.append(statistics.variance(xVariances))

 AccelMeansY.append( statistics.mean(yVariances) )
 AccelModesY.append( statistics.mode(yVariances) )
 AccelVarsY.append( statistics.variance(yVariances) )

 if (doplot == "y"):
  print("Mode of xVariances is "+str(statistics.mode(xVariances) ) )
  print("Mean of xVariances is "+str(statistics.mean(xVariances)) )
  print("Var of xVariances is "+str(statistics.variance(xVariances)))

 if(doplot == "y"):
  plot.stem(xVariances)
  plot.show()


print("Accel X values means from 15 to 60 psi: " + str(AccelMeansX) +"\n" )
print("Accel X values modes from 15 to 60 psi: " + str(AccelModesX) +"\n" )
print("Accel X values variances from 15 to 60 psi: " + str(AccelVarsX) +"\n" )
print("Accel Y values means from 15 to 60 psi: " + str(AccelMeansY) +"\n" )
print("Accel Y values modes from 15 to 60 psi: " + str(AccelModesY) +"\n" )
print("Accel Y values variances from 15 to 60 psi: " + str(AccelVarsY) +"\n" )

print("Normalised results are: \n")
normAccelMeansX = [ e/max(AccelMeansX) for e in AccelMeansX ]
normAccelModesX = [ e/max(AccelModesX) for e in AccelModesX ]
normAccelVarsX = [ e/max(AccelVarsX) for e in AccelVarsX ]
normAccelMeansY = [ e/max(AccelMeansY) for e in AccelMeansY ]
normAccelModesY = [ e/max(AccelModesY) for e in AccelModesY ]
normAccelVarsY = [ e/max(AccelVarsY) for e in AccelVarsY ]

print("Normalised Accel X means: "+str(normAccelMeansX) + "\n")
print("Normalised Accel X modes: "+str(normAccelModesX) + "\n")
print("Normalised Accel X vars: "+str(normAccelVarsX) + "\n")
print("Normalised Accel Y means: "+str(normAccelMeansY) + "\n")
print("Normalised Accel Y modes: "+str(normAccelModesY) + "\n")
print("Normalised Accel Y vars: "+str(normAccelVarsY) + "\n")



 #Begin by choosing only data that is zero or over :)
 #for x in xList
  #print(line)
  #val = round(float(line),decimalPlaces)
  #try:
  # varholderdict[val] = varholderdict[val] + 1
  #except KeyError: 
  # varholderdict[val] = 1

#sortedVarholderdict = dict(sorted(varholderdict.items(),key= lambda x:x[1]))
#print(sortedVarholderdict)

#lastFew = list(sortedVarholderdict.items())
#print(lastFew[-1][0])
#lastFewKeys = [float(lastFew[-1][0]) , float(lastFew[-2][0]) , float(lastFew[-3][0]) , float(lastFew[-4][0]) , 
#float(lastFew[-5][0]) , float(lastFew[-6][0]) , float(lastFew[-7][0]) , float(lastFew[-8][0]) , 
#float(lastFew[-9][0]) , float(lastFew[-10][0]), float(lastFew[-11][0]), float(lastFew[-12][0]), float(lastFew[-13][0]), 
#float(lastFew[-14][0]), float(lastFew[-15][0]), float(lastFew[-16][0]), float(lastFew[-17][0]), float(lastFew[-18][0]), 
#float(lastFew[-19][0]), float(lastFew[-20][0])  ]
#lastFewSum = (float(lastFew[-1][0]) + float(lastFew[-2][0]) + float(lastFew[-3][0]) + float(lastFew[-4][0]) + 
#float(lastFew[-5][0]) + float(lastFew[-6][0]) + float(lastFew[-7][0]) + float(lastFew[-8][0]) + 
#float(lastFew[-9][0]) + float(lastFew[-10][0]) + float(lastFew[-11][0]) + float(lastFew[-12][0]) + float(lastFew[-13][0]) 
# + float(lastFew[-14][0]) + float(lastFew[-15][0]) + float(lastFew[-16][0]) + float(lastFew[-17][0]) + float(lastFew[-18][0]) 
#+ float(lastFew[-19][0]) + float(lastFew[-20][0])  )
#lastFewVar = statistics.variance(lastFewKeys) #float(lastFewSum) / 10.0;
#https://stackoverflow.com/questions/10543303/number-of-values-in-a-list-greater-than-a-certain-number
#countLessThan1 = 0
#for m in lastFewKeys:
# print("key is "+str(m))
# if( m < 1.0 ):
#    countLessThan1 += 1

#print('Last 20 Sum is: '+str(lastFewSum)+' and last20 Var is: '+str(lastFewVar)+' for '+filename +
# ', and key < 1: '+str(countLessThan1))

#if(doplot == "y"):
#  plot.stem(list(sortedVarholderdict.keys()),list(sortedVarholderdict.values()))
#  plot.show()
#plot.stem(xList)
#plot.show()
