
#!/usr/bin/python3

import sys
#import matplotlib
#import matplotlib.pyplot as plot
import statistics
import random
import copy

global popsize 
popsize = 400
global hiddenMax
hiddenMax = 20
global hiddenMin
hiddenMin = 5
global weightMax
weightMax = 2.0

global justLidar
justLidar = False
global justAccel
justAccel = False

#NB run using python3 simulation.py acceldatafilename lidardatafilename
# e.g. python3 simulation.py Accel45psi.data Lidar45psi.data

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

#accelFFANN = Individual( ammInputLayer, ammHiddenLayer, ammOutputLayer )
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

lmmOutputLayer.bias = 0.03233947380481528 #0.34915196870822807
LidarmeasurementModel = Individual( lmmInputLayer, lmmHiddenLayer, lmmOutputLayer )

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

#do initial prediction just to get started
tempvals = list( motion_model_60psi.values() )
prediction = [x * state_probability for x in tempvals]

#Now for update1 with arbitrary values
tempY1suchthatX1 = 0.5 #LidarmeasurementModel['60psi'][40.0]
tempMult = [x * tempY1suchthatX1 for x in prediction]
update1 = [t*2 for t in tempMult]
print("Update1 with arbitrary values is: "+str(update1))

print("prediction1 is :"+str(prediction))

#Current Accel, and Lidar data values
currentAccel = 500.0;
currentLidar = 500.0;

#Now do the first step .... PREDICTION

global predictionMap 
predictionMap = dict()
predictionMap[20.0] = prediction[0]
predictionMap[40.0] = prediction[1]
predictionMap[60.0] = prediction[2]

print("just about to do prediction and prediction map is currently")
print(predictionMap)

#define some variables that get used in various functions
global overall60PSIchances
overall60PSIchances = 0.0
global overall40PSIchances
overall40PSIchances = 0.0
global overall20PSIchances
overall20PSIchances = 0.0

#global overall60PSIchancesLidar 
#overall60PSIchancesLidar = 0.0
#global overall40PSIchancesLidar 
#overall40PSIchancesLidar = 0.0
#global overall20PSIchancesLidar 
#overall20PSIchancesLidar = 0.0

global meanAccelFfannOutput
meanAccelFfannOutput = 0.0

global meanLidarFfannOutput
meanLidarFfannOutput = 0.0

