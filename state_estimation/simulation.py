#!/usr/bin/python3

import sys
import matplotlib
import matplotlib.pyplot as plot
import statistics

filenamesAccel = ["Accel15psi.datavarholder.datavarhistogram.data",
"Accel20psi.datavarholder.datavarhistogram.data",
"Accel25psi.datavarholder.datavarhistogram.data",
"Accel30psi.datavarholder.datavarhistogram.data",
"Accel35psi.datavarholder.datavarhistogram.data",
"Accel40psi.datavarholder.datavarhistogram.data",
"Accel45psi.datavarholder.datavarhistogram.data",
"Accel50psi.datavarholder.datavarhistogram.data",
"Accel55psi.datavarholder.datavarhistogram.data",
"Accel60psi.datavarholder.datavarhistogram.data"
]

filenamesLidar = ["Accel15psi.datavarholder.datavarhistogram.data",
"Accel20psi.datavarholder.datavarhistogram.data",
"Accel25psi.datavarholder.datavarhistogram.data",
"Accel30psi.datavarholder.datavarhistogram.data",
"Accel35psi.datavarholder.datavarhistogram.data",
"Accel40psi.datavarholder.datavarhistogram.data",
"Accel45psi.datavarholder.datavarhistogram.data",
"Accel50psi.datavarholder.datavarhistogram.data",
"Accel55psi.datavarholder.datavarhistogram.data",
"Accel60psi.datavarholder.datavarhistogram.data"]

#Initialise measuremodel data structure keys
AccelmeasurementModel = dict()
AccelmeasurementModel['60psi'] =  dict()
AccelmeasurementModel['55psi'] =  dict()
AccelmeasurementModel['50psi'] =  dict()
AccelmeasurementModel['45psi'] =  dict()
AccelmeasurementModel['40psi'] =  dict()
AccelmeasurementModel['35psi'] =  dict()
AccelmeasurementModel['30psi'] =  dict()
AccelmeasurementModel['25psi'] =  dict()
AccelmeasurementModel['20psi'] =  dict()
AccelmeasurementModel['15psi'] =  dict()

LidarmeasurementModel = dict()
LidarmeasurementModel['60psi'] = dict()
LidarmeasurementModel['55psi'] =  dict()
LidarmeasurementModel['50psi'] =  dict()
LidarmeasurementModel['45psi'] =  dict()
LidarmeasurementModel['40psi'] =  dict()
LidarmeasurementModel['35psi'] =  dict()
LidarmeasurementModel['30psi'] =  dict()
LidarmeasurementModel['25psi'] =  dict()
LidarmeasurementModel['20psi'] =  dict()
LidarmeasurementModel['15psi'] =  dict()

