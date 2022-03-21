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

 overall60PSIchancesAccel = predictionOfAccelBeing60SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing60SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing55SuchThatPreviousAccelWas60psi = motion_model_55psi[60]  * predictionMap[60]
 predictionOfAccelBeing55SuchThatPreviousAccelWas55psi =  motion_model_55psi[55] * predictionMap[55]
 predictionOfAccelBeing55SuchThatPreviousAccelWas50psi = motion_model_55psi[50] * predictionMap[50]
 predictionOfAccelBeing55SuchThatPreviousAccelWas45psi = motion_model_55psi[45] * predictionMap[45]
 predictionOfAccelBeing55SuchThatPreviousAccelWas40psi = motion_model_55psi[40] * predictionMap[40]
 predictionOfAccelBeing55SuchThatPreviousAccelWas35psi = motion_model_55psi[35] * predictionMap[35]
 predictionOfAccelBeing55SuchThatPreviousAccelWas30psi = motion_model_55psi[30] * predictionMap[30]
 predictionOfAccelBeing55SuchThatPreviousAccelWas25psi = motion_model_55psi[25] * predictionMap[25]
 predictionOfAccelBeing55SuchThatPreviousAccelWas20psi = motion_model_55psi[20] * predictionMap[20]
 predictionOfAccelBeing55SuchThatPreviousAccelWas15psi = motion_model_55psi[15] * predictionMap[15]

 overall55PSIchancesAccel = predictionOfAccelBeing55SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing55SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing50SuchThatPreviousAccelWas60psi = motion_model_50psi[60]  * predictionMap[60]
 predictionOfAccelBeing50SuchThatPreviousAccelWas55psi =  motion_model_50psi[55] * predictionMap[55]
 predictionOfAccelBeing50SuchThatPreviousAccelWas50psi = motion_model_50psi[50] * predictionMap[50]
 predictionOfAccelBeing50SuchThatPreviousAccelWas45psi = motion_model_50psi[45] * predictionMap[45]
 predictionOfAccelBeing50SuchThatPreviousAccelWas40psi = motion_model_50psi[40] * predictionMap[40]
 predictionOfAccelBeing50SuchThatPreviousAccelWas35psi = motion_model_50psi[35] * predictionMap[35]
 predictionOfAccelBeing50SuchThatPreviousAccelWas30psi = motion_model_50psi[30] * predictionMap[30]
 predictionOfAccelBeing50SuchThatPreviousAccelWas25psi = motion_model_50psi[25] * predictionMap[25]
 predictionOfAccelBeing50SuchThatPreviousAccelWas20psi = motion_model_50psi[20] * predictionMap[20]
 predictionOfAccelBeing50SuchThatPreviousAccelWas15psi = motion_model_50psi[15] * predictionMap[15]

 overall50PSIchancesAccel = predictionOfAccelBeing50SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing50SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing45SuchThatPreviousAccelWas60psi = motion_model_45psi[60]  * predictionMap[60]
 predictionOfAccelBeing45SuchThatPreviousAccelWas55psi =  motion_model_45psi[55] * predictionMap[55]
 predictionOfAccelBeing45SuchThatPreviousAccelWas50psi = motion_model_45psi[50] * predictionMap[50]
 predictionOfAccelBeing45SuchThatPreviousAccelWas45psi = motion_model_45psi[45] * predictionMap[45]
 predictionOfAccelBeing45SuchThatPreviousAccelWas40psi = motion_model_45psi[40] * predictionMap[40]
 predictionOfAccelBeing45SuchThatPreviousAccelWas35psi = motion_model_45psi[35] * predictionMap[35]
 predictionOfAccelBeing45SuchThatPreviousAccelWas30psi = motion_model_45psi[30] * predictionMap[30]
 predictionOfAccelBeing45SuchThatPreviousAccelWas25psi = motion_model_45psi[25] * predictionMap[25]
 predictionOfAccelBeing45SuchThatPreviousAccelWas20psi = motion_model_45psi[20] * predictionMap[20]
 predictionOfAccelBeing45SuchThatPreviousAccelWas15psi = motion_model_45psi[15] * predictionMap[15]

 overall45PSIchancesAccel = predictionOfAccelBeing45SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing45SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing40SuchThatPreviousAccelWas60psi = motion_model_40psi[60]  * predictionMap[60]
 predictionOfAccelBeing40SuchThatPreviousAccelWas55psi =  motion_model_40psi[55] * predictionMap[55]
 predictionOfAccelBeing40SuchThatPreviousAccelWas50psi = motion_model_40psi[50] * predictionMap[50]
 predictionOfAccelBeing40SuchThatPreviousAccelWas45psi = motion_model_40psi[45] * predictionMap[45]
 predictionOfAccelBeing40SuchThatPreviousAccelWas40psi = motion_model_40psi[40] * predictionMap[40]
 predictionOfAccelBeing40SuchThatPreviousAccelWas35psi = motion_model_40psi[35] * predictionMap[35]
 predictionOfAccelBeing40SuchThatPreviousAccelWas30psi = motion_model_40psi[30] * predictionMap[30]
 predictionOfAccelBeing40SuchThatPreviousAccelWas25psi = motion_model_40psi[25] * predictionMap[25]
 predictionOfAccelBeing40SuchThatPreviousAccelWas20psi = motion_model_40psi[20] * predictionMap[20]
 predictionOfAccelBeing40SuchThatPreviousAccelWas15psi = motion_model_40psi[15] * predictionMap[15]

 overall40PSIchancesAccel = predictionOfAccelBeing40SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing40SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing35SuchThatPreviousAccelWas60psi = motion_model_35psi[60]  * predictionMap[60]
 predictionOfAccelBeing35SuchThatPreviousAccelWas55psi =  motion_model_35psi[55] * predictionMap[55]
 predictionOfAccelBeing35SuchThatPreviousAccelWas50psi = motion_model_35psi[50] * predictionMap[50]
 predictionOfAccelBeing35SuchThatPreviousAccelWas45psi = motion_model_35psi[45] * predictionMap[45]
 predictionOfAccelBeing35SuchThatPreviousAccelWas40psi = motion_model_35psi[40] * predictionMap[40]
 predictionOfAccelBeing35SuchThatPreviousAccelWas35psi = motion_model_35psi[35] * predictionMap[35]
 predictionOfAccelBeing35SuchThatPreviousAccelWas30psi = motion_model_35psi[30] * predictionMap[30]
 predictionOfAccelBeing35SuchThatPreviousAccelWas25psi = motion_model_35psi[25] * predictionMap[25]
 predictionOfAccelBeing35SuchThatPreviousAccelWas20psi = motion_model_35psi[20] * predictionMap[20]
 predictionOfAccelBeing35SuchThatPreviousAccelWas15psi = motion_model_35psi[15] * predictionMap[15]

 overall35PSIchancesAccel = predictionOfAccelBeing35SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing35SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing30SuchThatPreviousAccelWas60psi = motion_model_30psi[60]  * predictionMap[60]
 predictionOfAccelBeing30SuchThatPreviousAccelWas55psi =  motion_model_30psi[55] * predictionMap[55]
 predictionOfAccelBeing35SuchThatPreviousAccelWas50psi = motion_model_30psi[50] * predictionMap[50]
 predictionOfAccelBeing35SuchThatPreviousAccelWas45psi = motion_model_30psi[45] * predictionMap[45]
 predictionOfAccelBeing35SuchThatPreviousAccelWas40psi = motion_model_30psi[40] * predictionMap[40]
 predictionOfAccelBeing35SuchThatPreviousAccelWas35psi = motion_model_30psi[35] * predictionMap[35]
 predictionOfAccelBeing35SuchThatPreviousAccelWas30psi = motion_model_30psi[30] * predictionMap[30]
 predictionOfAccelBeing35SuchThatPreviousAccelWas25psi = motion_model_30psi[25] * predictionMap[25]
 predictionOfAccelBeing35SuchThatPreviousAccelWas20psi = motion_model_30psi[20] * predictionMap[20]
 predictionOfAccelBeing35SuchThatPreviousAccelWas15psi = motion_model_30psi[15] * predictionMap[15]

 overall30PSIchancesAccel = predictionOfAccelBeing30SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing30SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing25SuchThatPreviousAccelWas60psi = motion_model_25psi[60]  * predictionMap[60]
 predictionOfAccelBeing25SuchThatPreviousAccelWas55psi =  motion_model_25psi[55] * predictionMap[55]
 predictionOfAccelBeing25SuchThatPreviousAccelWas50psi = motion_model_25psi[50] * predictionMap[50]
 predictionOfAccelBeing25SuchThatPreviousAccelWas45psi = motion_model_25psi[45] * predictionMap[45]
 predictionOfAccelBeing25SuchThatPreviousAccelWas40psi = motion_model_25psi[40] * predictionMap[40]
 predictionOfAccelBeing25SuchThatPreviousAccelWas35psi = motion_model_25psi[35] * predictionMap[35]
 predictionOfAccelBeing25SuchThatPreviousAccelWas30psi = motion_model_25psi[30] * predictionMap[30]
 predictionOfAccelBeing25SuchThatPreviousAccelWas25psi = motion_model_25psi[25] * predictionMap[25]
 predictionOfAccelBeing25SuchThatPreviousAccelWas20psi = motion_model_25psi[20] * predictionMap[20]
 predictionOfAccelBeing25SuchThatPreviousAccelWas15psi = motion_model_25psi[15] * predictionMap[15]

 overall25PSIchancesAccel = predictionOfAccelBeing25SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing25SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing20SuchThatPreviousAccelWas60psi = motion_model_20psi[60]  * predictionMap[60]
 predictionOfAccelBeing20SuchThatPreviousAccelWas55psi =  motion_model_20psi[55] * predictionMap[55]
 predictionOfAccelBeing20SuchThatPreviousAccelWas50psi = motion_model_20psi[50] * predictionMap[50]
 predictionOfAccelBeing20SuchThatPreviousAccelWas45psi = motion_model_20psi[45] * predictionMap[45]
 predictionOfAccelBeing20SuchThatPreviousAccelWas40psi = motion_model_20psi[40] * predictionMap[40]
 predictionOfAccelBeing20SuchThatPreviousAccelWas35psi = motion_model_20psi[35] * predictionMap[35]
 predictionOfAccelBeing20SuchThatPreviousAccelWas30psi = motion_model_20psi[30] * predictionMap[30]
 predictionOfAccelBeing20SuchThatPreviousAccelWas25psi = motion_model_20psi[25] * predictionMap[25]
 predictionOfAccelBeing20SuchThatPreviousAccelWas20psi = motion_model_20psi[20] * predictionMap[20]
 predictionOfAccelBeing20SuchThatPreviousAccelWas15psi = motion_model_20psi[15] * predictionMap[15]

 overall20PSIchancesAccel = predictionOfAccelBeing20SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing20SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing15SuchThatPreviousAccelWas60psi = motion_model_15psi[60]  * predictionMap[60]
 predictionOfAccelBeing15SuchThatPreviousAccelWas55psi =  motion_model_15psi[55] * predictionMap[55]
 predictionOfAccelBeing15SuchThatPreviousAccelWas50psi = motion_model_15psi[50] * predictionMap[50]
 predictionOfAccelBeing15SuchThatPreviousAccelWas45psi = motion_model_15psi[45] * predictionMap[45]
 predictionOfAccelBeing15SuchThatPreviousAccelWas40psi = motion_model_15psi[40] * predictionMap[40]
 predictionOfAccelBeing15SuchThatPreviousAccelWas35psi = motion_model_15psi[35] * predictionMap[35]
 predictionOfAccelBeing15SuchThatPreviousAccelWas30psi = motion_model_15psi[30] * predictionMap[30]
 predictionOfAccelBeing15SuchThatPreviousAccelWas25psi = motion_model_15psi[25] * predictionMap[25]
 predictionOfAccelBeing15SuchThatPreviousAccelWas20psi = motion_model_15psi[20] * predictionMap[20]
 predictionOfAccelBeing15SuchThatPreviousAccelWas15psi = motion_model_15psi[15] * predictionMap[15]

 overall15PSIchancesAccel = predictionOfAccelBeing15SuchThatPreviousAccelWas60psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas55psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas50psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas45psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas40psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas35psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas30psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas25psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas20psi + 
predictionOfAccelBeing15SuchThatPreviousAccelWas15psi

 predictionMapAccel = dict()
 predictionMapAccel[15.0] = overall15PSIchancesAccel
 predictionMapAccel[20.0] = overall20PSIchancesAccel
 predictionMapAccel[25.0] = overall25PSIchancesAccel
 predictionMapAccel[30.0] = overall30PSIchancesAccel
 predictionMapAccel[35.0] = overall35PSIchancesAccel
 predictionMapAccel[40.0] = overall40PSIchancesAccel
 predictionMapAccel[45.0] = overall45PSIchancesAccel
 predictionMapAccel[50.0] = overall50PSIchancesAccel
 predictionMapAccel[55.0] = overall55PSIchancesAccel
 predictionMapAccel[60.0] = overall60PSIchancesAccel

#2nd step is update
def update():
 
