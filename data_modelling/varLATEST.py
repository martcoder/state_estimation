#!/usr/bin/python3

import sys
import os
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

AccelWindowedMeansX = []
AccelWindowedModesX = []
AccelWindowedMeansY = []
AccelWindowedModesY = []

meanLidarVariances = []
modeLidarVariances = []
varLidarVariances = []

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

 counter = 0
 limit = 10000
 for line in Lines:
  counter += 1
  linevals = line.split(',')
  xval = float(linevals[0])
  if (xval > -3000) and (xval < 3000): #  and (counter < limit): #remove outliers and negatives
    xList.append(round(float(linevals[0]),decimalPlaces)) # x value with rounded decimal places
  yval = float(linevals[1])
  if (yval > -1000) and (yval < 1000): #  and (counter < limit): # remove outliers and negatives
    yList.append(round( float(linevals[1]),decimalPlaces ) ) # y value

 #first let's just check the entire dataset variance.... 
 print("Before processing....\n")
 #print(xList)
 print("Total Var for X: "+str( statistics.variance(xList) )+"\n" )
 print("Total Var for Y: "+str( statistics.variance(yList) )+"\n" )

 #Now go over the data and do FIR filter with size 4
 filterSize = 4
 filterCoeff = 0.25
 for index in range(filterSize,len(xList)):
  xList[index] = (filterCoeff*xList[index]) + (filterCoeff*xList[index-1]) + (filterCoeff*xList[index-2]) + (filterCoeff*xList[index-3]) #+ (filterCoeff*xList[index-4])

 for index in range(filterSize,len(yList)):
  yList[index] = (filterCoeff*yList[index]) + (filterCoeff*yList[index-1]) + (filterCoeff*yList[index-2]) + (filterCoeff*yList[index-3]) #+ (filterCoeff*yList[index-4])

 #Now go over the data and do short-time variance :) also short-time mean and mode
 window = 5
 lower = 0
 upper = window
 xVariances = []
 yVariances = []
 xMeans = []
 xModes = []
 yMeans = []
 yModes = []
 #Also write a varholder file for pmf-ing later :)
 try:
  os.remove(filename+"varholder.data")
 except FileNotFoundError:
  pass
 writerVars = open(filename+"varholder.data","a")

 while upper < len(xList):
   xVariances.append( statistics.variance(xList[lower:upper]) )
   writerVars.write(str(statistics.variance(xList[lower:upper]))+"\n")
   xMeans.append( statistics.mean( xList[lower:upper]  )  )
   xModes.append( statistics.mode( xList[lower:upper]   )   )
    #yVariances.append( statistics.variance(yList[lower:upper]) )
   lower = lower + window
   upper = upper + window

 lower = 0
 upper = window
 while upper < len(yList):
   #xVariances.append( statistics.variance(xList[lower:upper]) )
   yVariances.append( statistics.variance(yList[lower:upper]) )
   yMeans.append( statistics.mean(  yList[lower:upper]  )   )
   yModes.append( statistics.mode( yList[lower:upper]  )    )
   lower = lower + window
   upper = upper + window

 logger = "log.txt"
 writer = open(logger,"a")
 writer.write( "For data: "+filename+"\n")
 writer.write( "Mode: "+str(statistics.mode(xVariances) )+"\n")
 writer.write( "Mean: "+str(statistics.mean(xVariances))  +"\n")
 writer.write( "Var: "+str(statistics.variance(xVariances))  +"\n\n")

 AccelWindowedMeansX.append(statistics.mean(xMeans))
 AccelWindowedModesX.append(statistics.mean(xModes))
 AccelWindowedMeansY.append(statistics.mean(yMeans))
 AccelWindowedModesY.append(statistics.mean(yModes))

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


#print("Accel X values means from 15 to 60 psi: " + str(AccelMeansX) +"\n" )
print("Accel X values modes from 15 to 60 psi: " + str(AccelModesX) +"\n" )
print("Accel X values variances from 15 to 60 psi: " + str(AccelVarsX) +"\n" )
#print("Accel Y values means from 15 to 60 psi: " + str(AccelMeansY) +"\n" )
#print("Accel Y values modes from 15 to 60 psi: " + str(AccelModesY) +"\n" )
print("Accel Y values variances from 15 to 60 psi: " + str(AccelVarsY) +"\n" )