#Populate measurement model data structure values
for filename in filenamesAccel:
 lefile = open(filename,"r")
 Lines = lefile.readlines() 
 for line in Lines: 
   keyval = line.split(',')
   if filename == str("Accel60psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['60psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel55psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['55psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel50psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['50psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel45psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['45psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel40psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['40psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel35psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['35psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel30psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['30psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel25psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['25psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel20psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['20psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel15psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['15psi'][round(float(keyval[0]),2)] = float(keyval[1])

for filename in filenamesLidar:
 lefile = open(filename,"r")
 Lines = lefile.readlines() 
 for line in Lines: 
   keyval = line.split(',')
   if filename == str("Accel60psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['60psi'][round(float(keyval[0]))] = float(keyval[1])
   if filename == str("Accel55psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['55psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel50psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['50psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel45psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['45psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel40psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['40psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel35psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['35psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel30psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['30psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel25psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['25psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel20psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['20psi'][round(float(keyval[0]),2)] = float(keyval[1])
   if filename == str("Accel15psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['15psi'][round(float(keyval[0]),2)] = float(keyval[1])

#Now for the motion models
state_probability = 0.1; # 10 possible states, 1/10
motion_model_60psi = dict()
motion_model_60psi[15] = 0.005
motion_model_60psi[20] = 0.005
motion_model_60psi[25] = 0.01
motion_model_60psi[30] = 0.02
motion_model_60psi[35] = 0.02
motion_model_60psi[40] = 0.02
motion_model_60psi[45] = 0.02
motion_model_60psi[50] = 0.2
motion_model_60psi[55] = 0.3
motion_model_60psi[60] = 0.4

motion_model_55psi = dict()
motion_model_55psi[15] = 0.005
motion_model_55psi[20] = 0.005
motion_model_55psi[25] = 0.01
motion_model_55psi[30] = 0.02
motion_model_55psi[35] = 0.02
motion_model_55psi[40] = 0.02
motion_model_55psi[45] = 0.02
motion_model_55psi[50] = 0.3
motion_model_55psi[55] = 0.5
motion_model_55psi[60] = 0.1

motion_model_50psi = dict()
motion_model_50psi[15] = 0.005
motion_model_50psi[20] = 0.005
motion_model_50psi[25] = 0.02
motion_model_50psi[30] = 0.02
motion_model_50psi[35] = 0.02
motion_model_50psi[40] = 0.02
motion_model_50psi[45] = 0.3
motion_model_50psi[50] = 0.5
motion_model_50psi[55] = 0.1
motion_model_50psi[60] = 0.01

motion_model_45psi = dict()
motion_model_45psi[15] = 0.01
motion_model_45psi[20] = 0.02
motion_model_45psi[25] = 0.02
motion_model_45psi[30] = 0.02
motion_model_45psi[35] = 0.02
motion_model_45psi[40] = 0.3
motion_model_45psi[45] = 0.4
motion_model_45psi[50] = 0.2
motion_model_45psi[55] = 0.005
motion_model_45psi[60] = 0.005

motion_model_40psi = dict()
motion_model_40psi[15] = 0.01
motion_model_40psi[20] = 0.02
motion_model_40psi[25] = 0.02
motion_model_40psi[30] = 0.02
motion_model_40psi[35] = 0.3
motion_model_40psi[40] = 0.3
motion_model_40psi[45] = 0.3
motion_model_40psi[50] = 0.02
motion_model_40psi[55] = 0.005
motion_model_40psi[60] = 0.005

motion_model_35psi = dict()
motion_model_35psi[15] = 0.01
motion_model_35psi[20] = 0.02
motion_model_35psi[25] = 0.02
motion_model_35psi[30] = 0.3
motion_model_35psi[35] = 0.5
motion_model_35psi[40] = 0.1
motion_model_35psi[45] = 0.02
motion_model_35psi[50] = 0.02
motion_model_35psi[55] = 0.005
motion_model_35psi[60] = 0.005

motion_model_30psi = dict()
motion_model_30psi[15] = 0.01
motion_model_30psi[20] = 0.02
motion_model_30psi[25] = 0.1
motion_model_30psi[30] = 0.3
motion_model_30psi[35] = 0.5
motion_model_30psi[40] = 0.02
motion_model_30psi[45] = 0.02
motion_model_30psi[50] = 0.02
motion_model_30psi[55] = 0.005
motion_model_30psi[60] = 0.005

motion_model_25psi = dict()
motion_model_25psi[15] = 0.02
motion_model_25psi[20] = 0.3
motion_model_25psi[25] = 0.5
motion_model_25psi[30] = 0.1
motion_model_25psi[35] = 0.02
motion_model_25psi[40] = 0.02
motion_model_25psi[45] = 0.02
motion_model_25psi[50] = 0.01
motion_model_25psi[55] = 0.005
motion_model_25psi[60] = 0.005

motion_model_20psi = dict()
motion_model_20psi[15] = 0.3
motion_model_20psi[20] = 0.5
motion_model_20psi[25] = 0.1
motion_model_20psi[30] = 0.02
motion_model_20psi[35] = 0.02
motion_model_20psi[40] = 0.02
motion_model_20psi[45] = 0.02
motion_model_20psi[50] = 0.01
motion_model_20psi[55] = 0.005
motion_model_20psi[60] = 0.005

motion_model_15psi = dict()
motion_model_15psi[15] = 0.3
motion_model_15psi[20] = 0.3
motion_model_15psi[25] = 0.3
motion_model_15psi[30] = 0.02
motion_model_15psi[35] = 0.02
motion_model_15psi[40] = 0.02
motion_model_15psi[45] = 0.02
motion_model_15psi[50] = 0.01
motion_model_15psi[55] = 0.005
motion_model_15psi[60] = 0.005

#do initial prediction just to get started
tempvals = list( motion_model_60psi.values() )
prediction1 = [x * state_probability for x in tempvals]

#Now for update1 with arbitrary values
tempY1suchthatX1 = LidarmeasurementModel['60psi'][40.0]
tempMult = [x * tempY1suchthatX1 for x in prediction1]
update1 = [t*2 for t in tempMult]
print("Update1 with arbitrary values is: "+str(update1))

print("prediction1 is :"+str(prediction1))

#Now do the first step .... PREDICTION
def prediction():
 #60 psi
 predictionMap = dict()
 predictionMap[15] = prediction1[0]
 predictionMap[20] = prediction[1]
 predictionMap[25] = prediction[2]
 predictionMap[30] = prediction[3]
 predictionMap[35] = prediction[4]
 predictionMap[40] = prediction[5]
 predictionMap[45] = prediction[6]
 predictionMap[50] = prediction[7] 
 predictionMap[55] = prediction[8]
 predictionMap[60] = prediction[9]

 predictionOfAccelBeing60SuchThatPreviousAccelWas60psi = motion_model_60psi[60]  * predictionMap[60]
 predictionOfAccelBeing60SuchThatPreviousAccelWas55psi =  motion_model_60psi[55] * predictionMap[55]
 predictionOfAccelBeing60SuchThatPreviousAccelWas50psi = motion_model_60psi[50] * predictionMap[50]
 predictionOfAccelBeing60SuchThatPreviousAccelWas45psi = motion_model_60psi[45] * predictionMap[45]
 predictionOfAccelBeing60SuchThatPreviousAccelWas40psi = motion_model_60psi[40] * predictionMap[40]
 predictionOfAccelBeing60SuchThatPreviousAccelWas35psi = motion_model_60psi[35] * predictionMap[35]
 predictionOfAccelBeing60SuchThatPreviousAccelWas30psi = motion_model_60psi[30] * predictionMap[30]
 predictionOfAccelBeing60SuchThatPreviousAccelWas25psi = motion_model_60psi[25] * predictionMap[25]
 predictionOfAccelBeing60SuchThatPreviousAccelWas20psi = motion_model_60psi[20] * predictionMap[20]
 predictionOfAccelBeing60SuchThatPreviousAccelWas15psi = motion_model_60psi[15] * predictionMap[15]

 overall60PSIchances = predictionOfAccelBeing60SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas15psi









