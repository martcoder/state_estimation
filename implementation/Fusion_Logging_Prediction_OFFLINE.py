# This code is licensed under the LGPL Lesser GNU Public License
#  https://github.com/martcoder/state_estimation/

#Accelerometer model is MMA8452

#Runas > python3 Fusion_Logging_Prediction_OFFLINE.py AccelDataFileName LidarDataFileName

import time
from datetime import datetime
import os, os.path
import errno
import sys
import copy
import random
import statistics

#define some variables that get used in various functions
global hiddenMax
hiddenMax = 20
global hiddenMin
hiddenMin = 5
global weightMax
weightMax = 2.0

global overall60PSIchances
overall60PSIchances = 0.0
global overall40PSIchances
overall40PSIchances = 0.0
global overall20PSIchances
overall20PSIchances = 0.0

global meanAccelFfannOutput
meanAccelFfannOutput = 0.0

global meanLidarFfannOutput
meanLidarFfannOutput = 0.0

global meanAccel100
meanAccel100 = 0.0

global meanLidar100
meanLidar100 = 0.0

global previous100Accel
previous100Accel = []

global previous100Lidar
previous100Lidar = []

global medianAccelFfannOutput
medianAccelFfannOutput = 0.0
global medianLidarFfannOutput
medianAccelFfannOutput = 0.0


global predictionMapAccel 
predictionMapAccel = dict()
predictionMapAccel[60.0] = 0.0
predictionMapAccel[40.0] = 0.0
predictionMapAccel[20.0] = 0.0
global predictionMapLidar
predictionMapLidar = dict()
predictionMapLidar[60.0] = 0.0
predictionMapLidar[40.0] = 0.0
predictionMapLidar[20.0] = 0.0

global runningTotalCount
runningTotalCount = 0.0
global runningTotalSumAccel
runningTotalSumAccel = 0.0
global runningTotalSumLidar
runningTotalSumLidar = 0.0

global accelModelOutputList
accelModelOutputList = []
global lidarModelOutputList
lidarModelOutputList = []


global currentModelValueAccel
currentModelValueAccel = 0.0

global currentModelValueLidar
currentModelValueLidar = 0.0


#folder creation from: https://gist.github.com/keithweaver/562d3caa8650eefe7f84fa074e9ca949
#==========SETUP LOGGING===============
errorFile = "./errors.log"
folderName = str( datetime.now().time() )
logfileRoot = "./OFFLINEpredictionF"+folderName+"/"
try: #make the logging folder, record error if it doesnt work. 
  if not os.path.exists(logfileRoot):
    os.makedirs(logfileRoot)
except OSError:
    errorF = open( errorFile,"a")
    errorF.write("Error creating logging folder at "+str(datetime.now().time())+'\n')
logfileNames = ["log1.data","log2.data","log3.data","log4.data","log5.data","log6.data","log7.data","log8.data","log9.data","log10.data","log11.data","log12.data","log13.data","log14.data","log15.data","log16.data","log17.data","log18.data","log19.data","log20.data","log21.data","log22.data","log23.data","log24.data","log25.data","log26.data","log27.data","log28.data","log29.data","log30.data","log31.data","log32.data","log33.data","log34.data","log35.data","log36.data","log37.data","log38.data","log39.data","log40.data"] # circular log
predictionFileNames = ["fprdct1.data","fprdct2.data","fprdct3.data","fprdct4.data","fprdct5.data","fprdct6.data","fprdct7.data","fprdct8.data","fprdct9.data","fprdct10.data","fprdct11.data","fprdct12.data","fprdct13.data","fprdct14.data","fprdct15.data","fprdct16.data","fprdct17.data","fprdct18.data","fprdct19.data","fprdct20.data","fprdct21.data","fprdct22.data","fprdct23.data","fprdct24.data","fprdct25.data","fprdct26.data","fprdct27.data","fprdct28.data","fprdct29.data","fprdct30.data","fprdct31.data","fprdct32.data","fprdct33.data","fprdct34.data","fprdct35.data","fprdct36.data","fprdct37.data","fprdct38.data","fprdct39.data","fprdct40.data"]
logfileConcatPredictions = []
logfileConcatNames = []
for i in range(len(logfileNames)):
  logfileConcatNames.append( logfileRoot+logfileNames[i] )
  logfileConcatPredictions.append( logfileRoot+predictionFileNames[i]  )
