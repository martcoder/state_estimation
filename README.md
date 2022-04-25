# state_estimation
State Estimation Project

Multiple sensors provide data
which can be combined using 
sensor fusion using a Bayesian
estimation algorithm based on
a prediction step followed by
an update step. 

The algorithm aims to reduce 
sensor error and tend toward 
the true value. 

Steps required:

- data collection prototyping
  using currently a rPi to 
  receive and log data
  (COMPLETED)

- data analysis to build models
  (completed initially using
  statistics such as variance,
  but in practise was too 
  difficult to differentiate
  between different states. 
  Instead trained artificial
  neural network classifiers
  for Accelerometer data and
  Lidar data and used them 
  as measurement models, now
  COMPLETED)

- run algorithm on data to test
  (now COMPLETED)

- tweaking of the algorithm 
  and data processing analysis
  methods to achieve best result
  (now COMPLETED however results
   were not definitive enough)

- implementation in more suitable
  hardware with realtime display
  of state estimation
  (would like to implement in 
   MSP430 and/or FPGA but ran 
   out of time to do this)
