logfileNames = ["log1.data","log2.data","log3.data","log4.data","log5.data"] # circular log
lfnIndex = 0 # index for which log file we will write to next
dataList = []

currentReading = 4
programLoop = 0
while programLoop < 7:

  while( len(dataList) < 10000):
    dataList.append(str(currentReading)+'\n')
    currentReading = currentReading+1

  #dataList = map(lambda x:x+'\n', dataList) # append
  f = open( logfileNames[lfnIndex],"a" )
  f.writelines( dataList )
  f.close #automatically flushes too
  dataList[:] = [] #empty current values

  if lfnIndex < (len(logfileNames) - 1):
    lfnIndex = lfnIndex + 1 # increment to next log file for writing to
  else:
    lfnIndex = 0  # if we reached the end of log files, circle round to start again 

  programLoop = programLoop + 1