lfnIndex = 0 # index for which log file we will write to next
#dataList = [] #for storing data values
predictionDataList = [] #for storing prediction data values
#MAX_VOLUME_OF_DATA_PER_FILE = 15 #quite fast like 2 logfiles per minute

#======WRITE DATA TO CIRCULAR LOG FILES==============
def writeDataToFile(filename):
    f = open( filename,"w" )
    f.writelines( dataList )
    f.close() #automatically flushes too
    return True

def writePredictionToFile(filename):
    f = open( filename,"w" )
    f.writelines( predictionDataList )
    f.close() #automatically flushes too
    return True


def writeLog(towrite):
   flog = open(logfileRoot+"log.log")
   flog.write(towrite)
   flog.close()
   return True

# NOW FOR MACHINE-LEARNING MODELS
class Individual:
  def __init__(self,input,hidden,output):
    self.inputLayer = copy.deepcopy(input)
    self.hiddenLayer = copy.deepcopy(hidden)
    self.outputLayer = copy.deepcopy(output)
    self.best = 0

class Node:
  def __init__(self):
    self.input = 0.0
    self.weight = random.uniform(0.0,weightMax) #initialise weight randomly
    self.bias = random.uniform(0.0,weightMax)
    self.weights = []
    self.output = 0.0
    self.lms = 999999999999999.0
    self.meanOutputLOW = 100.0
    self.meanOutputMED = 100.0
    self.meanOutputHIGH = 100.0

#Initialise measuremodel FFANN for acceleration, hence the a in the amm
ammInputLayer = Node()
ammInputLayer.weight = 1.0061789956545186
ammInputLayer.bias = 0.018344856493117234
ammHiddenLayer = []
weights = [1.3008844685982437,0.82557979157225,0.5971036921598851,\
1.6221239464256758,1.658719232929949,1.95881299520407,1.2163583748773723,\
1.4936133155439555,0.21143498938076677,1.9232676153303996,0.4451278281419764]
biases = [0.8671751913958576,1.3255037187755965,0.12085837431132629,\
0.1872091100792339,0.810033632607061,0.36038850435203984,1.1141950114108992,\
0.3051406290308978,0.11362218161265836,0.5142996798131558,0.0886190798847386]
for x in range(11):
  ammHiddenLayer.append(Node())
  ammHiddenLayer[x].weight = weights[x]
  ammHiddenLayer[x].bias = biases[x]
ammOutputLayer = Node()
ammOutputLayer.weights.append(0.2695829597148024)
ammOutputLayer.weights.append(0.04742078471485922)
ammOutputLayer.weights.append(0.14134250243199997)
ammOutputLayer.weights.append(0.16313547427365904)
ammOutputLayer.weights.append(0.2695829597148024)
ammOutputLayer.weights.append(0.21772441106714058)
ammOutputLayer.weights.append(0.255015613773330414)
ammOutputLayer.weights.append(0.3622444874966593)
ammOutputLayer.weights.append(0.21772441106714058)
ammOutputLayer.weights.append(0.21772441106714058)
ammOutputLayer.weights.append(0.21772441106714058)
ammOutputLayer.bias = 0.016236279611958393

AccelmeasurementModel = Individual( ammInputLayer, ammHiddenLayer, ammOutputLayer )

lmmInputLayer = Node()
lmmHiddenLayer = []
lmmOutputLayer = Node()
lmmInputLayer.weight = 0.9262540838770146
lmmInputLayer.bias = 0.010212594599706026 #0.04018407937509605
lweights = []
lweights.append(1.9737394536757076)
lweights.append(0.7210050115250795)
lweights.append(1.8685856098840263)
lweights.append(0.39364612992216874)
lweights.append(1.8502180550015328)
lweights.append(1.9737394536757076)
lweights.append(1.9737394536757076)
lweights.append(1.9737394536757076)
lweights.append(0.7210050115250795)
lweights.append(1.8685856098840263)
lweights.append(0.39364612992216874)
lweights.append(1.8502180550015328)
lweights.append(1.1457428659323026)
lweights.append(1.9737394536757076)

lbiases = []
lbiases.append(0.040413757266005958)
lbiases.append(0.19073090274237336)
lbiases.append(0.4629375430821314)
lbiases.append(0.5092694520336518)
lbiases.append(1.1867358663941552)
lbiases.append(0.04041375726005958)
lbiases.append(0.04041375726005958)
lbiases.append(0.04041375726005958)
lbiases.append(0.19073090274237336)
lbiases.append(0.4629375430821314)
lbiases.append(0.5092694520336518)
lbiases.append(1.1867358663941552)
lbiases.append(0.026007775587584492)
lbiases.append(0.04041375726005958)

