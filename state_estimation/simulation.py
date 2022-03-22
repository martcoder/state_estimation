
#!/usr/bin/python3

import sys
import matplotlib
import matplotlib.pyplot as plot
import statistics

filenamesAccel = ["Accel15psi.datavarholder.datavarhistogram.data",\
"Accel20psi.datavarholder.datavarhistogram.data",\
"Accel25psi.datavarholder.datavarhistogram.data",\
"Accel30psi.datavarholder.datavarhistogram.data",\
"Accel35psi.datavarholder.datavarhistogram.data",\
"Accel40psi.datavarholder.datavarhistogram.data",\
"Accel45psi.datavarholder.datavarhistogram.data",\
"Accel50psi.datavarholder.datavarhistogram.data",\
"Accel55psi.datavarholder.datavarhistogram.data",\
"Accel60psi.datavarholder.datavarhistogram.data"
]

filenamesLidar = ["Accel15psi.datavarholder.datavarhistogram.data",\
"Accel20psi.datavarholder.datavarhistogram.data",\
"Accel25psi.datavarholder.datavarhistogram.data",\
"Accel30psi.datavarholder.datavarhistogram.data",\
"Accel35psi.datavarholder.datavarhistogram.data",\
"Accel40psi.datavarholder.datavarhistogram.data",\
"Accel45psi.datavarholder.datavarhistogram.data",\
"Accel50psi.datavarholder.datavarhistogram.data",\
"Accel55psi.datavarholder.datavarhistogram.data",\
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
     LidarmeasurementModel['60psi'][round(float(keyval[0]),2)] = float(keyval[1])
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

#print("lidar measurement model for 60psi is")
#print(LidarmeasurementModel['60psi'])
#exit()

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
prediction = [x * state_probability for x in tempvals]

#Now for update1 with arbitrary values
tempY1suchthatX1 = LidarmeasurementModel['60psi'][40.0]
tempMult = [x * tempY1suchthatX1 for x in prediction]
update1 = [t*2 for t in tempMult]
print("Update1 with arbitrary values is: "+str(update1))

print("prediction1 is :"+str(prediction))


#Current Accel, and Lidar data values
currentAccel = 40.0;
currentLidar = 20.0;

#Now do the first step .... PREDICTION

predictionMap = dict()
predictionMap[15.0] = prediction[0]
predictionMap[20.0] = prediction[1]
predictionMap[25.0] = prediction[2]
predictionMap[30.0] = prediction[3]
predictionMap[35.0] = prediction[4]
predictionMap[40.0] = prediction[5]
predictionMap[45.0] = prediction[6]
predictionMap[50.0] = prediction[7] 
predictionMap[55.0] = prediction[8]
predictionMap[60.0] = prediction[9]

print("just about to do prediction and prediction map is currently")
print(predictionMap)


#define some variables that get used in various functions
overall60PSIchancesAccel = 0.0
overall55PSIchancesAccel = 0.0
overall50PSIchancesAccel = 0.0
overall45PSIchancesAccel = 0.0
overall40PSIchancesAccel = 0.0
overall35PSIchancesAccel = 0.0
overall30PSIchancesAccel = 0.0
overall25PSIchancesAccel = 0.0
overall20PSIchancesAccel = 0.0
overall15PSIchancesAccel = 0.0

overall60PSIchancesLidar = 0.0
overall55PSIchancesLidar = 0.0
overall50PSIchancesLidar = 0.0
overall45PSIchancesLidar = 0.0
overall40PSIchancesLidar = 0.0
overall35PSIchancesLidar = 0.0
overall30PSIchancesLidar = 0.0
overall25PSIchancesLidar = 0.0
overall20PSIchancesLidar = 0.0
overall15PSIchancesLidar = 0.0


def bucket_the_value(var):
 if var < 0.05:
      var = 0
 elif (var >= 0.05) and (var < 0.1):
      var = 0.05
 elif (var >= 0.1) and (var < 0.2):
      var = 0.1
 elif (var >= 0.2) and (var < 0.3):
      var = 0.2
 elif (var >= 0.3) and (var < 0.4):
      var = 0.3
 elif (var >= 0.4) and (var < 0.5):
      var = 0.4
 elif (var >= 0.5) and (var < 0.6):
      var = 0.5
 elif (var >= 0.6) and (var < 0.7):
      var = 0.6
 elif (var >= 0.7) and (var < 0.8):
      var = 0.7
 elif (var >= 0.8) and (var < 0.9):
      var = 0.8
 elif (var >= 0.9) and (var < 1.0):
      var = 0.9
 elif (var >= 1.0) and (var <1.5):
      var = 1.0
 elif (var >= 1.5) and (var < 2.0):
      var = 1.5
 elif (var >= 2.0) and (var < 2.5):
      var = 2.0
 elif (var >= 2.5) and (var < 3.0):
      var = 2.5
 elif (var >= 3.0) and (var < 4.0):
      var = 3.0
 elif (var >= 4.0) and (var < 5.0):
      var = 4.0
 elif (var >= 5.0) and (var < 6.0):
      var = 5.0
 elif (var >= 6.0) and (var < 7.0):
      var = 6.0
 elif (var >= 7.0) and (var < 8.0):
      var = 7.0
 elif (var >= 8.0) and (var < 9.0):
      var = 8.0
 elif (var >= 9.0) and (var < 10.0):
      var = 9.0
 elif (var >= 10.0) and (var < 20.0):
      var = 10.0
 elif (var >= 20.0) and (var < 30.0):
      var = 20.0
 elif (var >= 30.0) and (var < 40.0):
      var = 30.0
 elif (var >= 40.0) and (var < 50.0):
      var = 40.0
 elif (var >= 50.0) and (var < 60.0):
      var = 50.0
 elif (var >= 60.0) and (var < 70.0):
      var = 60.0
 elif (var >= 70.0) and (var < 80.0):
      var = 70.0
 elif (var >= 80.0) and (var < 90.0):
      var = 80.0
 elif (var >= 90.0) and (var < 100.0):
      var = 90.0
 elif (var >= 100.0) and (var < 200.0):
      var = 100.0
 elif (var >= 200.0) and (var < 300.0):
      var = 200.0
 elif (var >= 300.0) and (var < 400.0):
      var = 300.0
 elif (var >= 400.0) and (var < 500.0):
      var = 400.0
 elif (var >= 500.0) and (var < 600.0):
      var = 500.0
 elif (var >= 600.0) and (var < 700.0):
      var = 600.0
 elif (var >= 700.0) and (var < 800.0):
      var = 700.0
 elif (var >= 800.0) and (var < 900.0):
      var = 800.0
 elif (var >= 900.0) and (var < 1000.0):
      var = 900.0
 elif (var >= 1000.0) and (var < 1200.0):
      var = 1000.0
 elif (var >= 1200.0) and (var < 1400.0):
      var = 1200.0
 elif (var >= 1400.0) and (var < 1600.0):
      var = 1400.0
 elif (var >= 1600.0) and (var < 1800.0):
      var = 1600.0
 elif (var >= 1800.0) and (var < 2000.0):
      var = 1800.0
 elif (var >= 2000.0) and (var < 2500.0):
      var = 2000.0
 elif (var >= 2500.0) and (var < 3000.0):
      var = 2500.0
 elif (var >= 3000.0) and (var < 3500.0):
      var = 3000.0
 elif (var >= 3500.0):
      var = 3500
 return var

def prediction():
 predictionOfAccelBeing60SuchThatPreviousAccelWas60psi = motion_model_60psi[60]  * predictionMap[60.0]
 print("motion model is "+str(motion_model_60psi[60])+" and predictionMap[60] is "+str(predictionMap[60.0]))

 print(predictionOfAccelBeing60SuchThatPreviousAccelWas60psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas55psi =  motion_model_60psi[55] * predictionMap[55.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas55psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas50psi = motion_model_60psi[50] * predictionMap[50.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas50psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas45psi = motion_model_60psi[45] * predictionMap[45.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas45psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas40psi = motion_model_60psi[40] * predictionMap[40.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas40psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas35psi = motion_model_60psi[35] * predictionMap[35.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas35psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas30psi = motion_model_60psi[30] * predictionMap[30.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas30psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas25psi = motion_model_60psi[25] * predictionMap[25.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas25psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas20psi = motion_model_60psi[20] * predictionMap[20.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas20psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas15psi = motion_model_60psi[15] * predictionMap[15.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas15psi)

 global overall60PSIchancesAccel
 overall60PSIchancesAccel = predictionOfAccelBeing60SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas15psi

 print("overall60PSIchancesAccel are")
 print(overall60PSIchancesAccel)

 predictionOfAccelBeing55SuchThatPreviousAccelWas60psi = motion_model_55psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas55psi =  motion_model_55psi[55] * predictionMap[55.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas50psi = motion_model_55psi[50] * predictionMap[50.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas45psi = motion_model_55psi[45] * predictionMap[45.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas40psi = motion_model_55psi[40] * predictionMap[40.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas35psi = motion_model_55psi[35] * predictionMap[35.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas30psi = motion_model_55psi[30] * predictionMap[30.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas25psi = motion_model_55psi[25] * predictionMap[25.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas20psi = motion_model_55psi[20] * predictionMap[20.0]
 predictionOfAccelBeing55SuchThatPreviousAccelWas15psi = motion_model_55psi[15] * predictionMap[15.0]

 global overall55PSIchancesAccel
 overall55PSIchancesAccel = predictionOfAccelBeing55SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing55SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing50SuchThatPreviousAccelWas60psi = motion_model_50psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas55psi =  motion_model_50psi[55] * predictionMap[55.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas50psi = motion_model_50psi[50] * predictionMap[50.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas45psi = motion_model_50psi[45] * predictionMap[45.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas40psi = motion_model_50psi[40] * predictionMap[40.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas35psi = motion_model_50psi[35] * predictionMap[35.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas30psi = motion_model_50psi[30] * predictionMap[30.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas25psi = motion_model_50psi[25] * predictionMap[25.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas20psi = motion_model_50psi[20] * predictionMap[20.0]
 predictionOfAccelBeing50SuchThatPreviousAccelWas15psi = motion_model_50psi[15] * predictionMap[15.0]

 global overall50PSIchancesAccel
 overall50PSIchancesAccel = predictionOfAccelBeing50SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing50SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing45SuchThatPreviousAccelWas60psi = motion_model_45psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas55psi =  motion_model_45psi[55] * predictionMap[55.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas50psi = motion_model_45psi[50] * predictionMap[50.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas45psi = motion_model_45psi[45] * predictionMap[45.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas40psi = motion_model_45psi[40] * predictionMap[40.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas35psi = motion_model_45psi[35] * predictionMap[35.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas30psi = motion_model_45psi[30] * predictionMap[30.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas25psi = motion_model_45psi[25] * predictionMap[25.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas20psi = motion_model_45psi[20] * predictionMap[20.0]
 predictionOfAccelBeing45SuchThatPreviousAccelWas15psi = motion_model_45psi[15] * predictionMap[15.0]

 global overall45PSIchancesAccel 
 overall45PSIchancesAccel = predictionOfAccelBeing45SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing45SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing40SuchThatPreviousAccelWas60psi = motion_model_40psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas55psi =  motion_model_40psi[55] * predictionMap[55.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas50psi = motion_model_40psi[50] * predictionMap[50.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas45psi = motion_model_40psi[45] * predictionMap[45.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas40psi = motion_model_40psi[40] * predictionMap[40.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas35psi = motion_model_40psi[35] * predictionMap[35.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas30psi = motion_model_40psi[30] * predictionMap[30.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas25psi = motion_model_40psi[25] * predictionMap[25.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas20psi = motion_model_40psi[20] * predictionMap[20.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas15psi = motion_model_40psi[15] * predictionMap[15.0]

 global overall40PSIchancesAccel
 overall40PSIchancesAccel = predictionOfAccelBeing40SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing35SuchThatPreviousAccelWas60psi = motion_model_35psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas55psi =  motion_model_35psi[55] * predictionMap[55.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas50psi = motion_model_35psi[50] * predictionMap[50.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas45psi = motion_model_35psi[45] * predictionMap[45.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas40psi = motion_model_35psi[40] * predictionMap[40.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas35psi = motion_model_35psi[35] * predictionMap[35.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas30psi = motion_model_35psi[30] * predictionMap[30.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas25psi = motion_model_35psi[25] * predictionMap[25.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas20psi = motion_model_35psi[20] * predictionMap[20.0]
 predictionOfAccelBeing35SuchThatPreviousAccelWas15psi = motion_model_35psi[15] * predictionMap[15.0]

 global overall35PSIchancesAccel 
 overall35PSIchancesAccel = predictionOfAccelBeing35SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing35SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing30SuchThatPreviousAccelWas60psi = motion_model_30psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas55psi =  motion_model_30psi[55] * predictionMap[55.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas50psi = motion_model_30psi[50] * predictionMap[50.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas45psi = motion_model_30psi[45] * predictionMap[45.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas40psi = motion_model_30psi[40] * predictionMap[40.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas35psi = motion_model_30psi[35] * predictionMap[35.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas30psi = motion_model_30psi[30] * predictionMap[30.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas25psi = motion_model_30psi[25] * predictionMap[25.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas20psi = motion_model_30psi[20] * predictionMap[20.0]
 predictionOfAccelBeing30SuchThatPreviousAccelWas15psi = motion_model_30psi[15] * predictionMap[15.0]

 global overall30PSIchancesAccel 
 overall30PSIchancesAccel = predictionOfAccelBeing30SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing30SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing25SuchThatPreviousAccelWas60psi = motion_model_25psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas55psi =  motion_model_25psi[55] * predictionMap[55.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas50psi = motion_model_25psi[50] * predictionMap[50.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas45psi = motion_model_25psi[45] * predictionMap[45.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas40psi = motion_model_25psi[40] * predictionMap[40.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas35psi = motion_model_25psi[35] * predictionMap[35.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas30psi = motion_model_25psi[30] * predictionMap[30.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas25psi = motion_model_25psi[25] * predictionMap[25.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas20psi = motion_model_25psi[20] * predictionMap[20.0]
 predictionOfAccelBeing25SuchThatPreviousAccelWas15psi = motion_model_25psi[15] * predictionMap[15.0]

 global overall25PSIchancesAccel 
 overall25PSIchancesAccel = predictionOfAccelBeing25SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing25SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing20SuchThatPreviousAccelWas60psi = motion_model_20psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas55psi =  motion_model_20psi[55] * predictionMap[55.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas50psi = motion_model_20psi[50] * predictionMap[50.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas45psi = motion_model_20psi[45] * predictionMap[45.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas40psi = motion_model_20psi[40] * predictionMap[40.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas35psi = motion_model_20psi[35] * predictionMap[35.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas30psi = motion_model_20psi[30] * predictionMap[30.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas25psi = motion_model_20psi[25] * predictionMap[25.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas20psi = motion_model_20psi[20] * predictionMap[20.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas15psi = motion_model_20psi[15] * predictionMap[15.0]

 global overall20PSIchancesAccel 
 overall20PSIchancesAccel = predictionOfAccelBeing20SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas20psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas15psi

 predictionOfAccelBeing15SuchThatPreviousAccelWas60psi = motion_model_15psi[60]  * predictionMap[60.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas55psi =  motion_model_15psi[55] * predictionMap[55.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas50psi = motion_model_15psi[50] * predictionMap[50.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas45psi = motion_model_15psi[45] * predictionMap[45.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas40psi = motion_model_15psi[40] * predictionMap[40.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas35psi = motion_model_15psi[35] * predictionMap[35.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas30psi = motion_model_15psi[30] * predictionMap[30.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas25psi = motion_model_15psi[25] * predictionMap[25.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas20psi = motion_model_15psi[20] * predictionMap[20.0]
 predictionOfAccelBeing15SuchThatPreviousAccelWas15psi = motion_model_15psi[15] * predictionMap[15.0]

 global overall15PSIchancesAccel 
 overall15PSIchancesAccel = predictionOfAccelBeing15SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing15SuchThatPreviousAccelWas55psi + \
predictionOfAccelBeing15SuchThatPreviousAccelWas50psi + \
predictionOfAccelBeing15SuchThatPreviousAccelWas45psi + \
predictionOfAccelBeing15SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing15SuchThatPreviousAccelWas35psi + \
predictionOfAccelBeing15SuchThatPreviousAccelWas30psi + \
predictionOfAccelBeing15SuchThatPreviousAccelWas25psi + \
predictionOfAccelBeing15SuchThatPreviousAccelWas20psi + \
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


def update(currentAccel,currentLidar):
 #For each possible state do (measurement_model * prediction) / 
 # (sumOf measurement_model * prediction)
 # ...to create a pmf with each state having a probability

 #construct numerators
 numeratorsAccel = dict()
 numeratorsLidar = dict()
 numeratorsAccel[60.0] = overall60PSIchancesAccel * AccelmeasurementModel['60psi'][currentAccel]
 print("overall60PSIchancesAccel is")
 print(overall60PSIchancesAccel)
 print("AccelmeasurementModel[60psi] for currentAccel value of "+str(currentAccel)+" is:")
 print(AccelmeasurementModel['60psi'][currentAccel])
 numeratorsAccel[55.0] = overall55PSIchancesAccel * AccelmeasurementModel['55psi'][currentAccel]
 numeratorsAccel[50.0] = overall50PSIchancesAccel * AccelmeasurementModel['50psi'][currentAccel]
 numeratorsAccel[45.0] = overall45PSIchancesAccel * AccelmeasurementModel['45psi'][currentAccel]
 numeratorsAccel[40.0] = overall40PSIchancesAccel * AccelmeasurementModel['40psi'][currentAccel]
 numeratorsAccel[35.0] = overall35PSIchancesAccel * AccelmeasurementModel['35psi'][currentAccel]
 numeratorsAccel[30.0] = overall30PSIchancesAccel * AccelmeasurementModel['30psi'][currentAccel]
 numeratorsAccel[25.0] = overall25PSIchancesAccel * AccelmeasurementModel['25psi'][currentAccel]
 numeratorsAccel[20.0] = overall20PSIchancesAccel * AccelmeasurementModel['20psi'][currentAccel]
 numeratorsAccel[15.0] = overall15PSIchancesAccel * AccelmeasurementModel['15psi'][currentAccel]
 print("numerator accel 60 for currentAccel var of "+str(currentAccel)+":"+str(numeratorsAccel[60.0]))
 numeratorsLidar[60.0] = overall60PSIchancesLidar * LidarmeasurementModel['60psi'][currentLidar]
 numeratorsLidar[55.0] = overall55PSIchancesLidar * LidarmeasurementModel['55psi'][currentLidar]
 numeratorsLidar[50.0] = overall50PSIchancesLidar * LidarmeasurementModel['50psi'][currentLidar]
 numeratorsLidar[45.0] = overall45PSIchancesLidar * LidarmeasurementModel['45psi'][currentLidar]
 numeratorsLidar[40.0] = overall40PSIchancesLidar * LidarmeasurementModel['40psi'][currentLidar]
 numeratorsLidar[35.0] = overall35PSIchancesLidar * LidarmeasurementModel['35psi'][currentLidar]
 numeratorsLidar[30.0] = overall30PSIchancesLidar * LidarmeasurementModel['30psi'][currentLidar]
 numeratorsLidar[25.0] = overall25PSIchancesLidar * LidarmeasurementModel['25psi'][currentLidar]
 numeratorsLidar[20.0] = overall20PSIchancesLidar * LidarmeasurementModel['20psi'][currentLidar]
 numeratorsLidar[15.0] = overall15PSIchancesLidar * LidarmeasurementModel['15psi'][currentLidar]

# Now for denominators, the probability of getting this read sensor data value
 denominatorsAccel = dict()
 denominatorsLidar = dict()

 denominatorsAccel[60.0] = overall60PSIchancesAccel * AccelmeasurementModel['60psi'][currentAccel]
 denominatorsAccel[55.0] = overall55PSIchancesAccel * AccelmeasurementModel['55psi'][currentAccel]
 denominatorsAccel[50.0] = overall50PSIchancesAccel * AccelmeasurementModel['50psi'][currentAccel]
 denominatorsAccel[45.0] = overall45PSIchancesAccel * AccelmeasurementModel['45psi'][currentAccel]
 denominatorsAccel[40.0] = overall40PSIchancesAccel * AccelmeasurementModel['40psi'][currentAccel]
 denominatorsAccel[35.0] = overall35PSIchancesAccel * AccelmeasurementModel['35psi'][currentAccel]
 denominatorsAccel[30.0] = overall30PSIchancesAccel * AccelmeasurementModel['30psi'][currentAccel]
 denominatorsAccel[25.0] = overall25PSIchancesAccel * AccelmeasurementModel['25psi'][currentAccel]
 denominatorsAccel[20.0] = overall20PSIchancesAccel * AccelmeasurementModel['20psi'][currentAccel]
 denominatorsAccel[15.0] = overall15PSIchancesAccel * AccelmeasurementModel['15psi'][currentAccel]
 denominatorsAccel[60.0] = overall60PSIchancesAccel * AccelmeasurementModel['60psi'][currentAccel]
 denominatorsAccel[55.0] = overall55PSIchancesAccel * AccelmeasurementModel['55psi'][currentAccel]
 denominatorsAccel[50.0] = overall50PSIchancesAccel * AccelmeasurementModel['50psi'][currentAccel]
 denominatorsAccel[45.0] = overall45PSIchancesAccel * AccelmeasurementModel['45psi'][currentAccel]
 denominatorsAccel[40.0] = overall40PSIchancesAccel * AccelmeasurementModel['40psi'][currentAccel]
 denominatorsAccel[35.0] = overall35PSIchancesAccel * AccelmeasurementModel['35psi'][currentAccel]
 denominatorsAccel[30.0] = overall30PSIchancesAccel * AccelmeasurementModel['30psi'][currentAccel]
 denominatorsAccel[25.0] = overall25PSIchancesAccel * AccelmeasurementModel['25psi'][currentAccel]
 denominatorsAccel[20.0] = overall20PSIchancesAccel * AccelmeasurementModel['20psi'][currentAccel]
 denominatorsAccel[15.0] = overall15PSIchancesAccel * AccelmeasurementModel['15psi'][currentAccel]

 denominatorsLidar[60.0] = overall60PSIchancesLidar * LidarmeasurementModel['60psi'][currentLidar]
 denominatorsLidar[55.0] = overall55PSIchancesLidar * LidarmeasurementModel['55psi'][currentLidar]
 denominatorsLidar[50.0] = overall50PSIchancesLidar * LidarmeasurementModel['50psi'][currentLidar]
 denominatorsLidar[45.0] = overall45PSIchancesLidar * LidarmeasurementModel['45psi'][currentLidar]
 denominatorsLidar[40.0] = overall40PSIchancesLidar * LidarmeasurementModel['40psi'][currentLidar]
 denominatorsLidar[35.0] = overall35PSIchancesLidar * LidarmeasurementModel['35psi'][currentLidar]
 denominatorsLidar[30.0] = overall30PSIchancesLidar * LidarmeasurementModel['30psi'][currentLidar]
 denominatorsLidar[25.0] = overall25PSIchancesLidar * LidarmeasurementModel['25psi'][currentLidar]
 denominatorsLidar[20.0] = overall20PSIchancesLidar * LidarmeasurementModel['20psi'][currentLidar]
 denominatorsLidar[15.0] = overall15PSIchancesLidar * LidarmeasurementModel['15psi'][currentLidar]
 denominatorsLidar[60.0] = overall60PSIchancesLidar * LidarmeasurementModel['60psi'][currentLidar]
 denominatorsLidar[55.0] = overall55PSIchancesLidar * LidarmeasurementModel['55psi'][currentLidar]
 denominatorsLidar[50.0] = overall50PSIchancesLidar * LidarmeasurementModel['50psi'][currentLidar]
 denominatorsLidar[45.0] = overall45PSIchancesLidar * LidarmeasurementModel['45psi'][currentLidar]
 denominatorsLidar[40.0] = overall40PSIchancesLidar * LidarmeasurementModel['40psi'][currentLidar]
 denominatorsLidar[35.0] = overall35PSIchancesLidar * LidarmeasurementModel['35psi'][currentLidar]
 denominatorsLidar[30.0] = overall30PSIchancesLidar * LidarmeasurementModel['30psi'][currentLidar]
 denominatorsLidar[25.0] = overall25PSIchancesLidar * LidarmeasurementModel['25psi'][currentLidar]
 denominatorsLidar[20.0] = overall20PSIchancesLidar * LidarmeasurementModel['20psi'][currentLidar]
 denominatorsLidar[15.0] = overall15PSIchancesLidar * LidarmeasurementModel['15psi'][currentLidar]
 denominatorAccel = denominatorsAccel[60.0] + denominatorsAccel[55.0] + denominatorsAccel[50.0] \
   + denominatorsAccel[45.0] + denominatorsAccel[40.0] + denominatorsAccel[35.0] \
   + denominatorsAccel[30.0] + denominatorsAccel[25.0] + denominatorsAccel[20.0] \
   + denominatorsAccel[15.0]

 denominatorLidar = denominatorsLidar[60.0] + denominatorsLidar[55.0] + denominatorsLidar[50.0] \
   + denominatorsLidar[45.0] + denominatorsLidar[40.0] + denominatorsLidar[35.0] \
   + denominatorsLidar[30.0] + denominatorsLidar[25.0] + denominatorsLidar[20.0] \
   + denominatorsLidar[15.0]

 if denominatorAccel == 0:
   denominatorAccel = 0.000001
 if denominatorLidar == 0:
   denominatorLidar = 0.000001
 predictionMap[15.0] = (numeratorsAccel[15.0] / denominatorAccel) + (numeratorsLidar[15.0] / denominatorLidar)
 predictionMap[20.0] = (numeratorsAccel[20.0] / denominatorAccel) + (numeratorsLidar[20.0] / denominatorLidar)
 predictionMap[25.0] = (numeratorsAccel[25.0] / denominatorAccel) + (numeratorsLidar[25.0] / denominatorLidar)
 predictionMap[30.0] = (numeratorsAccel[30.0] / denominatorAccel) + (numeratorsLidar[30.0] / denominatorLidar)
 predictionMap[35.0] = (numeratorsAccel[35.0] / denominatorAccel) + (numeratorsLidar[35.0] / denominatorLidar)
 predictionMap[40.0] = (numeratorsAccel[40.0] / denominatorAccel) + (numeratorsLidar[40.0] / denominatorLidar)
 predictionMap[45.0] = (numeratorsAccel[45.0] / denominatorAccel) + (numeratorsLidar[45.0] / denominatorLidar)
 predictionMap[50.0] = (numeratorsAccel[50.0] / denominatorAccel) + (numeratorsLidar[50.0] / denominatorLidar)
 predictionMap[55.0] = (numeratorsAccel[55.0] / denominatorAccel) + (numeratorsLidar[55.0] / denominatorLidar)
 predictionMap[60.0] = (numeratorsAccel[60.0] / denominatorAccel) + (numeratorsLidar[60.0] / denominatorLidar)

#2nd step is preprocessing incoming data e.g. filter, get variance, fit into bucket
#currentAccel = next line of data
#currentLidar = next line of data

print("just about to open a data file")

#for filename in filenamesLidar:
datafile = open("Accel60psi.data","r")
datafileLidar = open("Lidar60psi.data","r")
Lines = datafile.readlines() 
LinesLidar = datafileLidar.readlines()
counter = 0
datablockAccel = []
datablockLidar = []
print("just about to iterate over lines")
linecount = -1
for line in Lines:
  counter += 1
  linecount += 1
  var = 0.0
  if counter < 10:
    separated = line.split(',')
    val = float(separated[0])
    datablockAccel.append(val)
    print("just appended"+str(val)+" to datablock")

    sepLidar = LinesLidar[linecount].split(',')
    valLidar = float(sepLidar[0])
    if(valLidar > 700):
     valLidar = 475
    datablockLidar.append(valLidar)
  else:
    counter = 0
    var = statistics.variance(datablockAccel)
    varLidar = statistics.variance(datablockLidar)
    print("datablock contains")
    print(datablockAccel)
    datablockAccel = []
    datablockLidar = []
    print("Variance is"+str(var)+" before putting into a bucket")

    #Now put into bucket
    var = bucket_the_value(var)
    varLidar = bucket_the_value(varLidar)
    print("var is now bucketing as "+str(var) )
    print("got to linecount check, linecount is: "+str(linecount))
    #if linecount < 25:
    currentAccel = var #put our current data variance into currentAccel which gets used in update()
    currentLidar = varLidar
    prediction()
    update(currentAccel,currentLidar)
    print("Predictionmap is currently")
    print(predictionMap)
    #else:
    # exit()
#3rd step is update




