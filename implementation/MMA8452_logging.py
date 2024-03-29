# Code was kindly donated from:
#  https://github.com/DcubeTechVentures/MMA8452Q/commit/cf1cb4562311f98abb1d376851d6fd6c767178a1
# Changes and additions were added by myself and can be found here: 
#  https://github.com/martcoder/state_estimation/tree/main/data_collection/Accelerometer

import smbus
import time
from datetime import datetime
import os, os.path
import errno
#folder creation from: https://gist.github.com/keithweaver/562d3caa8650eefe7f84fa074e9ca949
#==========SETUP LOGGING===============
errorFile = "/home/pi/state_estimation/implementation/Accelerrors.log"
folderName = str( datetime.now().time() )
logfileRoot = "/home/pi/state_estimation/implementation/Accel"+folderName+"/"
try: #make the logging folder, record error if it doesnt work. 
  if not os.path.exists(logfileRoot):
    os.makedirs(logfileRoot)
except OSError:
    errorF = open( errorFile,"a")
    errorF.write("Error creating logging folder at "+str(datetime.now().time())+'\n')
    errorF.close()
logfileNames = ["log1.data","log2.data","log3.data","log4.data","log5.data","log6.data","log7.data","log8.data","log9.data","log10.data","log11.data","log12.data","log13.data","log14.data","log15.data","log16.data","log17.data","log18.data","log19.data","log20.data","log21.data","log22.data","log23.data","log24.data","log25.data","log26.data","log27.data","log28.data","log29.data","log30.data","log31.data","log32.data","log33.data","log34.data","log35.data","log36.data","log37.data","log38.data","log39.data","log40.data"] # circular log
logfileConcatNames = []
for i in range(len(logfileNames)):
  logfileConcatNames.append( logfileRoot+logfileNames[i] )
lfnIndex = 0 # index for which log file we will write to next
dataList = [] #for storing data values
MAX_VOLUME_OF_DATA_PER_FILE = 2500 #quite fast like 2 logfiles per minute

#======WRITE DATA TO CIRCULAR LOG FILES==============
def writeDataToFile(filename):
    f = open( filename,"w" )
    f.writelines( dataList )
    f.close #automatically flushes too
    return True

#====WRITE FLAG FILE WITH LATEST LOGFILE NAME====
def writeFlag(filename):
   ff = open( "/home/pi/state_estimation/implementation/AccelFlag.flag","w" ) # overwrite each time
   ff.write( filename ) 
   ff.close()
   return True 


#======GET I2C  BUS==============
bus = smbus.SMBus(1)


# ==========NOTES ON CONTROL REGISTER===============
# MMA8452Q address, 0x1C(28) ... can also be 1D as it was for me
# Select Control register, 0x2A(42)
#		0x00(00)	StandBy mode
#bit 7           6            5       4     3     2              1         0
#   ASLP_RATE1   ASLP_RATE0   DR2     DR1   DR0   LNOISE         F_READ    ACTIVE
#my choices would be:
#    12.5 Hz                  100 Hz              reduced noise  normal    active mode
#    0           1            0       1      1    1              0         1   
#therefore the control register byte will be 0 1 0 1 1 1 0 1 which is 0x5D


#=====INITIALISE AND CONFIGURE SENSOR=========
def initialise_configure_sensor():

 # -----ZERO THE CONTROL REGISTER FIRST-----

 # interesting, they're zeroing it first, also they had addr 0x1C 
 # but when  i run i2cdetect -y 1 i shows as 1D

 bus.write_byte_data(0x1D, 0x2A, 0x00) 

 # MMA8452Q address, 0x1C(28) ... can also be 1D as it was for me
 # Select Control register, 0x2A(42)
 #		0x01(01)	Active mode


 #-----NOW WRITE the CTRL_REG1-------

 bus.write_byte_data(0x1D, 0x2A, 0x5D) #it was 0x01 before, basically defaults. 


 #-----NOW WRITE the CONFIG REG------
 
 # MMA8452Q address, 0x1C(28) ... can also be 1D as it was for me
 # Select Configuration register, 0x0E(14)
 #		0x00(00)	Set range to +/- 2g
 bus.write_byte_data(0x1D, 0x0E, 0x00)


def read_data():

 # MMA8452Q address, 0x1C(28)
 # Read data back from 0x00(0), 7 bytes
 # Status register, X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB
 # changed 1C to 1D after reading datasheet and running i2cdetect -y 1
 data = bus.read_i2c_block_data(0x1D, 0x00, 7) 

 # Convert the data
 xAccl = (data[1] * 256 + data[2]) / 16
 if xAccl > 2047 :
  xAccl -= 4096

 yAccl = (data[3] * 256 + data[4]) / 16
 if yAccl > 2047 :
  yAccl -= 4096

 zAccl = (data[5] * 256 + data[6]) / 16
 if zAccl > 2047 :
  zAccl -= 4096

 return xAccl, yAccl, zAccl


 # Output data to screen
 print("Acceleration in X-Axis : "+str(xAccl))
 print("Acceleration in Y-Axis : " +str(yAccl))
 print("Acceleration in Z-Axis : " +str(zAccl))
 print("=========================\n")

if __name__ == "__main__":
    try:
        initialise_configure_sensor() #COMMENT OUT WHEN DEBUGGING
        time.sleep(0.5)
        prevX = 0
        prevY = 0
        prevZ = 0
        writeFlag("zero") # start with zero in the flag file
        #x,y,z = (1,1,1)  #FOR DEBUGGING
        while True:
            # Loop until max volume of data has been gathered
            while( len(dataList) < MAX_VOLUME_OF_DATA_PER_FILE ):
               x,y,z = read_data() # read next sensor value, COMMENT OUT WHEN DEBUGGING
               #x = x + 1   #FOR DEBUGGING
               #y = y + 1   #FOR DEBUGGING
               #z = z + 1   #FOR DEBUGGING
               # Check values are populated, and check they are not same as previous value (even at rest they change a little)
               if( (x != None or y != None or z != None) and ( (x != prevX) and (y != prevY) and (z != prevZ) )  ):
                   prevX = x
                   prevY = y
                   prevZ = z
                   dataList.append( str(x)+","+str(y)+","+str(z)+","+str(datetime.now().time())+'\n' ) # append to list of sensor values
                   #print("data read is x: "+str(x)+", y: "+str(y)+", z: "+str(z)+'\n'" and list length is "+str(len(dataList)))

            # Write data to current log file
            complete = writeDataToFile( logfileConcatNames[lfnIndex] )
            if complete: # once file is written
                dataList[:] = [] #empty current values
                #print("log file name (from index "+str(lfnIndex)+") to write is "+str(logfileConcatNames[lfnIndex]) )
                written = writeFlag( logfileConcatNames[lfnIndex] ) # write lastest log file name to flag file... 
                errorF = open( errorFile,"a")
                errorF.write("Just wrote "+str(logfileConcatNames[lfnIndex])+" with result "+str(written)+" to flag file at "+str(datetime.now().time())+'\n')
                errorF.close()

            #time.sleep(20) #FOR DEBUGGING ONLY
            # Set next log file to use in the circular logging
            if lfnIndex < (len(logfileConcatNames) - 1):
                lfnIndex = lfnIndex + 1 # increment to next log file for writing to
            else:
                lfnIndex = 0  # if we reached the end of log files, circle round to start again

    except KeyboardInterrupt(): # ctrl + c in terminal.
        if link != None:
                link.close()
                #print("program interrupted by the user")