for x in range(10):
  lmmHiddenLayer.append(Node())
  lmmHiddenLayer[x].weight = lweights[x]
  lmmHiddenLayer[x].bias = lbiases[x]
lmmOutputLayer.weights = []
lmmOutputLayer.weights.append(0.17560603783383788)
lmmOutputLayer.weights.append(0.5264303902852817)
lmmOutputLayer.weights.append(0.5366098343584506)
lmmOutputLayer.weights.append(0.2391898715091062)
lmmOutputLayer.weights.append(0.3126473384541354)
lmmOutputLayer.weights.append(0.17560603783383788)
lmmOutputLayer.weights.append(0.17560603783383788)
lmmOutputLayer.weights.append(1.4609781643403315)
lmmOutputLayer.weights.append(0.5264303902852817)
lmmOutputLayer.weights.append(0.048015829318969194)
lmmOutputLayer.weights.append(0.23918987150191062)
lmmOutputLayer.weights.append(0.12269093738804715)
lmmOutputLayer.weights.append(0.17560603783383788)
lmmOutputLayer.weights.append(0.17560603783383788)

lmmOutputLayer.bias = 0.03233947380481528
LidarmeasurementModel = Individual( lmmInputLayer, lmmHiddenLayer, lmmOutputLayer )


#Now for the prediction Algorithm.....
#Now for the motion models
state_probability = 0.33333; # 3 possible states, 1/3
motion_model_60psi = dict()
motion_model_60psi[20.0] = 0.05
motion_model_60psi[40.0] = 0.25
motion_model_60psi[60.0] = 0.7

motion_model_40psi = dict()
motion_model_40psi[20.0] = 0.2
motion_model_40psi[40.0] = 0.7
motion_model_40psi[60.0] = 0.1

motion_model_20psi = dict()
motion_model_20psi[20] = 0.7
motion_model_20psi[40] = 0.25
motion_model_20psi[60] = 0.05

# Hard-code the first prediction to get started....
#Now do the first step .... PREDICTION

global predictionMap 
predictionMap = dict()
predictionMap[20.0] = 0.333
predictionMap[40.0] = 0.333
predictionMap[60.0] = 0.333

#ACCEL MEASUREMENT-MODEL PROBABILITIES
def measurementModelProbabilityHIGHaccel(value):
  if value >= 190:
    return 0.05
  if (value >= 180) and (value < 190):
    return 0.25
  if value < 180: 
    return 0.7

def measurementModelProbabilityMEDaccel(value):
  if value >= 190:
    return 0.2
  if (value >= 180) and (value < 190):
    return 0.6
  if value < 180: 
    return 0.2

def measurementModelProbabilityLOWaccel(value):
  if value >= 190:
    return 0.7
  if (value >= 180) and (value < 190):
    return 0.25
  if value < 180: 
    return 0.05

#LIDAR MEASUREMENT-MODEL PROBABILITIES
#based on the best measurement model FFANN that was able to be evolved. 
def measurementModelProbabilityHIGHlidar(value):
  if value < 2760.0:
    return 0.7
  if (value >= 2760) and (value < 2770.0):
    return 0.25
  if value > 2770.0: 
    return 0.05

def measurementModelProbabilityMEDlidar(value):
  if value < 2760.0:
    return 0.2
  if (value >= 2760.0) and (value < 2770.0):
    return 0.6
  if value >= 2770: 
    return 0.2

def measurementModelProbabilityLOWlidar(value):
  if value < 2760.0:
    return 0.05
  if (value >= 2760.0) and (value < 2770.0):
    return 0.25
  if value >= 2770.0: 
    return 0.7

def relu(value):
  return max(0.0,value)

def accelProcessCurrentAccel(currentDataValue): 
  #Process input layer
  global AccessmeasurementModel
  AccelmeasurementModel.inputLayer.output = currentDataValue * AccelmeasurementModel.inputLayer.weight
  AccelmeasurementModel.inputLayer.output += AccelmeasurementModel.inputLayer.bias
  AccelmeasurementModel.inputLayer.output = relu( AccelmeasurementModel.inputLayer.output )

  #Process hidden layer
  for x in AccelmeasurementModel.hiddenLayer:
    x.output = x.weight * AccelmeasurementModel.inputLayer.output
    x.output += x.bias
    x.output = relu(x.output)

  #Process output layer
  AccelmeasurementModel.outputLayer.output = 0.0
  for x in range(len(AccelmeasurementModel.hiddenLayer)):
    AccelmeasurementModel.outputLayer.output += AccelmeasurementModel.hiddenLayer[x].output * AccelmeasurementModel.outputLayer.weights[x]
  AccelmeasurementModel.outputLayer.output += AccelmeasurementModel.outputLayer.bias
  AccelmeasurementModel.outputLayer.output = relu(AccelmeasurementModel.outputLayer.output)

  return AccelmeasurementModel.outputLayer.output