#print("Normalised results are: \n")
normAccelMeansX = [ e/max(AccelMeansX) for e in AccelMeansX ]
normAccelModesX = [ e/max(AccelModesX) for e in AccelModesX ]
normAccelVarsX = [ e/max(AccelVarsX) for e in AccelVarsX ]
normAccelMeansY = [ e/max(AccelMeansY) for e in AccelMeansY ]
normAccelModesY = [ e/max(AccelModesY) for e in AccelModesY ]
normAccelVarsY = [ e/max(AccelVarsY) for e in AccelVarsY ]

accelMeansXplusY = [sum(t) for t in zip(normAccelMeansX,normAccelMeansY)]
normAccelMeansXplusY = [ b/max(accelMeansXplusY) for b in accelMeansXplusY ]
accelVarsXplusY = [sum(z) for z in zip(normAccelVarsX,normAccelVarsY)]
normAccelVarsXplusY = [c/max(accelVarsXplusY) for c in accelVarsXplusY]
meansPlusVars = [sum(y) for y in zip(normAccelMeansXplusY,normAccelVarsXplusY)]

#print("Normalised Accel X means: "+str(normAccelMeansX) + "\n")
#print("Normalised Accel X modes: "+str(normAccelModesX) + "\n")
print("Normalised Accel X vars: "+str(normAccelVarsX) + "\n")
#print("Normalised Accel Y means: "+str(normAccelMeansY) + "\n")
#print("Normalised Accel Y modes: "+str(normAccelModesY) + "\n")
print("Normalised Accel Y vars: "+str(normAccelVarsY) + "\n")

normWindowedXMeans = [ k/max(AccelWindowedMeansX) for k in AccelWindowedMeansX ]
normWindowedYMeans = [ n/max(AccelWindowedMeansY) for n in AccelWindowedMeansY ]
print("Normalised windowed X means :"+str(AccelWindowedMeansX) )
#print("Normalised windowed Y means :"+str(AccelWindowedMeansY) )

#print("Normalised Accel X+Y means: "+str(normAccelMeansXplusY) + "\n")
#print("Normalised Accel X+Y vars: "+str(normAccelVarsXplusY) + "\n")
#print("Accel means plus vars: "+str(meansPlusVars) + "\n")

filenamesLidar = ["Lidar15psi.data","Lidar20psi.data","Lidar25psi.data","Lidar30psi.data","Lidar35psi.data","Lidar40psi.data",
"Lidar45psi.data","Lidar50psi.data","Lidar55psi.data","Lidar60psi.data"]
LidarMeansX = []
LidarModesX = []
LidarVarsX = []
LidarMeansY = []
LidarModesY = []
LidarVarsY = []
modeLidarWindowedMeans = []
modeLidarWindowedModes = []

for filename in filenamesLidar:
 #filename = sys.argv[1]
 decimalPlaces = int(sys.argv[1])
 doplot = sys.argv[2]
 fileholder = open(filename,"r")
 Lines = fileholder.readlines() 
 varholderdict = dict()
 lidarList = []

 lidarcounter = 0
 for line in Lines:
  lidarcounter += 1
  linevals = line.split(',')
  lidarval = float(linevals[0])
  if lidarval >= 400 and lidarval < 550: # and lidarcounter < limit: # remove outliers and keep within window limit defined earlier for accel
    lidarList.append(lidarval) # x value

 #print("Lidar raw data mean is: "+str(statistics.mean(lidarList)))
 #print( "Lidar raw data min is: "+str(min(lidarList))  )

 #Now do FIR FILTER for Lidar aswell
 #filterSizeLidar = 5
 #filterCoeffLidar = 0.2
 #for index in range(filterSizeLidar,len(lidarList)):
 # lidarList[index] = (filterCoeffLidar*lidarList[index]) + (filterCoeffLidar*lidarList[index-1]) + (filterCoeffLidar*lidarList[index-2]) + (filterCoeffLidar*lidarList[index-3]) + (filterCoeffLidar*lidarList[index-4])

 #print("Lidar FIR'd data mean is: "+str(statistics.mean(lidarList)))
 #print("Lidar FIR'd data min is: "+str( min(lidarList) ))
 #print("Lidar FIR'd data variance is: "+str(statistics.variance(lidarList)) )

 #Now go over the data and do short-time variance :)
 try:
  os.remove(filename+"varholder.data")
 except FileNotFoundError:
  pass
 writerVars = open(filename+"varholder.data","a")


 windowLidar = 10
 lower = 0
 upper = windowLidar
 lidarVariances = [] # list of variances for window size chunks through the file
 lidarMeans = []
 lidarModes = []
 varcounter = 0
 themode = 0.0
 blockcounter = 0
 last10var = []
 while upper < len(lidarList):
   lidarVariances.append( statistics.variance(lidarList[lower:upper]) )
   writerVars.write(str(statistics.variance(lidarList[lower:upper]))+"\n")
   #thevar = statistics.variance(lidarList[lower:upper])
   #last10var.append(thevar)
   #blockcounter += 1
   #varcounter += 1
   #if blockcounter > 10:
   #  themode = statistics.mode(last10var)
   #  last10var = []
   #  varcounter = 0
   #  blockcounter = 0
   #if(themode < 0.0000001):
   # themode = 0.00001
   #writerVars.write( str(themode)+"\n" )
   lidarMeans.append( statistics.mean(lidarList[lower:upper])  )
   lidarModes.append( statistics.mode(lidarList[lower:upper])  )
   #yVariances.append( statistics.variance(yList[lower:upper]) )
   lower = lower + windowLidar
   upper = upper + windowLidar

 #append this file's values to the global variables
 checkforzero = 0
 if(statistics.mode(lidarVariances) < 0.0000001):
    modeLidarVariances.append( 0.00001 )
 else:
  modeLidarVariances.append( statistics.mode(lidarVariances) )
 meanLidarVariances.append( statistics.mean(lidarVariances) ) 
 varLidarVariances.append( statistics.variance(lidarVariances) )
 modeLidarWindowedMeans.append( statistics.variance(lidarMeans) )
 modeLidarWindowedModes.append( statistics.variance(lidarModes) )
