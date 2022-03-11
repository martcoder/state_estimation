#!/usr/bin/python3

import os
import sys
import matplotlib
import matplotlib.pyplot as plot
import statistics

#format to run is: python3 pmf.py <filename> <decimalplaces> <doPlot? y or n>
filename = sys.argv[1]
filenames = ["Accel15psi.datavarholder.data","Accel20psi.datavarholder.data","Accel25psi.datavarholder.data","Accel30psi.datavarholder.data","Accel35psi.datavarholder.data","Accel40psi.datavarholder.data",
"Accel45psi.datavarholder.data","Accel50psi.datavarholder.data","Accel55psi.datavarholder.data","Accel60psi.datavarholder.data"]
for filename in filenames:
 decimalPlaces = int(sys.argv[2])
 doplot = sys.argv[3]
 varholder = open(filename,"r")
 Lines = varholder.readlines() 
 varholderdict = dict()
 #varholderx15dict[1] = 0.1
 #varholderx15dict[2] = 0.34
 #varholderx15dict[3] = 0.12
 #print(varholderx15dict)
 for line in Lines:
  #print(line)
  val = round(float(line),decimalPlaces)
  try:
   varholderdict[val] = varholderdict[val] + 1
  except KeyError: 
   varholderdict[val] = 1

 sortedVarholderdict = dict(sorted(varholderdict.items(),key= lambda x:x[1]))
 print(sortedVarholderdict)

 #Now write to file as keys in 1st column, values in 2nd column
 try:
  os.remove(filename+"varhistogram.data")
 except FileNotFoundError:
  pass
 writerVars = open(filename+"varhistogram.data","a")
 for x in list(sortedVarholderdict.items()):
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
   plot.stem(list(sortedVarholderdict.keys()),list(sortedVarholderdict.values()))
   plot.show()

