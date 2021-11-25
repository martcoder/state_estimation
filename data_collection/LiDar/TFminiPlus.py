#!/usr/bin/env python3
# utf-8 encoding 
# kindly donated by https://github.com/ibrahimqazi/TFmini-Plus-LiDAR-interfacing-with-Raspberr-Pi/blob/master/python3_2_tfmini_plus.py
# and then added to by myself

import time
import serial


#==========SETUP LOGGING===============

logfileNames = ["log1.data","log2.data","log3.data","log4.data","log5.data"] # circular log
lfnIndex = 0 # index for which log file we will write to next
dataList = [] #for storing data values
MAX_VOLUME_OF_DATA_PER_FILE = 50000

#=========SETUP SERIAL CONNECTION======
link = serial.Serial(port='/dev/ttyAMA0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
#link = serial.Serial("/dev/ttys0",115200)
# link = serial.Serial("COM12", 115200)
# link = serial.Serial("/dev/ttyUSB1", 115200)

#=====WRITE CONFIG TO SENSOR=======
def writeConfig():
    try:
      #link.write(bytes.fromhex("5A 05 05 01 65")) #cm
      link.write(bytes.fromhex("5A 05 05 06 6A")) #mm
      time.sleep(1)
      #response = link.readline().decode('ascii')
      #print("Response was: "+str(response))

    except Exception:
      print("Got an exception in my attempt to configure the sensor")
      traceback.print_exc()
    link.flush() # flush buffer

#======WRITE DATA TO CIRCULAR LOG FILES==============
def writeDataToFile(filename):
    f = open( filename,"a" )
    f.writelines( dataList )
    f.close #automatically flushes too
    return True



#======READ DATA FROM SENSOR, KEEP LOOPING=============
# we define a new function that will get the data from LiDAR and publish it
def read_data():
        counter = link.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = link.read(9)
            link.reset_input_buffer()

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # these values are specified by manufacturer
                print("Printing python3 portion")            
                distance = bytes_serial[2] + bytes_serial[3]*256 
# multiplied by 256, because the binary data is shifted by 8 to the left (equivalent to "<< 8").                                              
# Dist_L, could simply be added resulting in 16-bit data of Dist_Total.
                strength = bytes_serial[4] + bytes_serial[5]*256
                temperature = bytes_serial[6] + bytes_serial[7]*256
                temperature = (temperature/8) - 256
                if distance != 0:
                    print("Distance: upperByte="+str(bytes_serial[3])+", lowerByte="+str(bytes_serial[2]))
                    print("Distance:"+ str(distance))
                else:
                    print("Distance is too close or far, so got a 0")
                if strength != 0:
                    print("Strength:" + str(strength))
                else:
                    print("Strength is too weak, so got a 0")
                print("Temperature:" + str(temperature))
                link.reset_input_buffer() 
                return distance

if __name__ == "__main__":
    try:
        if link.isOpen() == False:
            link.open()
            link.flushInput()
            link.flushOutput()
        #Configure sensor to use mm rather than cm
        writeConfig()

        while True:
            # Loop until max volume of data has been gathered
            while( len(dataList) < MAX_VOLUME_OF_DATA_PER_FILE ):
               datavalue = read_data() # read next sensor value
               if(datavalue != None):
                   dataList.append( str(datavalue)+'\n' ) # append to list of sensor values
                   print("data value is "+str(datavalue)+" and list length is "+str(len(dataList)))

            # Write data to current log file
            complete = writeDataToFile( logfileNames[lfnIndex]  )
            if complete:
                dataList[:] = [] #empty current values

            # Set next log file to use in the circular logging
            if lfnIndex < (len(logfileNames) - 1):
                lfnIndex = lfnIndex + 1 # increment to next log file for writing to
            else:
                lfnIndex = 0  # if we reached the end of log files, circle round to start again

    except KeyboardInterrupt(): # ctrl + c in terminal.
        if link != None:
                link.close()
                print("program interrupted by the user")