#print("And the windowed variances themselves are: "+str(lidarVariances) )

#Now work on the global variables. 
normalisedMeanLidar = [ f / max(meanLidarVariances) for f in meanLidarVariances]
normalisedModeLidar = [h / max(modeLidarVariances) for h in modeLidarVariances]
normalisedVarLidar = [ g / max(varLidarVariances) for g in varLidarVariances ]

print("mode of Lidar variances: "+str(modeLidarVariances)+ "\n")
print("Normalised mean Lidar: "+str(normalisedMeanLidar)+ "\n") 
print("Normalised mode Lidar: "+str(normalisedModeLidar)+ "\n") 
print("Normalised var Lidar: "+str(normalisedVarLidar)+ "\n") 
#print("Variance of Lidar windowed means: "+str( modeLidarWindowedMeans ) + "\n")
#print("Variance of Lidar windowed modes: "+str( modeLidarWindowedModes ) + "\n")

#AccelWindowedMeansX = [i for i in AccelWindowedMeansX if i is not None]
#AccelWindowedMeansY = [i for i in AccelWindowedMeansY if i is not None]
#AccelWindowedModesX = [i for i in AccelWindowedModesX if i is not None]
#AccelWindowedModesX = [i for i in AccelWindowedModesX if i is not None]
#print(AccelWindowedMeansX)
#print( "Variance of accel windowed means x:"+str((AccelWindowedMeansX)) + "\n")
#print( "Variance of accel windowed modes x:"+str((AccelWindowedModesX)) + "\n")
#print( "Variance of accel windowed modes y:"+str((AccelWindowedModesY) ) + "\n")
#print( "Variance of accel windowed means y:"+str((AccelWindowedMeansY)  ) + "\n")

normalisedVarAccelWindowedMeansX = [ j/max(AccelWindowedMeansX) for j in AccelWindowedMeansX ]
normalisedVarAccelWindowedModesX = [ m/max(AccelWindowedModesX) for m in AccelWindowedModesX ]
#print( "Normalised Variance of accel windowed means x:" +str([ j/max(AccelWindowedMeansX) for j in AccelWindowedMeansX ]) + "\n")
#print( "Normalised Variance of accel windowed modes x:" +str([ h/max(AccelWindowedModesX) for h in AccelWindowedModesX ]) + "\n")

combined = [sum(z) for z in zip(normAccelVarsXplusY,normalisedVarAccelWindowedMeansX)]
#print("accel x plus y plus var of windowed means X is: "+str(combined) + "\n")
normVarsXplusNormVarWindowedMeansX = [sum(y) for y in zip(normAccelVarsX,normalisedVarAccelWindowedMeansX)] 
#print("Accel Varianced X plus Var of windowed Means X: "+str(normVarsXplusNormVarWindowedMeansX) )

normVarXplusnormVarLidar = [sum(u) for u in zip(normAccelVarsX,normalisedVarLidar)]
print("SENSOR FUSION AccelXVars and LidarVars: "+str(normVarXplusnormVarLidar))