global predictionMapAccel 
predictionMapAccel = dict()

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
 print("motion model is "+str(motion_model_60psi[60])+" and predictionMap[60] is "+str(predictionMap[60.0]))

 print(predictionOfAccelBeing60SuchThatPreviousAccelWas60psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas40psi =  motion_model_60psi[40.0] * predictionMap[40.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas40psi)
 predictionOfAccelBeing60SuchThatPreviousAccelWas20psi = motion_model_60psi[20.0] * predictionMap[20.0]
 print(predictionOfAccelBeing60SuchThatPreviousAccelWas20psi)

 global overall60PSIchances
 overall60PSIchances = predictionOfAccelBeing60SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing60SuchThatPreviousAccelWas20psi

 print("In prediction... overall60PSIchancesAccel are"+str(overall60PSIchances)+"\n")

 predictionOfAccelBeing40SuchThatPreviousAccelWas60psi = motion_model_40psi[60.0]  * predictionMap[60.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas40psi = motion_model_40psi[40.0] * predictionMap[40.0]
 predictionOfAccelBeing40SuchThatPreviousAccelWas20psi = motion_model_40psi[20.0] * predictionMap[20.0]

 global overall40PSIchances
 overall40PSIchances = predictionOfAccelBeing40SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing40SuchThatPreviousAccelWas20psi

 print("In prediction... overall40PSIchancesAccel are"+str(overall40PSIchances)+"\n")


 predictionOfAccelBeing20SuchThatPreviousAccelWas60psi = motion_model_20psi[60.0]  * predictionMap[60.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas40psi = motion_model_20psi[40.0] * predictionMap[40.0]
 predictionOfAccelBeing20SuchThatPreviousAccelWas20psi = motion_model_20psi[20.0] * predictionMap[20.0]
 
 global overall20PSIchances
 overall20PSIchances = predictionOfAccelBeing20SuchThatPreviousAccelWas60psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas40psi + \
predictionOfAccelBeing20SuchThatPreviousAccelWas20psi

 print("In prediction... overall20PSIchancesAccel are"+str(overall20PSIchances)+"\n")

 #predictionMapAccel = dict()
 #predictionMapAccel[20.0] = overall20PSIchancesAccel
 #predictionMapAccel[40.0] = overall40PSIchancesAccel
 #predictionMapAccel[60.0] = overall60PSIchancesAccel
#Values are based on the best FFANN models that were able to be evolved. 

#ACCEL MEASUREMENT-MODEL PROBABILITIES
def measurementModelProbabilityHIGHaccel(value):
  if value < 5200000.0:
    return 0.05
  if value > 5200000.0 and value < 5400000.0:
    return 0.25
  if value > 5400000.0: 
    return 0.7

def measurementModelProbabilityMEDaccel(value):
  if value < 5200000.0:
    return 0.2
  if value > 5200000 and value < 5400000.0:
    return 0.6
  if value > 5400000: 
    return 0.2

def measurementModelProbabilityLOWaccel(value):
  if value < 5200000:
    return 0.7
  if value > 5200000 and value < 5400000.0:
    return 0.25
  if value > 5400000: 
    return 0.05

#LIDAR MEASUREMENT-MODEL PROBABILITIES
#based on the best measurement model FFANN that was able to be evolved. 
def measurementModelProbabilityHIGHlidar(value):
  if value < 8000000.0:
    return 0.7
  if value > 8000000 and value < 8250000.0:
    return 0.25
  if value > 8250000.0: 
    return 0.05

def measurementModelProbabilityMEDlidar(value):
  if value < 8000000.0:
    return 0.2
  if value > 8000000.0 and value < 8250000.0:
    return 0.6
  if value > 8250000.0: 
    return 0.2

def measurementModelProbabilityLOWlidar(value):
  if value < 8000000.0:
    return 0.05
  if value > 8000000.0 and value < 8250000.0:
    return 0.25
  if value > 8250000: 
    return 0.7

global runningTotalCount
runningTotalCount = 0.0
global runningTotalSumAccel
runningTotalSumAccel = 0.0
global runningTotalSumLidar
runningTotalSumLidar = 0.0


def update(currentAccel,currentLidar):
 #For each possible state do (measurement_model * prediction) / 
 # (sumOf measurement_model * prediction)
 # ...to create a pmf with each state having a probability
 print("CURRENTLY IN UPDATE")
 #construct numerators
 numeratorsAccel = dict()
 numeratorsLidar = dict()
 currentModelValueAccel = accelProcessCurrentAccel(currentAccel)
 currentModelValueLidar = lidarProcessCurrentLidar(currentLidar)

 print("Current model value accel is "+str(currentModelValueAccel)+"\n")
 print("Current model value lidar is "+str(currentModelValueLidar)+"\n")

 #global runningTotalSumAccel
 #runningTotalAccel = 0.0
 
 global runningTotalCount
 runningTotalCount += 1.0 # increment count by 1 for each FFANN output value added to the sum
 
 #print("Accel Running count is "+str(runningTotalValAccel)+" and the running sum is "+str()+"\n")

 global runningTotalSumAccel
 print("Accel equation parts are: currentSum: "+str(runningTotalSumAccel)+", current accel model outut: "+str(currentModelValueAccel)+", and running count is: "+str(runningTotalCount))
 runningTotalSumAccel = runningTotalSumAccel + currentModelValueAccel
 print("Accel running total sum plus current output gives new running sum of "+str(runningTotalSumAccel) )
 global meanAccelFfannOutput
 meanAccelFfannOutput =  runningTotalSumAccel  / runningTotalCount
 print("Running avg accel ffann output is now "+str(meanAccelFfannOutput)+"\n")
 global meanLidarFfannOutput
 #Get now running total sum for Lidar
 global runningTotalSumLidar
 runningTotalSumLidar = runningTotalSumLidar + currentModelValueLidar 
 meanLidarFfannOutput = runningTotalSumLidar / runningTotalCount
 print("Running avg lidar ffann output is "+str(meanLidarFfannOutput)+"\n")
 global overall60PSIchances
 global overall40PSIchances
 global overall20PSIchances

 print("measurement model prob high accel for meanAccelFfannOutput of "+str(meanAccelFfannOutput)+" is "+str(measurementModelProbabilityHIGHaccel( meanAccelFfannOutput  )))
 numeratorsAccel[60.0] = overall60PSIchances * measurementModelProbabilityHIGHaccel( meanAccelFfannOutput  )
 print("overall60PSIchances is "+str(overall60PSIchances)+"\n")

 #print("AccelmeasurementModel[60psi] for currentAccel value of "+str(currentAccel)+" is:")
 #print(AccelmeasurementModel['60psi'][currentAccel])
 numeratorsAccel[40.0] = overall40PSIchances * measurementModelProbabilityMEDaccel( meanAccelFfannOutput  )
 numeratorsAccel[20.0] = overall20PSIchances * measurementModelProbabilityLOWaccel( meanAccelFfannOutput  )
 print("overall40PSIchances is "+str(overall40PSIchances)+"\n")
 print("overall20PSIchances is "+str(overall20PSIchances)+"\n")

 print("numerator accel 60 for currentAccel mean ffan model output of "+str(meanAccelFfannOutput)+" and a modelprobability of "+str(measurementModelProbabilityHIGHaccel( meanAccelFfannOutput ))+" is : "+str(numeratorsAccel[60.0])+"\n")
 print("numerator accel 40 for currentAccel mean ffann model output of "+str(meanAccelFfannOutput)+" and a modelprobability of "+str(measurementModelProbabilityMEDaccel( meanAccelFfannOutput ))+" is : "+str(numeratorsAccel[40.0])+"\n")
 print("numerator accel 20 for currentAccel mean ffann model output of "+str(meanAccelFfannOutput)+" and a modelprobability of "+str(measurementModelProbabilityLOWaccel( meanAccelFfannOutput ))+" is : "+str(numeratorsAccel[20.0])+"\n")

 numeratorsLidar[60.0] = overall60PSIchances * measurementModelProbabilityHIGHlidar( meanLidarFfannOutput )
 numeratorsLidar[40.0] = overall40PSIchances * measurementModelProbabilityMEDlidar( meanLidarFfannOutput )
 numeratorsLidar[20.0] = overall20PSIchances * measurementModelProbabilityLOWlidar( meanLidarFfannOutput )
 print("numerator lidar 60 for current lidar mean ffann output of "+str(meanLidarFfannOutput)+" and a modelprobability of "+str(measurementModelProbabilityHIGHlidar( meanLidarFfannOutput ))+" is : "+str(numeratorsLidar[60.0]))
 print("numerator lidar 40 for current lidar mean ffann output of "+str(meanLidarFfannOutput)+" and a modelprobability of "+str(measurementModelProbabilityMEDlidar( meanLidarFfannOutput ))+" is: "+str(numeratorsLidar[40.0]))
 print("numerator lidar 20 for current lidar mean ffann output of "+str(meanLidarFfannOutput)+" and a modelprobabilty of "+str(measurementModelProbabilityLOWlidar( meanLidarFfannOutput ))+" is: "+str(numeratorsLidar[20.0]))
# Now for denominators, the probability of getting this read sensor data value
 denominatorsAccel = dict()
 denominatorsLidar = dict()

 denominatorsAccel[60.0] = overall60PSIchances * measurementModelProbabilityHIGHaccel( meanAccelFfannOutput  )
 denominatorsAccel[40.0] = overall40PSIchances * measurementModelProbabilityMEDaccel( meanAccelFfannOutput  )
 denominatorsAccel[20.0] = overall20PSIchances * measurementModelProbabilityLOWaccel( meanAccelFfannOutput  )

 denominatorsLidar[60.0] = overall60PSIchances * measurementModelProbabilityHIGHlidar( meanLidarFfannOutput )
 denominatorsLidar[40.0] = overall40PSIchances * measurementModelProbabilityMEDlidar( meanLidarFfannOutput )
 denominatorsLidar[20.0] = overall20PSIchances * measurementModelProbabilityLOWlidar( meanLidarFfannOutput )

 denominatorAccel = denominatorsAccel[60.0] + denominatorsAccel[40.0] + denominatorsAccel[20.0]

 denominatorLidar = denominatorsLidar[60.0] + denominatorsLidar[40.0] + denominatorsLidar[20.0]

 print("denominator accel is "+str(denominatorAccel)+", and denom Lidar is "+str(denominatorLidar))

 if denominatorAccel == 0:
   denominatorAccel = 0.000001
 if denominatorLidar == 0:
   denominatorLidar = 0.000001

 global predictionMap
 global justLidar
 global justAccel
 if justLidar:
   predictionMap[20.0] = (numeratorsLidar[20.0] / denominatorLidar)
   predictionMap[40.0] = (numeratorsLidar[40.0] / denominatorLidar)
   predictionMap[60.0] = (numeratorsLidar[60.0] / denominatorLidar)
 elif justAccel:
   predictionMap[20.0] = (numeratorsAccel[20.0] / denominatorAccel)
   predictionMap[40.0] = (numeratorsAccel[40.0] / denominatorAccel)
   predictionMap[60.0] = (numeratorsAccel[60.0] / denominatorAccel)
 else: #Do sensor fusion!!!!!! 
   predictionMap[20.0] = (numeratorsAccel[20.0] / denominatorAccel) + (numeratorsLidar[20.0] / denominatorLidar)
   predictionMap[40.0] = (numeratorsAccel[40.0] / denominatorAccel) + (numeratorsLidar[40.0] / denominatorLidar)
   predictionMap[60.0] = (numeratorsAccel[60.0] / denominatorAccel) + (numeratorsLidar[60.0] / denominatorLidar)



#THE SCRIPT OPERATES FROM HERE:
#2nd step is preprocessing incoming data e.g. filter, get variance, fit into bucket
#currentAccel = next line of data
#currentLidar = next line of data

print("Please enter whether you want to operate with just Lidar? Y or N > \n")
useJustLidar = input()
if(useJustLidar == "Y"):
  justLidar = True #
  print("Okay, proceeding with predictions using only Lidar data!!!\n")
else:
  justLidar = False
  print("Please enter whether you want to operate with just Accel? Y or N > \n")
  useJustAccel = input()
  if(useJustAccel == "Y"):
    justAccel = True
    print("Okay, proceeding with predictions using only Accelerometer data!!!\n")
  else:
    justAccel = False
    print("Okay, proceeding with Sensor Fusion!!!!!\n")
print("Please press the 'Any' key to continue")
input() #Any key will do...


#Now proceed with the simulation!!! 
print("just about to open a data file")

acceldataname = sys.argv[1]
lidardataname = sys.argv[2]


datafile = open(acceldataname,"r") #open("Accel15psi.data","r")
datafileLidar = open(lidardataname,"r")  #open("Lidar15psi.data","r")
Lines = datafile.readlines() 
LinesLidar = datafileLidar.readlines()
counter = 0
blockcounter = 0
datablockAccel = []
datablockLidar = []
print("just about to iterate over lines")
linecount = -1
FIRlist = []
last10Lidarvar = []
varmode = 0.0
stats = []
#debugCounter = 0
for line in Lines:
 #while debugCounter < 10:
  #debugCounter += 1
  separated = line.split(',')
  valAccel = float(separated[0])
  sepLidar = LinesLidar[linecount].split(',')
  valLidar = float(sepLidar[0])
  if valLidar < 450:
    valLidar = 500.0
  if valLidar > 650:
    valLidar = 500.0
  currentAccel = valAccel
  currentLidar = valLidar
  prediction()
  update(currentAccel,currentLidar)
  print("Predictionmap is currently")
  print(predictionMap)

  #Now normalise the prediction map
  normalisedMap = dict(predictionMap)
  #Find the max value...
  maxToFind = 0
  for x in predictionMap.items():
   if x[1] > maxToFind:
     maxToFind = x[1]
    #ensure max is a value if zero
    #if max == 0: 
    # max = 0.000001
  for kv in normalisedMap.items():
    normalisedMap[kv[0]] = kv[1]/maxToFind
  predictionMap = dict(normalisedMap)
  print("Predictionmap is currently")
  print(predictionMap)

'''
  counter += 1
  linecount += 1
  var = 0.0
  if counter < 5: #each datablock to be considered will have this many values
    separated = line.split(',')
    val = float(separated[0])
    if len(FIRlist) > 3: #once list fills up, need to make space
      FIRlist = FIRlist[1:] # remove first item aka oldest item
      FIRlist.append(val)
    else:
      FIRlist.append(val)
    #FIR Filter
    if linecount > 4: #ensure there are at least 4 previous values
      val = 0.2*FIRlist[0] + 0.2*FIRlist[1] + 0.2*FIRlist[2] + 0.2*FIRlist[3]
    datablockAccel.append(val)
    print("just appended FIR'd value of "+str(val)+" to datablock")
    sepLidar = LinesLidar[linecount].split(',')
    valLidar = float(sepLidar[0])
    if(valLidar > 700):
      valLidar = 475
    datablockLidar.append(valLidar)
  else:
    counter = 0
    blockcounter += 1
    var = statistics.variance(datablockAccel)
    varLidar = statistics.variance(datablockLidar)
    #last10Lidarvar.append(varLidar)
    #if len(last10Lidarvar) > 10:
    # varmode = statistics.mode(last10Lidarvar)
    # varmode = bucket_the_value(varmode)
    # last10Lidarvar = []
    print("lidar var mode is")
    print(varmode)
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
    currentLidar = varLidar #varmode
    prediction()
    update(currentAccel,currentLidar)
    print("Predictionmap is currently")
    print(predictionMap)

    #Now normalise the prediction map
    normalisedMap = dict(predictionMap)
    #Find the max value...
    max = 0
    for x in predictionMap.items():
     if x[1] > max:
      max = x[1]
    #ensure max is a value if zero
    #if max == 0: 
    # max = 0.000001
    for kv in normalisedMap.items():
     normalisedMap[kv[0]] = kv[1]/max
    predictionMap = dict(normalisedMap)
    print("Predictionmap is currently")
    print(predictionMap)
  
    statsMax = 0.0
    chosenPsi = 15.0
    # now keep some stats :) 
    for p in predictionMap.items():
     if p[1] > statsMax:
      statsMax = p[1]
      chosenPsi = p[0]
    print("appending "+str(chosenPsi)+" to stats")
    stats.append(chosenPsi) # keep a record of chosenPSI found each time :)
    
    print("length of stats is "+str(len(stats)))
    if len(stats) > 2:
     print("checking last few of stats: "+str(stats[-1])+" "+str(stats[-2]) )
     maxSoFar = 50.0
     for x in stats:
       if x > maxSoFar:
        maxSoFar = x
     modeSoFar = statistics.mode(stats)
     print("Mode of stats : "+str(modeSoFar))
     meanSoFar = statistics.mean(stats)
     print("Mean of stats : "+str(meanSoFar))
    
    #else:
    # exit()
#3rd step is update
'''


