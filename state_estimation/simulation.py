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
     AccelmeasurementModel['60psi'][keyval[0]] = keyval[1]
   if filename == str("Accel55psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['55psi'][keyval[0]] = keyval[1]
   if filename == str("Accel50psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['50psi'][keyval[0]] = keyval[1]
   if filename == str("Accel45psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['45psi'][keyval[0]] = keyval[1]
   if filename == str("Accel40psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['40psi'][keyval[0]] = keyval[1]
   if filename == str("Accel35psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['35psi'][keyval[0]] = keyval[1]
   if filename == str("Accel30psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['30psi'][keyval[0]] = keyval[1]
   if filename == str("Accel25psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['25psi'][keyval[0]] = keyval[1]
   if filename == str("Accel20psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['20psi'][keyval[0]] = keyval[1]
   if filename == str("Accel15psi.datavarholder.datavarhistogram.data"):
     AccelmeasurementModel['15psi'][keyval[0]] = keyval[1]

for filename in filenamesLidar:
 lefile = open(filename,"r")
 Lines = lefile.readlines() 
 for line in Lines: 
   keyval = line.split(',')
   if filename == str("Accel60psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['60psi'][keyval[0]] = keyval[1]
   if filename == str("Accel55psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['55psi'][keyval[0]] = keyval[1]
   if filename == str("Accel50psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['50psi'][keyval[0]] = keyval[1]
   if filename == str("Accel45psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['45psi'][keyval[0]] = keyval[1]
   if filename == str("Accel40psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['40psi'][keyval[0]] = keyval[1]
   if filename == str("Accel35psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['35psi'][keyval[0]] = keyval[1]
   if filename == str("Accel30psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['30psi'][keyval[0]] = keyval[1]
   if filename == str("Accel25psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['25psi'][keyval[0]] = keyval[1]
   if filename == str("Accel20psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['20psi'][keyval[0]] = keyval[1]
   if filename == str("Accel15psi.datavarholder.datavarhistogram.data"):
     LidarmeasurementModel['15psi'][keyval[0]] = keyval[1]