def lidarProcessCurrentLidar(currentDataValue):
  global LidarmeasurementModel 
  #Process input layer
  LidarmeasurementModel.inputLayer.output = currentDataValue * LidarmeasurementModel.inputLayer.weight
  LidarmeasurementModel.inputLayer.output += LidarmeasurementModel.inputLayer.bias
  LidarmeasurementModel.inputLayer.output = relu( LidarmeasurementModel.inputLayer.output )

  #Process hidden layer
  for x in LidarmeasurementModel.hiddenLayer:
    x.output = x.weight * LidarmeasurementModel.inputLayer.output
    x.output += x.bias
    x.output = relu(x.output)
  #Process output layer
  LidarmeasurementModel.outputLayer.output = 0.0
  for x in range(len(LidarmeasurementModel.hiddenLayer)):
    LidarmeasurementModel.outputLayer.output += LidarmeasurementModel.hiddenLayer[x].output * LidarmeasurementModel.outputLayer.weights[x]
  LidarmeasurementModel.outputLayer.output += LidarmeasurementModel.outputLayer.bias
  LidarmeasurementModel.outputLayer.output = relu(LidarmeasurementModel.outputLayer.output)

  return LidarmeasurementModel.outputLayer.output


def prediction():
 global motion_model_60psi
 global motion_model_40psi
 global motion_model_20psi
 global predictionMap #Ensure the existing value can be accessed....
 predictionOfAccelBeing60SuchThatPreviousAccelWas60psi = motion_model_60psi[60.0]  * predictionMap[60.0]
 #print("motion model is "+str(motion_model_60psi[60])+" and predictionMap[60] is "+str(predictionMap[60.0]))

 #print(predictionOfAccelBeing60SuchThatPreviousAccelWas60psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas40psi =  motion_model_60psi[40.0] * predictionMap[40.0]
 #print(predictionOfAccelBeing60SuchThatPreviousAccelWas40psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas20psi = motion_model_60psi[20.0] * predictionMap[20.0]
 #print(predictionOfAccelBeing60SuchThatPreviousAccelWas20psi)

 global overall60PSIchances
 overall60PSIchances = predictionOfAccelBeing60SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas20psi

 #print("In prediction... overall60PSIchancesAccel are"+str(overall60PSIchances)+"\n")

 predictionOfAccelBeing40SuchThatPreviousAccelWas60psi = motion_model_40psi[60.0]  * predictionMap[60.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas40psi = motion_model_40psi[40.0] * predictionMap[40.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas20psi = motion_model_40psi[20.0] * predictionMap[20.0]

 global overall40PSIchances
 overall40PSIchances = predictionOfAccelBeing40SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas20psi

 #print("In prediction... overall40PSIchancesAccel are"+str(overall40PSIchances)+"\n")


 predictionOfAccelBeing20SuchThatPreviousAccelWas60psi = motion_model_20psi[60.0]  * predictionMap[60.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas40psi = motion_model_20psi[40.0] * predictionMap[40.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas20psi = motion_model_20psi[20.0] * predictionMap[20.0]
 
 global overall20PSIchances
 overall20PSIchances = predictionOfAccelBeing20SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas20psi

 #print("In prediction... overall20PSIchancesAccel are"+str(overall20PSIchances)+"\n")
 #END OF PREDICTION FUNCTION

def update(currentAccel,currentLidar):
 #For each possible state do (measurement_model * prediction) / 
 # (sumOf measurement_model * prediction)
 # ...to create a pmf with each state having a probability
 #print("CURRENTLY IN UPDATE")
 #construct numerators
 numeratorsAccel = dict()
 numeratorsLidar = dict()
 global currentModelValueAccel
 currentModelValueAccel = accelProcessCurrentAccel(currentAccel)
 global currentModelValueLidar
 currentModelValueLidar = lidarProcessCurrentLidar(currentLidar)

 global previous100Accel
 global previous100Lidar

 #Fill up previous100Accel
 if len(previous100Accel) < 100:
    previous100Accel.append(currentModelValueAccel)
 else: #Once full, remove earliest and append the latest to keep it size 100
    previous100Accel = previous100Accel[1:100]
    previous100Accel.append(currentModelValueAccel)

 #Fill up previous100Lidar
 if len(previous100Lidar) < 100:
    previous100Lidar.append(currentModelValueLidar)
 else: #Once full, remove earliest and append the latest to keep it size 100
    previous100Lidar = previous100Lidar[1:100]
    previous100Lidar.append(currentModelValueLidar)

 global meanAccel100
 meanAccel100 = statistics.mean( previous100Accel )

 global meanLidar100
 meanLidar100 = statistics.mean( previous100Lidar )

 #currentModelValueLidar = lidarProcessCurrentLidar(currentLidar)

 #print("Current model value accel is "+str(currentModelValueAccel)+"\n")
 #print("Current model value lidar is "+str(currentModelValueLidar)+"\n")

 #global runningTotalSumAccel
 #runningTotalAccel = 0.0
 
 global runningTotalCount
 runningTotalCount += 1.0 # increment count by 1 for each FFANN output value added to the sum
 
 #print("Accel Running count is "+str(runningTotalValAccel)+" and the running sum is "+str()+"\n")

 global runningTotalSumAccel
 #print("Accel equation parts are: currentSum: "+str(runningTotalSumAccel)+", current accel model outut: "+str(currentModelValueAccel)+", and >
 runningTotalSumAccel = runningTotalSumAccel + currentModelValueAccel
 global runningTotalSumLidar
 runningTotalSumLidar = runningTotalSumLidar + currentModelValueLidar

 #print("Accel running total sum plus current output gives new running sum of "+str(runningTotalSumAccel) )
 global meanAccelFfannOutput
 meanAccelFfannOutput =  runningTotalSumAccel  / runningTotalCount
 global meanLidarFfannOutput
 meanLidarFfannOutput = runningTotalSumLidar / runningTotalCount
 #print("Running avg accel ffann output is now "+str(meanAccelFfannOutput)+"\n")
 #global meanLidarFfannOutput
#Get now running total sum for Lidar
 #global runningTotalSumLidar
 #runningTotalSumLidar = runningTotalSumLidar + currentModelValueLidar 
 #meanLidarFfannOutput = runningTotalSumLidar / runningTotalCount
 #print("Running avg lidar ffann output is "+str(meanLidarFfannOutput)+"\n")
 global overall60PSIchances
 global overall40PSIchances
 global overall20PSIchances

 #print("measurement model prob high accel for meanAccelFfannOutput of "+str(meanAccelFfannOutput)+" is "+str(measurementModelProbabilityHIGHa>
 numeratorsAccel[60.0] = overall60PSIchances * measurementModelProbabilityHIGHaccel( meanAccel100 ) # meanAccelFfannOutput  )
 #print("overall60PSIchances is "+str(overall60PSIchances)+"\n")

 #print("AccelmeasurementModel[60psi] for currentAccel value of "+str(currentAccel)+" is:")
 #print(AccelmeasurementModel['60psi'][currentAccel])
 numeratorsAccel[40.0] = overall40PSIchances * measurementModelProbabilityMEDaccel( meanAccel100 ) # meanAccelFfannOutput  )
 numeratorsAccel[20.0] = overall20PSIchances * measurementModelProbabilityLOWaccel( meanAccel100 ) #meanAccelFfannOutput  )

 numeratorsLidar[60.0] = overall60PSIchances * measurementModelProbabilityHIGHlidar( meanLidar100 ) #meanLidarFfannOutput )
 numeratorsLidar[40.0] = overall40PSIchances * measurementModelProbabilityMEDlidar( meanLidar100 ) #meanLidarFfannOutput )
 numeratorsLidar[20.0] = overall20PSIchances * measurementModelProbabilityLOWlidar( meanLidar100 ) #meanLidarFfannOutput )

 #print("overall40PSIchances is "+str(overall40PSIchances)+"\n")
 #print("overall20PSIchances is "+str(overall20PSIchances)+"\n")

 #print("numerator accel 60 for currentAccel mean ffan model output of "+str(meanAccelFfannOutput)+" and a modelprobability of "+str(measureme>
 #print("numerator accel 40 for currentAccel mean ffann model output of "+str(meanAccelFfannOutput)+" and a modelprobability of "+str(measurem>
 #print("numerator accel 20 for currentAccel mean ffann model output of "+str(meanAccelFfannOutput)+" and a modelprobability of "+str(measurem>

 #numeratorsLidar[60.0] = overall60PSIchances * measurementModelProbabilityHIGHlidar( meanLidarFfannOutput )
 #numeratorsLidar[40.0] = overall40PSIchances * measurementModelProbabilityMEDlidar( meanLidarFfannOutput )
 #numeratorsLidar[20.0] = overall20PSIchances * measurementModelProbabilityLOWlidar( meanLidarFfannOutput )
 #print("numerator lidar 60 for current lidar mean ffann output of "+str(meanLidarFfannOutput)+" and a modelprobability of "+str(measurementMo>
 #print("numerator lidar 40 for current lidar mean ffann output of "+str(meanLidarFfannOutput)+" and a modelprobability of "+str(measurementMo>
 #print("numerator lidar 20 for current lidar mean ffann output of "+str(meanLidarFfannOutput)+" and a modelprobabilty of "+str(measurementMod>
 # Now for denominators, the probability of getting this read sensor data value
 denominatorsAccel = dict()
 denominatorsLidar = dict()

 denominatorsAccel[60.0] = overall60PSIchances * measurementModelProbabilityHIGHaccel( meanAccel100 ) #meanAccelFfannOutput  )
 denominatorsAccel[40.0] = overall40PSIchances * measurementModelProbabilityMEDaccel( meanAccel100 ) #meanAccelFfannOutput  )
 denominatorsAccel[20.0] = overall20PSIchances * measurementModelProbabilityLOWaccel( meanAccel100 ) #meanAccelFfannOutput  )

 denominatorsLidar[60.0] = overall60PSIchances * measurementModelProbabilityHIGHlidar( meanLidar100 ) #meanLidarFfannOutput )
 denominatorsLidar[40.0] = overall40PSIchances * measurementModelProbabilityMEDlidar( meanLidar100 ) #meanLidarFfannOutput )
 denominatorsLidar[20.0] = overall20PSIchances * measurementModelProbabilityLOWlidar( meanLidar100 ) #meanLidarFfannOutput )

 #denominatorsLidar[60.0] = overall60PSIchances * measurementModelProbabilityHIGHlidar( meanLidarFfannOutput )
 #denominatorsLidar[40.0] = overall40PSIchances * measurementModelProbabilityMEDlidar( meanLidarFfannOutput )
 #denominatorsLidar[20.0] = overall20PSIchances * measurementModelProbabilityLOWlidar( meanLidarFfannOutput )

 denominatorAccel = denominatorsAccel[60.0] + denominatorsAccel[40.0] + denominatorsAccel[20.0]

 denominatorLidar = denominatorsLidar[60.0] + denominatorsLidar[40.0] + denominatorsLidar[20.0]

 #denominatorLidar = denominatorsLidar[60.0] + denominatorsLidar[40.0] + denominatorsLidar[20.0]

 #print("denominator accel is "+str(denominatorAccel)+", and denom Lidar is "+str(denominatorLidar))

 if denominatorAccel == 0:
   denominatorAccel = 0.000001
 if denominatorLidar == 0:
   denominatorLidar = 0.000001

 #if denominatorLidar == 0:
 #  denominatorLidar = 0.000001

 global predictionMap
 global predictionMapAccel
 global predictionMapLidar
 #global justLidar
 #global justAccel
 #if justLidar:
   #predictionMap[20.0] = (numeratorsLidar[20.0] / denominatorLidar)
   #predictionMap[40.0] = (numeratorsLidar[40.0] / denominatorLidar)
   #predictionMap[60.0] = (numeratorsLidar[60.0] / denominatorLidar)
 
 #predictionMap[20.0] = (numeratorsAccel[20.0] / denominatorAccel)
 #predictionMap[40.0] = (numeratorsAccel[40.0] / denominatorAccel)
 #predictionMap[60.0] = (numeratorsAccel[60.0] / denominatorAccel)
 #else: #Do sensor fusion!!!!!! 

 predictionMapAccel[20.0] = (numeratorsAccel[20.0] / denominatorAccel)
 predictionMapAccel[40.0] = (numeratorsAccel[40.0] / denominatorAccel)
 predictionMapAccel[60.0] = (numeratorsAccel[60.0] / denominatorAccel)

 predictionMapLidar[20.0] = (numeratorsLidar[20.0] / denominatorLidar)
 predictionMapLidar[40.0] = (numeratorsLidar[40.0] / denominatorLidar)
 predictionMapLidar[60.0] = (numeratorsLidar[60.0] / denominatorLidar)


 predictionMap[20.0] = (numeratorsAccel[20.0] / denominatorAccel) + (numeratorsLidar[20.0] / denominatorLidar)
 predictionMap[40.0] = (numeratorsAccel[40.0] / denominatorAccel) + (numeratorsLidar[40.0] / denominatorLidar)
 predictionMap[60.0] = (numeratorsAccel[60.0] / denominatorAccel) + (numeratorsLidar[60.0] / denominatorLidar)



if __name__ == "__main__":
    try:
        #time.sleep(0.5) #FOR DEBUGGING ONLY
        prevX = 0.0
        prevY = 0.0
        prevZ = 0.0
        currentx = 0.0
        currentl = 0.0
        previousLogNameA = ""
        previousLogNameL = ""

        for log in range(1,39):
            #lfnIndex = log
            currentx,currenty,currentz = (500,500,500) #COMMENT OUT WHEN DEBUGGING

            # Loop until max volume of data has been gathered
            #while( len(dataList) < MAX_VOLUME_OF_DATA_PER_FILE ):
            # Loop until next data log files have been written
            time.sleep(1)
            #writeLog("about to open flag file\n")
            LinA = "./AccelLogs/log"+str(log)+".data"
            LinL = "./LidarLogs/Llog"+str(log)+".data"
            print("about to calc OFFLINE predictions for accel log "+LinA+", and lidar log "+LinL)
            '''
            af = 0
            lf = 0
            try:
              af = open( "/home/pi/state_estimation/implementation/AccelFlag.flag" )
              lf = open( "/home/pi/state_estimation/implementation/LidarFlag.flag" )
            except FileNotFoundError:
              errorF = open( errorFile,"a")
              errorF.write("Error reading flag file, not found at "+str(datetime.now().time())+'\n')
              continue #go to next cycle of the while loop

            LinA = af.readline() #Lin should contain name of log file if one has been written
            af.close() # Release the flag file so it can be written to be other scripts
            LinL = lf.readline()
            lf.close()
            if (LinA == "zero") or (LinA == "") or (LinL == 'zero') or (LinL == ''):
               continue  #back to start of loop, https://www.tutorialspoint.com/python/python_loop_control.htm
            else: 
               if (LinA != previousLogNameA) and (LinL != previousLogNameL): #continue if we have new logs to process
                  #print("new logs to process are "+LinA+" , "+LinL)
                  previousLogName = LinA
                  previousLogName = LinL
                  #currentx,currenty,currentz = read_data() # read next sensor value
                  #print("current accel x read data val is "+str(currentx))
                  #currentx = currentx+1
                  #currenty = currenty + 1
                  #currentz = currentz + 1
                  #data has been written to file, so start processing it....
                  AccelData = 0
                  AccelLines = []
                  LidarData = 0
                  LidarLines = []
'''
            try:
                    AccelData = open(LinA) #LinA should contain name of log file if one has been written
                    AccelLines = AccelData.readlines()
                    AccelData.close() # close it so it can be accessed by the logging script...

            except FileNotFoundError:
                    #errorF = open( errorFile,"a")
                    print("Error reading accel data file named "+str(LinA)+" at "+str(datetime.now().time())+'\n')
                    #errorF.close()
                    #continue #go to next cycle of the while loop
            try:
                    LidarData = open(LinL) #LinL should contain name of log file if one has been written
                    LidarLines = LidarData.readlines()
                    LidarData.close() # close it so it can be accessed by the logging script...

            except FileNotFoundError:
                    #errorF = open( errorFile,"a")
                    print("Error reading lidar data file at "+str(datetime.now().time())+'\n')
                    #errorF.close()
                    #continue #go to next cycle of the while loop


            for ind in range(len(AccelLines)):
                     #print("accel index is "+str(ind)+" and length lidar data is "+str(len(LidarLines)))
                     try:
                       currentx = float(AccelLines[ind].split(',')[0])
                     except IndexError:
                       errorF = open( errorFile,"a")
                       #errorF.write("Index Error gone past accel data end at "+str(datetime.now().time())+'\n')
                       pass
                     try:
                       currentl = float(LidarLines[ind].split(',')[0])
                     except IndexError:
                       errorF = open( errorFile,"a")
                       #errorF.write("Index Error gone past lidar data end at "+str(datetime.now().time())+'\n')
                       pass
                     prediction() #First step of the algorithm is based on prior knowledge
                     currentAccel = currentx #if index error occurred, previousl value will be used
                     currentLidar = currentl #if index error occurred, previous value will be used
                     update(currentAccel,currentLidar) #2nd step of algorithm uses sensor data
                  #print("Predictionmap is currently")
                  #print(predictionMap)

                  #Now normalise the prediction map
                     normalisedMap = dict(predictionMap)
                  #Find the max value...
                     maxToFind = 0.0
                     for itm in predictionMap.items():
                       if itm[1] > maxToFind:
                         maxToFind = itm[1]
                  #ensure maxToFind is a value if zero
                  #if maxToFind == 0.0: 
                  # max = 0.000001
                     for kv in normalisedMap.items():
                       normalisedMap[kv[0]] = kv[1]/maxToFind
                     predictionMap = dict(normalisedMap)

                     #print("Predictionmap is currently")
                     #print(predictionMap)
                     #print("\n")
                  # Check values are populated, and check they are not same as previous value (even at rest they change a little)
                     '''if( (currentx != None or currenty != None or currentz != None) and ( (currentx != prevX) and (currenty != prevY) and (currentz != prevZ) )  ):
                      prevX = currentx
                      prevY = currenty
                      prevZ = currentz
                      print("current accel read value is "+str(currentx))
                      dataList.append( str(currentx)+","+str(currenty)+","+str(currentz)+","+str(datetime.now().time())+'\n' ) # append to list of sensor values
                      print("data read is x: "+str(currentx)+", y: "+str(currenty)+", z: "+str(currentz)+'\n'" and list length is "+str(len(dataList)))
                     '''
                     predictionDataList.append( "60 : "+str(predictionMap[60.0])+", 40 : "+str(predictionMap[40.0])+", 20 : "+str(predictionMap[20.0])+", Accel60 : "+str(predictionMapAccel[60.0])+", Accel40 : "+str(predictionMapAccel[40.0])+", Accel20 : "+str(predictionMapAccel[20.0])+", Lidar60 : "+str(predictionMapLidar[60.0])+", Lidar40 : "+str(predictionMapLidar[40.0])+", Lidar20 : "+str(predictionMapLidar[20.0])+", currentmodeloutputAccel : "+str(currentModelValueAccel)+", currentmodeloutputLidar : "+str(currentModelValueLidar)+", currentmeanoutputAccel : "+str(meanAccelFfannOutput)+", currentmeanoutputLidar : "+str(meanLidarFfannOutput)+", meanAccel100 : "+str(meanAccel100)+", meanLidar100 : "+str(meanLidar100)+"\n"  )
                     predictionsWritten = False
            try:
                       predictionsWritten = writePredictionToFile( logfileConcatPredictions[log-1] )
            except FileNotFoundError:
                       #errorF = open( errorFile,"a")
                       print("Error writing to prediction file "+str(logfileConcatPredictions[log-1])+" at "+str(datetime.now().time())+'\n')


            if predictionsWritten: #once predictions have been written to file
                    predictionDataList[:] = [] #empty current values read for next log file entries
                    print("Just wrote predictions for log files with index "+str(log))
            # Set next log file to use in the circular logging
            #if lfnIndex < (len(logfileConcatPredictions) - 1):
            #        lfnIndex = lfnIndex + 1 # increment to next log file for writing to
            #else:
            #        lfnIndex = 0  # if we reached the end of log files, circle round to start again



            #else:
            #     continue #if no new log file, continue looping....
               #print("data collected is \n")
               #print(dataList)
               # Write data to current log file
               #complete = writeDataToFile( logfileConcatNames[lfnIndex] )
               #predictionsWritten = writePredictionToFile( logfileConcatPredictions[lfnIndex] )
               #if complete: # once file is written
               #    dataList[:] = [] #empty current values
               #if predictionsWritten: #once predictions have been written to file
               #    predictionDataList[:] = [] #empty current values read for next log file entries

               # Set next log file to use in the circular logging
               #if lfnIndex < (len(logfileConcatPredictions) - 1):
               #    lfnIndex = lfnIndex + 1 # increment to next log file for writing to
               #else:
               #    lfnIndex = 0  # if we reached the end of log files, circle round to start again

    except KeyboardInterrupt(): # ctrl + c in terminal.
        if link != None:
                link.close()
                print("program interrupted by the user")

