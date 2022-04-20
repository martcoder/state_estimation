%SO FAR ALL I HAVE IS LIDAR RUNNING OKAY FOR ALL DATA
% I HAVE ACCEL DATA SAVED AND ABLE TO LOAD FROM STORAGE, BUT 
%... NOW NEED TO PROCESS ACCEL DATA IN REST OF SCRIPT TOO. 

clear; clc;

%Load data from storage
%dataLidar = load('Lidardata.mat')
load('LidarDataValues.mat')
Lidar60data = Lidar60psi_values(1:52000);
Lidar55data = Lidar55psi_values(1:52000);
Lidar50data = Lidar50psi_values(1:52000);
Lidar45data = Lidar45psi_values(1:52000);
Lidar40data = Lidar40psi_values(1:52000);
Lidar35data = Lidar35psi_values(1:52000);
Lidar30data = Lidar30psi_values(1:52000);
Lidar25data = Lidar25psi_values(1:52000);
Lidar20data = Lidar20psi_values(1:52000);
Lidar15data = Lidar15psi_values(1:52000);

%dataAccel = load('Acceldata.mat')
load('AccelDataXvals.mat')
load('AccelDataYvals.mat')
load('AccelDataZvals.mat')
Accel60data = dataAccel.Accel60data(1:45500)
Accel55data = dataAccel.Accel55data(1:45500)
Accel50data = dataAccel.Accel50data(1:45500)
Accel45data = dataAccel.Accel45data(1:45500)
Accel40data = dataAccel.Accel40data(1:45500)
Accel35data = dataAccel.Accel35data(1:45500)
Accel30data = dataAccel.Accel30data(1:45500)
Accel25data = dataAccel.Accel25data(1:45500)
Accel20data = dataAccel.Accel20data(1:45500)
Accel15data = dataAccel.Accel15data(1:45500)


%Cutoff data at 25000 in order to only keep the uphill part of the route...
% for more consistency in data....
Accel15psi_xValues = Accel15psi_xValues(1:25500);
Accel20psi_xValues = Accel20psi_xValues(1:25500);
Accel25psi_xValues = Accel25psi_xValues(1:25500);
Accel30psi_xValues = Accel30psi_xValues(1:25500);
Accel35psi_xValues = Accel35psi_xValues(1:25500);
Accel40psi_xValues = Accel40psi_xValues(1:25500);
Accel45psi_xValues = Accel45psi_xValues(1:25500);
Accel50psi_xValues = Accel50psi_xValues(1:25500);
Accel55psi_xValues = Accel55psi_xValues(1:25500);
Accel60psi_xValues = Accel60psi_xValues(1:25500);

Accel15psi_yValues = Accel15psi_yValues(1:25500);
Accel20psi_yValues = Accel20psi_yValues(1:25500);
Accel25psi_yValues = Accel25psi_yValues(1:25500);
Accel30psi_yValues = Accel30psi_yValues(1:25500);
Accel35psi_yValues = Accel35psi_yValues(1:25500);
Accel40psi_yValues = Accel40psi_yValues(1:25500);
Accel45psi_yValues = Accel45psi_yValues(1:25500);
Accel50psi_yValues = Accel50psi_yValues(1:25500);
Accel55psi_yValues = Accel55psi_yValues(1:25500);
Accel60psi_yValues = Accel60psi_yValues(1:25500);

Accel15psi_zValues = Accel15psi_zValues(1:25500);
Accel20psi_zValues = Accel20psi_zValues(1:25500);
Accel25psi_zValues = Accel25psi_zValues(1:25500);
Accel30psi_zValues = Accel30psi_zValues(1:25500);
Accel35psi_zValues = Accel35psi_zValues(1:25500);
Accel40psi_zValues = Accel40psi_zValues(1:25500);
Accel45psi_zValues = Accel45psi_zValues(1:25500);
Accel50psi_zValues = Accel50psi_zValues(1:25500);
Accel55psi_zValues = Accel55psi_zValues(1:25500);
Accel60psi_zValues = Accel60psi_zValues(1:25500);

% First to get the measurement models...



%PSI 60 psi 
lidarData60PSI = Lidar60data%[5,4,5,4,5,3,1,3,4,5,5,4,5,5,2,1,2,3,5,4,5,5,4,4,5]
lidarData60PSI_pdf_Keys = unique(lidarData60PSI)
lidarData60PSI_pdf_Values = histc( lidarData60PSI,unique(lidarData60PSI) )
lidarData60PSI_normalised_pdf_Values = lidarData60PSI_pdf_Values./(sum(lidarData60PSI_pdf_Values))
measurementModel_Lidar_60PSI = struct
measurementModel_Lidar_60PSI.pressure = 60
measurementModel_Lidar_60PSI.pdfKeys = lidarData60PSI_pdf_Keys
measurementModel_Lidar_60PSI.pdf_normalised_values = lidarData60PSI_normalised_pdf_Values
measurementModel_Lidar_60PSI_normPdf_map = containers.Map(measurementModel_Lidar_60PSI.pdfKeys,measurementModel_Lidar_60PSI.pdf_normalised_values)

accelData60PSI = Accel60data %[1,-1,1,1,-1,5,3,1,1,-1,0,1,1,-1,3,4,3,2,1,-1,1,-1,0,1,1]
accelData60PSI_pdf_Keys = unique(accelData60PSI)
accelData60PSI_pdf_Values = histc( accelData60PSI,unique(accelData60PSI) )
accelData60PSI_normalised_pdf_Values = accelData60PSI_pdf_Values./(sum(accelData60PSI_pdf_Values))
measurementModel_Accel_60PSI = struct
measurementModel_Accel_60PSI.pressure = 60
measurementModel_Accel_60PSI.pdfKeys = accelData60PSI_pdf_Keys
measurementModel_Accel_60PSI.pdf_normalised_values = accelData60PSI_normalised_pdf_Values
measurementModel_Accel_60PSI_normPdf_map = containers.Map(measurementModel_Accel_60PSI.pdfKeys,measurementModel_Accel_60PSI.pdf_normalised_values)

%PSI 55 psi 
lidarData55PSI = Lidar55data %[5,4,5,4,5,3,2,2,4,5,5,4,5,5,3,2,1,3,5,4,5,5,4,4,5]
lidarData55PSI_pdf_Keys = unique(lidarData55PSI)
lidarData55PSI_pdf_Values = histc( lidarData55PSI,unique(lidarData55PSI) )
lidarData55PSI_normalised_pdf_Values = lidarData55PSI_pdf_Values./(sum(lidarData55PSI_pdf_Values))
measurementModel_Lidar_55PSI = struct
measurementModel_Lidar_55PSI.pressure = 55
measurementModel_Lidar_55PSI.pdfKeys = lidarData55PSI_pdf_Keys
measurementModel_Lidar_55PSI.pdf_normalised_values = lidarData55PSI_normalised_pdf_Values
measurementModel_Lidar_55PSI_normPdf_map = containers.Map(measurementModel_Lidar_55PSI.pdfKeys,measurementModel_Lidar_55PSI.pdf_normalised_values)

accelData55PSI = Accel55data %[1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData55PSI_pdf_Keys = unique(accelData55PSI)
accelData55PSI_pdf_Values = histc( accelData55PSI,unique(accelData55PSI) )
accelData55PSI_normalised_pdf_Values = accelData55PSI_pdf_Values./(sum(accelData55PSI_pdf_Values))
measurementModel_Accel_55PSI = struct
measurementModel_Accel_55PSI.pressure = 55
measurementModel_Accel_55PSI.pdfKeys = accelData55PSI_pdf_Keys
measurementModel_Accel_55PSI.pdf_normalised_values = accelData55PSI_normalised_pdf_Values
measurementModel_Accel_55PSI_normPdf_map = containers.Map(measurementModel_Accel_55PSI.pdfKeys,measurementModel_Accel_55PSI.pdf_normalised_values)

%PSI 50 psi 
lidarData50PSI = Lidar50data %[4,4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
lidarData50PSI_pdf_Keys = unique(lidarData50PSI)
lidarData50PSI_pdf_Values = histc( lidarData50PSI,unique(lidarData50PSI) )
lidarData50PSI_normalised_pdf_Values = lidarData50PSI_pdf_Values./(sum(lidarData50PSI_pdf_Values))
measurementModel_Lidar_50PSI = struct
measurementModel_Lidar_50PSI.pressure = 50
measurementModel_Lidar_50PSI.pdfKeys = lidarData50PSI_pdf_Keys
measurementModel_Lidar_50PSI.pdf_normalised_values = lidarData50PSI_normalised_pdf_Values
measurementModel_Lidar_50PSI_normPdf_map = containers.Map(measurementModel_Lidar_50PSI.pdfKeys,measurementModel_Lidar_50PSI.pdf_normalised_values)


accelData50PSI = Accel50data %[1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData50PSI_pdf_Keys = unique(accelData50PSI)
accelData50PSI_pdf_Values = histc( accelData50PSI,unique(accelData50PSI) )
accelData50PSI_normalised_pdf_Values = accelData50PSI_pdf_Values./(sum(accelData50PSI_pdf_Values))
measurementModel_Accel_50PSI = struct
measurementModel_Accel_50PSI.pressure = 50
measurementModel_Accel_50PSI.pdfKeys = accelData50PSI_pdf_Keys
measurementModel_Accel_50PSI.pdf_normalised_values = accelData50PSI_normalised_pdf_Values
measurementModel_Accel_50PSI_normPdf_map = containers.Map(measurementModel_Accel_50PSI.pdfKeys,measurementModel_Accel_50PSI.pdf_normalised_values)

%PSI 45 psi 
lidarData45PSI = Lidar45data %[4,4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
lidarData45PSI_pdf_Keys = unique(lidarData45PSI)
lidarData45PSI_pdf_Values = histc( lidarData45PSI,unique(lidarData45PSI) )
lidarData45PSI_normalised_pdf_Values = lidarData45PSI_pdf_Values./(sum(lidarData45PSI_pdf_Values))
measurementModel_Lidar_45PSI = struct
measurementModel_Lidar_45PSI.pressure = 45
measurementModel_Lidar_45PSI.pdfKeys = lidarData45PSI_pdf_Keys
measurementModel_Lidar_45PSI.pdf_normalised_values = lidarData45PSI_normalised_pdf_Values
measurementModel_Lidar_45PSI_normPdf_map = containers.Map(measurementModel_Lidar_45PSI.pdfKeys,measurementModel_Lidar_45PSI.pdf_normalised_values)

accelData45PSI =  Accel45data %[1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData45PSI_pdf_Keys = unique(accelData45PSI)
accelData45PSI_pdf_Values = histc( accelData45PSI,unique(accelData45PSI) )
accelData45PSI_normalised_pdf_Values = accelData45PSI_pdf_Values./(sum(accelData45PSI_pdf_Values))
measurementModel_Accel_45PSI = struct
measurementModel_Accel_45PSI.pressure = 45
measurementModel_Accel_45PSI.pdfKeys = accelData45PSI_pdf_Keys
measurementModel_Accel_45PSI.pdf_normalised_values = accelData45PSI_normalised_pdf_Values
measurementModel_Accel_45PSI_normPdf_map = containers.Map(measurementModel_Accel_45PSI.pdfKeys,measurementModel_Accel_45PSI.pdf_normalised_values)

%PSI 40 psi 
lidarData40PSI = Lidar40data %[4,4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
lidarData40PSI_pdf_Keys = unique(lidarData40PSI)
lidarData40PSI_pdf_Values = histc( lidarData40PSI,unique(lidarData40PSI) )
lidarData40PSI_normalised_pdf_Values = lidarData40PSI_pdf_Values./(sum(lidarData40PSI_pdf_Values))
measurementModel_Lidar_40PSI = struct
measurementModel_Lidar_40PSI.pressure = 40
measurementModel_Lidar_40PSI.pdfKeys = lidarData40PSI_pdf_Keys
measurementModel_Lidar_40PSI.pdf_normalised_values = lidarData40PSI_normalised_pdf_Values
measurementModel_Lidar_40PSI_normPdf_map = containers.Map(measurementModel_Lidar_40PSI.pdfKeys,measurementModel_Lidar_40PSI.pdf_normalised_values)

accelData40PSI = Accel40data %[1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData40PSI_pdf_Keys = unique(accelData40PSI)
accelData40PSI_pdf_Values = histc( accelData40PSI,unique(accelData40PSI) )
accelData40PSI_normalised_pdf_Values = accelData40PSI_pdf_Values./(sum(accelData40PSI_pdf_Values))
measurementModel_Accel_40PSI = struct
measurementModel_Accel_40PSI.pressure = 40
measurementModel_Accel_40PSI.pdfKeys = accelData40PSI_pdf_Keys
measurementModel_Accel_40PSI.pdf_normalised_values = accelData40PSI_normalised_pdf_Values
measurementModel_Accel_40PSI_normPdf_map = containers.Map(measurementModel_Accel_40PSI.pdfKeys,measurementModel_Accel_40PSI.pdf_normalised_values)

%PSI 35 psi
lidarData35PSI = Lidar35data %[4,4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
lidarData35PSI_pdf_Keys = unique(lidarData35PSI)
lidarData35PSI_pdf_Values = histc( lidarData35PSI,unique(lidarData35PSI) )
lidarData35PSI_normalised_pdf_Values = lidarData35PSI_pdf_Values./(sum(lidarData35PSI_pdf_Values))
measurementModel_Lidar_35PSI = struct
measurementModel_Lidar_35PSI.pressure = 35
measurementModel_Lidar_35PSI.pdfKeys = lidarData35PSI_pdf_Keys
measurementModel_Lidar_35PSI.pdf_normalised_values = lidarData35PSI_normalised_pdf_Values
measurementModel_Lidar_35PSI_normPdf_map = containers.Map(measurementModel_Lidar_35PSI.pdfKeys,measurementModel_Lidar_35PSI.pdf_normalised_values)

accelData35PSI =  Accel35data %[1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData35PSI_pdf_Keys = unique(accelData35PSI)
accelData35PSI_pdf_Values = histc( accelData35PSI,unique(accelData35PSI) )
accelData35PSI_normalised_pdf_Values = accelData35PSI_pdf_Values./(sum(accelData35PSI_pdf_Values))
measurementModel_Accel_35PSI = struct
measurementModel_Accel_35PSI.pressure = 35
measurementModel_Accel_35PSI.pdfKeys = accelData35PSI_pdf_Keys
measurementModel_Accel_35PSI.pdf_normalised_values = accelData35PSI_normalised_pdf_Values
measurementModel_Accel_35PSI_normPdf_map = containers.Map(measurementModel_Accel_35PSI.pdfKeys,measurementModel_Accel_35PSI.pdf_normalised_values)

%PSI 30 psi
lidarData30PSI = Lidar30data %[4,4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
lidarData30PSI_pdf_Keys = unique(lidarData30PSI)
lidarData30PSI_pdf_Values = histc( lidarData30PSI,unique(lidarData30PSI) )
lidarData30PSI_normalised_pdf_Values = lidarData30PSI_pdf_Values./(sum(lidarData30PSI_pdf_Values))
measurementModel_Lidar_30PSI = struct
measurementModel_Lidar_30PSI.pressure = 30
measurementModel_Lidar_30PSI.pdfKeys = lidarData30PSI_pdf_Keys
measurementModel_Lidar_30PSI.pdf_normalised_values = lidarData30PSI_normalised_pdf_Values
measurementModel_Lidar_30PSI_normPdf_map = containers.Map(measurementModel_Lidar_30PSI.pdfKeys,measurementModel_Lidar_30PSI.pdf_normalised_values)

accelData30PSI =  Accel30data % [1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData30PSI_pdf_Keys = unique(accelData30PSI)
accelData30PSI_pdf_Values = histc( accelData30PSI,unique(accelData30PSI) )
accelData30PSI_normalised_pdf_Values = accelData30PSI_pdf_Values./(sum(accelData30PSI_pdf_Values))
measurementModel_Accel_30PSI = struct
measurementModel_Accel_30PSI.pressure = 30
measurementModel_Accel_30PSI.pdfKeys = accelData30PSI_pdf_Keys
measurementModel_Accel_30PSI.pdf_normalised_values = accelData30PSI_normalised_pdf_Values
measurementModel_Accel_30PSI_normPdf_map = containers.Map(measurementModel_Accel_30PSI.pdfKeys,measurementModel_Accel_30PSI.pdf_normalised_values)

%PSI 25 psi
lidarData25PSI = Lidar25data %[4,4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
lidarData25PSI_pdf_Keys = unique(lidarData25PSI)
lidarData25PSI_pdf_Values = histc( lidarData25PSI,unique(lidarData25PSI) )
lidarData25PSI_normalised_pdf_Values = lidarData25PSI_pdf_Values./(sum(lidarData25PSI_pdf_Values))
measurementModel_Lidar_25PSI = struct
measurementModel_Lidar_25PSI.pressure = 25
measurementModel_Lidar_25PSI.pdfKeys = lidarData25PSI_pdf_Keys
measurementModel_Lidar_25PSI.pdf_normalised_values = lidarData25PSI_normalised_pdf_Values
measurementModel_Lidar_25PSI_normPdf_map = containers.Map(measurementModel_Lidar_25PSI.pdfKeys,measurementModel_Lidar_25PSI.pdf_normalised_values)

accelData25PSI = Accel25data %[1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData25PSI_pdf_Keys = unique(accelData25PSI)
accelData25PSI_pdf_Values = histc( accelData25PSI,unique(accelData25PSI) )
accelData25PSI_normalised_pdf_Values = accelData25PSI_pdf_Values./(sum(accelData25PSI_pdf_Values))
measurementModel_Accel_25PSI = struct
measurementModel_Accel_25PSI.pressure = 25
measurementModel_Accel_25PSI.pdfKeys = accelData25PSI_pdf_Keys
measurementModel_Accel_25PSI.pdf_normalised_values = accelData25PSI_normalised_pdf_Values
measurementModel_Accel_25PSI_normPdf_map = containers.Map(measurementModel_Accel_25PSI.pdfKeys,measurementModel_Accel_25PSI.pdf_normalised_values)


%PSI 20 psi
lidarData20PSI = Lidar20data %[4,4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
lidarData20PSI_pdf_Keys = unique(lidarData20PSI)
lidarData20PSI_pdf_Values = histc( lidarData20PSI,unique(lidarData20PSI) )
lidarData20PSI_normalised_pdf_Values = lidarData20PSI_pdf_Values./(sum(lidarData20PSI_pdf_Values))
measurementModel_Lidar_20PSI = struct
measurementModel_Lidar_20PSI.pressure = 20
measurementModel_Lidar_20PSI.pdfKeys = lidarData20PSI_pdf_Keys
measurementModel_Lidar_20PSI.pdf_normalised_values = lidarData20PSI_normalised_pdf_Values
measurementModel_Lidar_20PSI_normPdf_map = containers.Map(measurementModel_Lidar_20PSI.pdfKeys,measurementModel_Lidar_20PSI.pdf_normalised_values)

accelData20PSI =  Accel20data  %[1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData20PSI_pdf_Keys = unique(accelData20PSI)
accelData20PSI_pdf_Values = histc( accelData20PSI,unique(accelData20PSI) )
accelData20PSI_normalised_pdf_Values = accelData20PSI_pdf_Values./(sum(accelData20PSI_pdf_Values))
measurementModel_Accel_20PSI = struct
measurementModel_Accel_20PSI.pressure = 20
measurementModel_Accel_20PSI.pdfKeys = accelData20PSI_pdf_Keys
measurementModel_Accel_20PSI.pdf_normalised_values = accelData20PSI_normalised_pdf_Values
measurementModel_Accel_20PSI_normPdf_map = containers.Map(measurementModel_Accel_20PSI.pdfKeys,measurementModel_Accel_20PSI.pdf_normalised_values)


%PSI 15 psi
lidarData15PSI = Lidar15data %[4,4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
lidarData15PSI_pdf_Keys = unique(lidarData15PSI)
lidarData15PSI_pdf_Values = histc( lidarData15PSI,unique(lidarData15PSI) )
lidarData15PSI_normalised_pdf_Values = lidarData15PSI_pdf_Values./(sum(lidarData15PSI_pdf_Values))
measurementModel_Lidar_15PSI = struct
measurementModel_Lidar_15PSI.pressure = 15
measurementModel_Lidar_15PSI.pdfKeys = lidarData15PSI_pdf_Keys
measurementModel_Lidar_15PSI.pdf_normalised_values = lidarData15PSI_normalised_pdf_Values
measurementModel_Lidar_15PSI_normPdf_map = containers.Map(measurementModel_Lidar_15PSI.pdfKeys,measurementModel_Lidar_15PSI.pdf_normalised_values)

accelData15PSI = Accel15data  % [1,-1,1,1,-1,4,4,1,1,-1,0,1,1,-1,3,4,4,2,1,-1,1,-1,0,1,1]
accelData15PSI_pdf_Keys = unique(accelData15PSI)
accelData15PSI_pdf_Values = histc( accelData15PSI,unique(accelData15PSI) )
accelData15PSI_normalised_pdf_Values = accelData15PSI_pdf_Values./(sum(accelData15PSI_pdf_Values))
measurementModel_Accel_15PSI = struct
measurementModel_Accel_15PSI.pressure = 15
measurementModel_Accel_15PSI.pdfKeys = accelData15PSI_pdf_Keys
measurementModel_Accel_15PSI.pdf_normalised_values = accelData15PSI_normalised_pdf_Values
measurementModel_Accel_15PSI_normPdf_map = containers.Map(measurementModel_Accel_15PSI.pdfKeys,measurementModel_Accel_15PSI.pdf_normalised_values)


% Now for the motion models...the chances of this value being current
% given what the previous value was

x_state_probability = 1/8 % because there are 8 possible states 24->31

x_motion_model_60PSI = struct;
x_motion_model_60PSI.pressure = 60
x_motion_model_60PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_60PSI.previousValue_Values = [0.005,0.005,0.01,0.02,0.02,0.02,0.02,0.3,0.3,0.3]
x_motion_model_60PSI_mapped = containers.Map( x_motion_model_60PSI.previousValue_Keys, x_motion_model_60PSI.previousValue_Values)

x_motion_model_55PSI = struct;
x_motion_model_55PSI.pressure = 55
x_motion_model_55PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_55PSI.previousValue_Values = [0.005,0.005,0.01,0.02,0.02,0.02,0.02,0.3,0.3,0.3]
x_motion_model_55PSI_mapped = containers.Map( x_motion_model_55PSI.previousValue_Keys, x_motion_model_55PSI.previousValue_Values)


x_motion_model_50PSI = struct;
x_motion_model_50PSI.pressure = 50
x_motion_model_50PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_50PSI.previousValue_Values = [0.005,0.005,0.01,0.02,0.02,0.02,0.3,0.3,0.3,0.02]
x_motion_model_50PSI_mapped = containers.Map( x_motion_model_50PSI.previousValue_Keys, x_motion_model_50PSI.previousValue_Values)

x_motion_model_45PSI = struct;
x_motion_model_45PSI.pressure = 45
x_motion_model_45PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_45PSI.previousValue_Values = [0.01,0.02,0.02,0.02,0.02,0.3,0.3,0.3,0.005,0.005]
x_motion_model_45PSI_mapped = containers.Map( x_motion_model_45PSI.previousValue_Keys, x_motion_model_45PSI.previousValue_Values)

x_motion_model_40PSI = struct;
x_motion_model_40PSI.pressure = 40
x_motion_model_40PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_40PSI.previousValue_Values = [0.01,0.02,0.02,0.02,0.3,0.3,0.3,0.02,0.005,0.005]
x_motion_model_40PSI_mapped = containers.Map( x_motion_model_40PSI.previousValue_Keys, x_motion_model_40PSI.previousValue_Values)

x_motion_model_35PSI = struct;
x_motion_model_35PSI.pressure = 35
x_motion_model_35PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_35PSI.previousValue_Values = [0.01,0.02,0.02,0.3,0.3,0.3,0.02,0.02,0.005,0.005]
x_motion_model_35PSI_mapped = containers.Map( x_motion_model_35PSI.previousValue_Keys, x_motion_model_35PSI.previousValue_Values)

x_motion_model_30PSI = struct;
x_motion_model_30PSI.pressure = 30
x_motion_model_30PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_30PSI.previousValue_Values = [0.01,0.02,0.3,0.3,0.3,0.02,0.02,0.02,0.005,0.005]
x_motion_model_30PSI_mapped = containers.Map( x_motion_model_30PSI.previousValue_Keys, x_motion_model_30PSI.previousValue_Values)

x_motion_model_25PSI = struct;
x_motion_model_25PSI.pressure = 25
x_motion_model_25PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_25PSI.previousValue_Values = [0.02,0.3,0.3,0.3,0.02,0.02,0.02,0.01,0.005,0.005]
x_motion_model_25PSI_mapped = containers.Map( x_motion_model_25PSI.previousValue_Keys, x_motion_model_25PSI.previousValue_Values)

x_motion_model_20PSI = struct;
x_motion_model_20PSI.pressure = 20
x_motion_model_20PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_20PSI.previousValue_Values = [0.3,0.3,0.3,0.02,0.02,0.02,0.02,0.01,0.005,0.005]
x_motion_model_20PSI_mapped = containers.Map( x_motion_model_20PSI.previousValue_Keys, x_motion_model_20PSI.previousValue_Values)

x_motion_model_15PSI = struct;
x_motion_model_15PSI.pressure = 15
x_motion_model_15PSI.previousValue_Keys = [15,20,25,30,35,40,45,50,55,60]
x_motion_model_15PSI.previousValue_Values = [0.3,0.3,0.3,0.02,0.02,0.02,0.02,0.01,0.005,0.005]
x_motion_model_15PSI_mapped = containers.Map( x_motion_model_15PSI.previousValue_Keys, x_motion_model_15PSI.previousValue_Values)


% Lets run through our prediction equation and assume that the data coming
% in is for 25PSI just to make it easy this first time :) 

% Initialise equation, I'm gonna start it off with a PSI of 60 therefore x1 = 60, and see if
% it is able to move toward the actual PSI of x 
% Prediction 1 is motion model of our pick multiplied by p(of that PSI value)
predictionx1 = x_motion_model_60PSI.previousValue_Values * x_state_probability %lets start it nice and easy with a typical value

% first y value in is lidar data with value 5; and accel data with value 1
%update1 =  % [ P(y1 | x1) * p(x1) ] / p(y1) 
% so the first Lidar data point for 25 PSI is 5, but we're gonna check that
% against the probability density function for 30 PSI!!! 
probY1suchthatX1 = measurementModel_Lidar_60PSI_normPdf_map(463) % 5 is our arbitrary but plausible starting data value
probY1suchthatX1ACCEL = measurementModel_Accel_60PSI_normPdf_map()
% probX1 %hmmm, this is the probability of 5 in general!!! so the average of all pdf values for 5?
probX1 = predictionx1 
%probability full stop of getting this data reading of 5
probY1 = ( measurementModel_Lidar_60PSI_normPdf_map(463) + measurementModel_Lidar_50PSI_normPdf_map(463) ) / 2
update1 = ( probY1suchthatX1 * probX1 ) / probY1

%Okay that worked and the update resulted in a new pdf !!! :) 
% Now let's get into the recursive bit..... :) 
% FIRST STEP IS PREDICTION!!! 
predictionXpreviousMapped60 = containers.Map(x_motion_model_60PSI.previousValue_Keys,predictionx1)
%prediction chances of value being 60PSI = motion_model prob for 60PSI * %previous optimal guess
predictionOfXbeing60PSIsuchthatPrevXwas60 = x_motion_model_60PSI_mapped(60) * predictionXpreviousMapped60(60)
%prediction chances of value being 28PSI 
predictionOfXbeing60PSIsuchthatPrevXwas55 = x_motion_model_60PSI_mapped(55) * predictionXpreviousMapped60(55)
%prediction chances of value being 25PSI
predictionOfXbeing60PSIsuchthatPrevXwas50 = x_motion_model_60PSI_mapped(50) * predictionXpreviousMapped60(50)
predictionOfXbeing60PSIsuchthatPrevXwas45 = x_motion_model_60PSI_mapped(45) * predictionXpreviousMapped60(45);
predictionOfXbeing60PSIsuchthatPrevXwas40 = x_motion_model_60PSI_mapped(40) * predictionXpreviousMapped60(40);
predictionOfXbeing60PSIsuchthatPrevXwas35 = x_motion_model_60PSI_mapped(35) * predictionXpreviousMapped60(35);
predictionOfXbeing60PSIsuchthatPrevXwas30 = x_motion_model_60PSI_mapped(30) * predictionXpreviousMapped60(30);
predictionOfXbeing60PSIsuchthatPrevXwas25 = x_motion_model_60PSI_mapped(25) * predictionXpreviousMapped60(25);
predictionOfXbeing60PSIsuchthatPrevXwas20 = x_motion_model_60PSI_mapped(20) * predictionXpreviousMapped60(20);
predictionOfXbeing60PSIsuchthatPrevXwas15 = x_motion_model_60PSI_mapped(15) * predictionXpreviousMapped60(15);
%Overall chances of 60PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall60PSIchances = predictionOfXbeing60PSIsuchthatPrevXwas60 + predictionOfXbeing60PSIsuchthatPrevXwas55 + predictionOfXbeing60PSIsuchthatPrevXwas50 +predictionOfXbeing60PSIsuchthatPrevXwas45 ...
    + predictionOfXbeing60PSIsuchthatPrevXwas40 + predictionOfXbeing60PSIsuchthatPrevXwas35 + predictionOfXbeing60PSIsuchthatPrevXwas30 ...
    + predictionOfXbeing60PSIsuchthatPrevXwas25 + predictionOfXbeing60PSIsuchthatPrevXwas20 + predictionOfXbeing60PSIsuchthatPrevXwas15;



predictionXpreviousMapped55 = containers.Map(x_motion_model_55PSI.previousValue_Keys,predictionx1)
%prediction chances of value being 60PSI = motion_model prob for 60PSI * %previous optimal guess
predictionOfXbeing55PSIsuchthatPrevXwas60 = x_motion_model_55PSI_mapped(60) * predictionXpreviousMapped55(60)
%prediction chances of value being 55PSI 
predictionOfXbeing55PSIsuchthatPrevXwas55 = x_motion_model_55PSI_mapped(55) * predictionXpreviousMapped55(55)
%prediction chances of value being 50PSI
predictionOfXbeing55PSIsuchthatPrevXwas50 = x_motion_model_55PSI_mapped(50) * predictionXpreviousMapped55(50)

predictionOfXbeing55PSIsuchthatPrevXwas45 = x_motion_model_55PSI_mapped(45) * predictionXpreviousMapped55(45);
predictionOfXbeing55PSIsuchthatPrevXwas40 = x_motion_model_55PSI_mapped(40) * predictionXpreviousMapped55(40);
predictionOfXbeing55PSIsuchthatPrevXwas35 = x_motion_model_55PSI_mapped(35) * predictionXpreviousMapped55(35);
predictionOfXbeing55PSIsuchthatPrevXwas30 = x_motion_model_55PSI_mapped(30) * predictionXpreviousMapped55(30);
predictionOfXbeing55PSIsuchthatPrevXwas25 = x_motion_model_55PSI_mapped(25) * predictionXpreviousMapped55(25);
predictionOfXbeing55PSIsuchthatPrevXwas20 = x_motion_model_55PSI_mapped(20) * predictionXpreviousMapped55(20);
predictionOfXbeing55PSIsuchthatPrevXwas15 = x_motion_model_55PSI_mapped(15) * predictionXpreviousMapped55(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall55PSIchances = predictionOfXbeing55PSIsuchthatPrevXwas60 + predictionOfXbeing55PSIsuchthatPrevXwas55 + predictionOfXbeing55PSIsuchthatPrevXwas50 ...
    + predictionOfXbeing55PSIsuchthatPrevXwas45 + predictionOfXbeing55PSIsuchthatPrevXwas40 + predictionOfXbeing55PSIsuchthatPrevXwas35 ...
    + predictionOfXbeing55PSIsuchthatPrevXwas30 + predictionOfXbeing55PSIsuchthatPrevXwas25 + predictionOfXbeing55PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing55PSIsuchthatPrevXwas15;

predictionXpreviousMapped50 = containers.Map(x_motion_model_50PSI.previousValue_Keys,predictionx1)
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing50PSIsuchthatPrevXwas60 = x_motion_model_50PSI_mapped(60) * predictionXpreviousMapped50(60)
%prediction chances of value being 28PSI 
predictionOfXbeing50PSIsuchthatPrevXwas55 = x_motion_model_50PSI_mapped(55) * predictionXpreviousMapped50(55)
%prediction chances of value being 25PSI
predictionOfXbeing50PSIsuchthatPrevXwas50 = x_motion_model_50PSI_mapped(50) * predictionXpreviousMapped50(50)
predictionOfXbeing50PSIsuchthatPrevXwas45 = x_motion_model_50PSI_mapped(45) * predictionXpreviousMapped50(45);
predictionOfXbeing50PSIsuchthatPrevXwas40 = x_motion_model_50PSI_mapped(40) * predictionXpreviousMapped50(40);
predictionOfXbeing50PSIsuchthatPrevXwas35 = x_motion_model_50PSI_mapped(35) * predictionXpreviousMapped50(35);
predictionOfXbeing50PSIsuchthatPrevXwas30 = x_motion_model_50PSI_mapped(30) * predictionXpreviousMapped50(30);
predictionOfXbeing50PSIsuchthatPrevXwas25 = x_motion_model_50PSI_mapped(25) * predictionXpreviousMapped50(25);
predictionOfXbeing50PSIsuchthatPrevXwas20 = x_motion_model_50PSI_mapped(20) * predictionXpreviousMapped50(20);
predictionOfXbeing50PSIsuchthatPrevXwas15 = x_motion_model_50PSI_mapped(15) * predictionXpreviousMapped50(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall50PSIchances = predictionOfXbeing50PSIsuchthatPrevXwas60 + predictionOfXbeing50PSIsuchthatPrevXwas55 + predictionOfXbeing50PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing50PSIsuchthatPrevXwas45 + predictionOfXbeing50PSIsuchthatPrevXwas40 + predictionOfXbeing50PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing50PSIsuchthatPrevXwas30 + predictionOfXbeing50PSIsuchthatPrevXwas25 + predictionOfXbeing50PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing50PSIsuchthatPrevXwas15; 

predictionXpreviousMapped45 = containers.Map(x_motion_model_45PSI.previousValue_Keys,predictionx1)
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing45PSIsuchthatPrevXwas60 = x_motion_model_45PSI_mapped(60) * predictionXpreviousMapped45(60)
%prediction chances of value being 28PSI 
predictionOfXbeing45PSIsuchthatPrevXwas55 = x_motion_model_45PSI_mapped(55) * predictionXpreviousMapped45(55)
%prediction chances of value being 25PSI
predictionOfXbeing45PSIsuchthatPrevXwas50 = x_motion_model_45PSI_mapped(50) * predictionXpreviousMapped45(50)
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
predictionOfXbeing45PSIsuchthatPrevXwas45 = x_motion_model_45PSI_mapped(45) * predictionXpreviousMapped45(45);
predictionOfXbeing45PSIsuchthatPrevXwas40 = x_motion_model_45PSI_mapped(40) * predictionXpreviousMapped45(40);
predictionOfXbeing45PSIsuchthatPrevXwas35 = x_motion_model_45PSI_mapped(35) * predictionXpreviousMapped45(35);
predictionOfXbeing45PSIsuchthatPrevXwas30 = x_motion_model_45PSI_mapped(30) * predictionXpreviousMapped45(30);
predictionOfXbeing45PSIsuchthatPrevXwas25 = x_motion_model_45PSI_mapped(25) * predictionXpreviousMapped45(25);
predictionOfXbeing45PSIsuchthatPrevXwas20 = x_motion_model_45PSI_mapped(20) * predictionXpreviousMapped45(20);
predictionOfXbeing45PSIsuchthatPrevXwas15 = x_motion_model_45PSI_mapped(15) * predictionXpreviousMapped45(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall45PSIchances = predictionOfXbeing45PSIsuchthatPrevXwas60 + predictionOfXbeing45PSIsuchthatPrevXwas55 + predictionOfXbeing45PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing45PSIsuchthatPrevXwas45 + predictionOfXbeing45PSIsuchthatPrevXwas40 + predictionOfXbeing45PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing45PSIsuchthatPrevXwas30 + predictionOfXbeing45PSIsuchthatPrevXwas25 + predictionOfXbeing45PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing45PSIsuchthatPrevXwas15;

predictionXpreviousMapped40 = containers.Map(x_motion_model_40PSI.previousValue_Keys,predictionx1);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing40PSIsuchthatPrevXwas60 = x_motion_model_40PSI_mapped(60) * predictionXpreviousMapped40(60);
%prediction chances of value being 28PSI 
predictionOfXbeing40PSIsuchthatPrevXwas55 = x_motion_model_40PSI_mapped(55) * predictionXpreviousMapped40(55);
%prediction chances of value being 25PSI
predictionOfXbeing40PSIsuchthatPrevXwas50 = x_motion_model_40PSI_mapped(50) * predictionXpreviousMapped40(50);
predictionOfXbeing40PSIsuchthatPrevXwas45 = x_motion_model_40PSI_mapped(45) * predictionXpreviousMapped40(45);
predictionOfXbeing40PSIsuchthatPrevXwas40 = x_motion_model_40PSI_mapped(40) * predictionXpreviousMapped40(40);
predictionOfXbeing40PSIsuchthatPrevXwas35 = x_motion_model_40PSI_mapped(35) * predictionXpreviousMapped40(35);
predictionOfXbeing40PSIsuchthatPrevXwas30 = x_motion_model_40PSI_mapped(30) * predictionXpreviousMapped40(30);
predictionOfXbeing40PSIsuchthatPrevXwas25 = x_motion_model_40PSI_mapped(25) * predictionXpreviousMapped40(25);
predictionOfXbeing40PSIsuchthatPrevXwas20 = x_motion_model_40PSI_mapped(20) * predictionXpreviousMapped40(20);
predictionOfXbeing40PSIsuchthatPrevXwas15 = x_motion_model_40PSI_mapped(15) * predictionXpreviousMapped40(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall40PSIchances = predictionOfXbeing40PSIsuchthatPrevXwas60 + predictionOfXbeing40PSIsuchthatPrevXwas55 + predictionOfXbeing40PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing40PSIsuchthatPrevXwas45 + predictionOfXbeing40PSIsuchthatPrevXwas40 + predictionOfXbeing40PSIsuchthatPrevXwas35 + ... 
    predictionOfXbeing40PSIsuchthatPrevXwas30 + predictionOfXbeing40PSIsuchthatPrevXwas25 + predictionOfXbeing40PSIsuchthatPrevXwas20 + ... 
    predictionOfXbeing40PSIsuchthatPrevXwas15; 

predictionXpreviousMapped35 = containers.Map(x_motion_model_35PSI.previousValue_Keys,predictionx1);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing35PSIsuchthatPrevXwas60 = x_motion_model_35PSI_mapped(60) * predictionXpreviousMapped35(60);
%prediction chances of value being 28PSI 
predictionOfXbeing35PSIsuchthatPrevXwas55 = x_motion_model_35PSI_mapped(55) * predictionXpreviousMapped35(55);
%prediction chances of value being 25PSI
predictionOfXbeing35PSIsuchthatPrevXwas50 = x_motion_model_35PSI_mapped(50) * predictionXpreviousMapped35(50);
predictionOfXbeing35PSIsuchthatPrevXwas45 = x_motion_model_35PSI_mapped(45) * predictionXpreviousMapped35(45);
predictionOfXbeing35PSIsuchthatPrevXwas40 = x_motion_model_35PSI_mapped(40) * predictionXpreviousMapped35(40);
predictionOfXbeing35PSIsuchthatPrevXwas35 = x_motion_model_35PSI_mapped(35) * predictionXpreviousMapped35(35);
predictionOfXbeing35PSIsuchthatPrevXwas30 = x_motion_model_35PSI_mapped(30) * predictionXpreviousMapped35(30);
predictionOfXbeing35PSIsuchthatPrevXwas25 = x_motion_model_35PSI_mapped(25) * predictionXpreviousMapped35(25);
predictionOfXbeing35PSIsuchthatPrevXwas20 = x_motion_model_35PSI_mapped(20) * predictionXpreviousMapped35(20);
predictionOfXbeing35PSIsuchthatPrevXwas15 = x_motion_model_35PSI_mapped(15) * predictionXpreviousMapped35(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall35PSIchances = predictionOfXbeing35PSIsuchthatPrevXwas60 + predictionOfXbeing35PSIsuchthatPrevXwas55 + predictionOfXbeing35PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing35PSIsuchthatPrevXwas45 + predictionOfXbeing35PSIsuchthatPrevXwas40 + predictionOfXbeing35PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing35PSIsuchthatPrevXwas30 + predictionOfXbeing35PSIsuchthatPrevXwas25 + predictionOfXbeing35PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing35PSIsuchthatPrevXwas15; 

predictionXpreviousMapped30 = containers.Map(x_motion_model_30PSI.previousValue_Keys,predictionx1);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing30PSIsuchthatPrevXwas60 = x_motion_model_30PSI_mapped(60) * predictionXpreviousMapped30(60);
%prediction chances of value being 28PSI 
predictionOfXbeing30PSIsuchthatPrevXwas55 = x_motion_model_30PSI_mapped(55) * predictionXpreviousMapped30(55);
%prediction chances of value being 25PSI
predictionOfXbeing30PSIsuchthatPrevXwas50 = x_motion_model_30PSI_mapped(50) * predictionXpreviousMapped30(50);
predictionOfXbeing30PSIsuchthatPrevXwas45 = x_motion_model_30PSI_mapped(45) * predictionXpreviousMapped30(45);
predictionOfXbeing30PSIsuchthatPrevXwas40 = x_motion_model_30PSI_mapped(40) * predictionXpreviousMapped30(40);
predictionOfXbeing30PSIsuchthatPrevXwas35 = x_motion_model_30PSI_mapped(35) * predictionXpreviousMapped30(35);
predictionOfXbeing30PSIsuchthatPrevXwas30 = x_motion_model_30PSI_mapped(30) * predictionXpreviousMapped30(30);
predictionOfXbeing30PSIsuchthatPrevXwas25 = x_motion_model_30PSI_mapped(25) * predictionXpreviousMapped30(25);
predictionOfXbeing30PSIsuchthatPrevXwas20 = x_motion_model_30PSI_mapped(20) * predictionXpreviousMapped30(20);
predictionOfXbeing30PSIsuchthatPrevXwas15 = x_motion_model_30PSI_mapped(15) * predictionXpreviousMapped30(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall30PSIchances = predictionOfXbeing30PSIsuchthatPrevXwas60 + predictionOfXbeing30PSIsuchthatPrevXwas55 + predictionOfXbeing30PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing30PSIsuchthatPrevXwas45 + predictionOfXbeing30PSIsuchthatPrevXwas40 + predictionOfXbeing30PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing30PSIsuchthatPrevXwas30 + predictionOfXbeing30PSIsuchthatPrevXwas25 + predictionOfXbeing30PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing30PSIsuchthatPrevXwas15;


predictionXpreviousMapped25 = containers.Map(x_motion_model_25PSI.previousValue_Keys,predictionx1);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing25PSIsuchthatPrevXwas60 = x_motion_model_25PSI_mapped(60) * predictionXpreviousMapped25(60);
%prediction chances of value being 28PSI 
predictionOfXbeing25PSIsuchthatPrevXwas55 = x_motion_model_25PSI_mapped(55) * predictionXpreviousMapped25(55);
%prediction chances of value being 25PSI
predictionOfXbeing25PSIsuchthatPrevXwas50 = x_motion_model_25PSI_mapped(50) * predictionXpreviousMapped25(50);
predictionOfXbeing25PSIsuchthatPrevXwas45 = x_motion_model_25PSI_mapped(45) * predictionXpreviousMapped25(45);
predictionOfXbeing25PSIsuchthatPrevXwas40 = x_motion_model_25PSI_mapped(40) * predictionXpreviousMapped25(40);
predictionOfXbeing25PSIsuchthatPrevXwas35 = x_motion_model_25PSI_mapped(35) * predictionXpreviousMapped25(35);
predictionOfXbeing25PSIsuchthatPrevXwas30 = x_motion_model_25PSI_mapped(30) * predictionXpreviousMapped25(30);
predictionOfXbeing25PSIsuchthatPrevXwas25 = x_motion_model_25PSI_mapped(25) * predictionXpreviousMapped25(25);
predictionOfXbeing25PSIsuchthatPrevXwas20 = x_motion_model_25PSI_mapped(20) * predictionXpreviousMapped25(20);
predictionOfXbeing25PSIsuchthatPrevXwas15 = x_motion_model_25PSI_mapped(15) * predictionXpreviousMapped25(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall25PSIchances = predictionOfXbeing25PSIsuchthatPrevXwas60 + predictionOfXbeing25PSIsuchthatPrevXwas55 + predictionOfXbeing25PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing25PSIsuchthatPrevXwas45 + predictionOfXbeing25PSIsuchthatPrevXwas40 + predictionOfXbeing25PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing25PSIsuchthatPrevXwas30 + predictionOfXbeing25PSIsuchthatPrevXwas25 + predictionOfXbeing25PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing25PSIsuchthatPrevXwas15; 

predictionXpreviousMapped20 = containers.Map(x_motion_model_20PSI.previousValue_Keys,predictionx1);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing20PSIsuchthatPrevXwas60 = x_motion_model_20PSI_mapped(60) * predictionXpreviousMapped20(60);
%prediction chances of value being 28PSI 
predictionOfXbeing20PSIsuchthatPrevXwas55 = x_motion_model_20PSI_mapped(55) * predictionXpreviousMapped20(55);
%prediction chances of value being 25PSI
predictionOfXbeing20PSIsuchthatPrevXwas50 = x_motion_model_20PSI_mapped(50) * predictionXpreviousMapped20(50);
predictionOfXbeing20PSIsuchthatPrevXwas45 = x_motion_model_20PSI_mapped(45) * predictionXpreviousMapped20(45);
predictionOfXbeing20PSIsuchthatPrevXwas40 = x_motion_model_20PSI_mapped(40) * predictionXpreviousMapped20(40);
predictionOfXbeing20PSIsuchthatPrevXwas35 = x_motion_model_20PSI_mapped(35) * predictionXpreviousMapped20(35);
predictionOfXbeing20PSIsuchthatPrevXwas30 = x_motion_model_20PSI_mapped(30) * predictionXpreviousMapped20(30);
predictionOfXbeing20PSIsuchthatPrevXwas25 = x_motion_model_20PSI_mapped(25) * predictionXpreviousMapped20(25);
predictionOfXbeing20PSIsuchthatPrevXwas20 = x_motion_model_20PSI_mapped(20) * predictionXpreviousMapped20(20);
predictionOfXbeing20PSIsuchthatPrevXwas15 = x_motion_model_20PSI_mapped(15) * predictionXpreviousMapped20(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall20PSIchances =  predictionOfXbeing20PSIsuchthatPrevXwas60 + predictionOfXbeing20PSIsuchthatPrevXwas55 + predictionOfXbeing20PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas45 + predictionOfXbeing20PSIsuchthatPrevXwas40 + predictionOfXbeing20PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas30 + predictionOfXbeing20PSIsuchthatPrevXwas25 + predictionOfXbeing20PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas15;

predictionXpreviousMapped15 = containers.Map(x_motion_model_15PSI.previousValue_Keys,predictionx1);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing15PSIsuchthatPrevXwas60 = x_motion_model_15PSI_mapped(60) * predictionXpreviousMapped15(60);
%prediction chances of value being 28PSI 
predictionOfXbeing20PSIsuchthatPrevXwas55 = x_motion_model_15PSI_mapped(55) * predictionXpreviousMapped15(55);
%prediction chances of value being 25PSI
predictionOfXbeing20PSIsuchthatPrevXwas50 = x_motion_model_15PSI_mapped(50) * predictionXpreviousMapped15(50);
predictionOfXbeing20PSIsuchthatPrevXwas45 = x_motion_model_15PSI_mapped(45) * predictionXpreviousMapped15(45);
predictionOfXbeing20PSIsuchthatPrevXwas40 = x_motion_model_15PSI_mapped(40) * predictionXpreviousMapped15(40);
predictionOfXbeing20PSIsuchthatPrevXwas35 = x_motion_model_15PSI_mapped(35) * predictionXpreviousMapped15(35);
predictionOfXbeing20PSIsuchthatPrevXwas30 = x_motion_model_15PSI_mapped(30) * predictionXpreviousMapped15(30);
predictionOfXbeing20PSIsuchthatPrevXwas25 = x_motion_model_15PSI_mapped(25) * predictionXpreviousMapped15(25);
predictionOfXbeing20PSIsuchthatPrevXwas20 = x_motion_model_15PSI_mapped(20) * predictionXpreviousMapped15(20);
predictionOfXbeing20PSIsuchthatPrevXwas15 = x_motion_model_15PSI_mapped(15) * predictionXpreviousMapped15(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall15PSIchances =  predictionOfXbeing15PSIsuchthatPrevXwas60 + predictionOfXbeing20PSIsuchthatPrevXwas55 + predictionOfXbeing20PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas45 + predictionOfXbeing20PSIsuchthatPrevXwas40 + predictionOfXbeing20PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas30 + predictionOfXbeing20PSIsuchthatPrevXwas25 + predictionOfXbeing20PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas15; 

predictionPDF = struct
predictionPDFACCEL = struct
predictionPDF.keys = [15,20,25,30,35,40,45,50,55,60]
predictionPDFACCEL.keys = [15,20,25,30,35,40,45,50,55,60]
predictionPDF.values = [overall15PSIchances,overall20PSIchances,overall25PSIchances,overall30PSIchances,overall35PSIchances,overall40PSIchances,overall45PSIchances,overall50PSIchances,overall55PSIchances,overall60PSIchances]
predictionPDFACCEL.values = [overall15PSIchances,overall20PSIchances,overall25PSIchances,overall30PSIchances,overall35PSIchances,overall40PSIchances,overall45PSIchances,overall50PSIchances,overall55PSIchances,overall60PSIchances]
predictionPDFmap = containers.Map(predictionPDF.keys,predictionPDF.values)
predictionPDFmapACCEL = containers.Map(predictionPDFACCEL.keys,predictionPDFACCEL.values)
% 2ND STEP IS UPDATE ... now we start using the actual real data readings

% for each possible state do ( measurement_model * prediction ) / ( sumOf measurement_model * prediction )
% ... to create a prob dist with each state having a probability
% updatedProb30PSI =  the real data readings start with 4 for the actual values coming in at 25 PSI 
numeratorPSI60 = measurementModel_Lidar_60PSI_normPdf_map(463) * overall60PSIchances
numeratorPSI55 = measurementModel_Lidar_55PSI_normPdf_map(463) * overall55PSIchances
numeratorPSI50 = measurementModel_Lidar_50PSI_normPdf_map(463) * overall50PSIchances
numeratorPSI45 = measurementModel_Lidar_45PSI_normPdf_map(463) * overall45PSIchances
numeratorPSI40 = measurementModel_Lidar_40PSI_normPdf_map(463) * overall40PSIchances
numeratorPSI35 = measurementModel_Lidar_35PSI_normPdf_map(463) * overall35PSIchances
numeratorPSI30 = measurementModel_Lidar_30PSI_normPdf_map(463) * overall30PSIchances
numeratorPSI25 = measurementModel_Lidar_25PSI_normPdf_map(463) * overall25PSIchances
numeratorPSI20 = measurementModel_Lidar_20PSI_normPdf_map(463) * overall20PSIchances
numeratorPSI15 = measurementModel_Lidar_15PSI_normPdf_map(463) * overall15PSIchances

numeratorPSI60ACCEL = measurementModel_Lidar_60PSI_normPdf_map(463) * overall60PSIchances
numeratorPSI55ACCEL = measurementModel_Lidar_55PSI_normPdf_map(463) * overall55PSIchances
numeratorPSI50ACCEL = measurementModel_Lidar_50PSI_normPdf_map(463) * overall50PSIchances
numeratorPSI45ACCEL = measurementModel_Lidar_45PSI_normPdf_map(463) * overall45PSIchances
numeratorPSI40ACCEL = measurementModel_Lidar_40PSI_normPdf_map(463) * overall40PSIchances
numeratorPSI35ACCEL = measurementModel_Lidar_35PSI_normPdf_map(463) * overall35PSIchances
numeratorPSI30ACCEL = measurementModel_Lidar_30PSI_normPdf_map(463) * overall30PSIchances
numeratorPSI25ACCEL = measurementModel_Lidar_25PSI_normPdf_map(463) * overall25PSIchances
numeratorPSI20ACCEL = measurementModel_Lidar_20PSI_normPdf_map(463) * overall20PSIchances
numeratorPSI15ACCEL = measurementModel_Lidar_15PSI_normPdf_map(463) * overall15PSIchances

% Denom is probability of getting this read sensor data value of 4 given 
% denomProb for 30psi
denom60psi = measurementModel_Lidar_60PSI_normPdf_map(463) * overall60PSIchances
denom55psi = measurementModel_Lidar_55PSI_normPdf_map(463) * overall55PSIchances
denom50psi = measurementModel_Lidar_50PSI_normPdf_map(463) * overall50PSIchances
denom45psi = measurementModel_Lidar_45PSI_normPdf_map(463) * overall45PSIchances
denom40psi = measurementModel_Lidar_40PSI_normPdf_map(463) * overall40PSIchances
denom35psi = measurementModel_Lidar_35PSI_normPdf_map(463) * overall35PSIchances
denom30psi = measurementModel_Lidar_30PSI_normPdf_map(463) * overall30PSIchances
denom25psi = measurementModel_Lidar_25PSI_normPdf_map(463) * overall25PSIchances
denom20psi = measurementModel_Lidar_20PSI_normPdf_map(463) * overall20PSIchances
denom15psi = measurementModel_Lidar_15PSI_normPdf_map(463) * overall15PSIchances

denominator = denom60psi + denom55psi + denom50psi + denom45psi + denom40psi ... 
    + denom35psi + denom30psi + denom25psi + denom20psi + denom15psi;

updatedMap = struct
updatedMap.keys = [15,20,25,30,35,40,45,50,55,60]
updatedMap.values = [numeratorPSI15 / denominator,numeratorPSI20 / denominator,numeratorPSI25 / denominator,numeratorPSI30 / denominator,numeratorPSI35 / denominator,numeratorPSI40 / denominator,numeratorPSI45 / denominator,numeratorPSI50 / denominator, numeratorPSI55 / denominator, numeratorPSI60 / denominator ]
updatedMapmapped = containers.Map(updatedMap.keys, updatedMap.values)


% LETS RECURSE ONCE AGAIN!!!! ----------------------------------
dataComingIn = Lidar15data %[4,5,4,5,3,2,3,4,5,4,4,5,5,3,2,2,3,5,4,5,4,4,4,5]
dataComingInACCEL = Accel15data
for myindex = 1:length(dataComingIn)
predictionXpreviousMapped60 = containers.Map(x_motion_model_60PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing60PSIsuchthatPrevXwas60 = x_motion_model_60PSI_mapped(60) * predictionXpreviousMapped60(60);
%prediction chances of value being 28PSI 
predictionOfXbeing60PSIsuchthatPrevXwas55 = x_motion_model_60PSI_mapped(55) * predictionXpreviousMapped60(55);
%prediction chances of value being 25PSI
predictionOfXbeing60PSIsuchthatPrevXwas50 = x_motion_model_60PSI_mapped(50) * predictionXpreviousMapped60(50);
predictionOfXbeing60PSIsuchthatPrevXwas45 = x_motion_model_60PSI_mapped(45) * predictionXpreviousMapped60(45);
predictionOfXbeing60PSIsuchthatPrevXwas40 = x_motion_model_60PSI_mapped(40) * predictionXpreviousMapped60(40);
predictionOfXbeing60PSIsuchthatPrevXwas35 = x_motion_model_60PSI_mapped(35) * predictionXpreviousMapped60(35);
predictionOfXbeing60PSIsuchthatPrevXwas30 = x_motion_model_60PSI_mapped(30) * predictionXpreviousMapped60(30);
predictionOfXbeing60PSIsuchthatPrevXwas25 = x_motion_model_60PSI_mapped(25) * predictionXpreviousMapped60(25);
predictionOfXbeing60PSIsuchthatPrevXwas20 = x_motion_model_60PSI_mapped(20) * predictionXpreviousMapped60(20);
predictionOfXbeing60PSIsuchthatPrevXwas15 = x_motion_model_60PSI_mapped(15) * predictionXpreviousMapped60(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall60PSIchances = predictionOfXbeing60PSIsuchthatPrevXwas60 + predictionOfXbeing60PSIsuchthatPrevXwas55 + predictionOfXbeing60PSIsuchthatPrevXwas50 +predictionOfXbeing60PSIsuchthatPrevXwas45 ...
    + predictionOfXbeing60PSIsuchthatPrevXwas40 + predictionOfXbeing60PSIsuchthatPrevXwas35 + predictionOfXbeing60PSIsuchthatPrevXwas30 ...
    + predictionOfXbeing60PSIsuchthatPrevXwas25 + predictionOfXbeing60PSIsuchthatPrevXwas20 + predictionOfXbeing60PSIsuchthatPrevXwas15;

predictionXpreviousMapped55 = containers.Map(x_motion_model_55PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing55PSIsuchthatPrevXwas60 = x_motion_model_55PSI_mapped(60) * predictionXpreviousMapped55(60);
%prediction chances of value being 28PSI 
predictionOfXbeing55PSIsuchthatPrevXwas55 = x_motion_model_55PSI_mapped(55) * predictionXpreviousMapped55(55);
%prediction chances of value being 25PSI
predictionOfXbeing55PSIsuchthatPrevXwas50 = x_motion_model_55PSI_mapped(50) * predictionXpreviousMapped55(50);
predictionOfXbeing55PSIsuchthatPrevXwas45 = x_motion_model_55PSI_mapped(45) * predictionXpreviousMapped55(45);
predictionOfXbeing55PSIsuchthatPrevXwas40 = x_motion_model_55PSI_mapped(40) * predictionXpreviousMapped55(40);
predictionOfXbeing55PSIsuchthatPrevXwas35 = x_motion_model_55PSI_mapped(35) * predictionXpreviousMapped55(35);
predictionOfXbeing55PSIsuchthatPrevXwas30 = x_motion_model_55PSI_mapped(30) * predictionXpreviousMapped55(30);
predictionOfXbeing55PSIsuchthatPrevXwas25 = x_motion_model_55PSI_mapped(25) * predictionXpreviousMapped55(25);
predictionOfXbeing55PSIsuchthatPrevXwas20 = x_motion_model_55PSI_mapped(20) * predictionXpreviousMapped55(20);
predictionOfXbeing55PSIsuchthatPrevXwas15 = x_motion_model_55PSI_mapped(15) * predictionXpreviousMapped55(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall55PSIchances = predictionOfXbeing55PSIsuchthatPrevXwas60 + predictionOfXbeing55PSIsuchthatPrevXwas55 + predictionOfXbeing55PSIsuchthatPrevXwas50 ...
    + predictionOfXbeing55PSIsuchthatPrevXwas45 + predictionOfXbeing55PSIsuchthatPrevXwas40 + predictionOfXbeing55PSIsuchthatPrevXwas35 ...
    + predictionOfXbeing55PSIsuchthatPrevXwas30 + predictionOfXbeing55PSIsuchthatPrevXwas25 + predictionOfXbeing55PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing55PSIsuchthatPrevXwas15;

predictionXpreviousMapped50 = containers.Map(x_motion_model_50PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing50PSIsuchthatPrevXwas60 = x_motion_model_50PSI_mapped(60) * predictionXpreviousMapped50(60);
%prediction chances of value being 28PSI 
predictionOfXbeing50PSIsuchthatPrevXwas55 = x_motion_model_50PSI_mapped(55) * predictionXpreviousMapped50(55);
%prediction chances of value being 25PSI
predictionOfXbeing50PSIsuchthatPrevXwas50 = x_motion_model_50PSI_mapped(50) * predictionXpreviousMapped50(50);
predictionOfXbeing50PSIsuchthatPrevXwas45 = x_motion_model_50PSI_mapped(45) * predictionXpreviousMapped50(45);
predictionOfXbeing50PSIsuchthatPrevXwas40 = x_motion_model_50PSI_mapped(40) * predictionXpreviousMapped50(40);
predictionOfXbeing50PSIsuchthatPrevXwas35 = x_motion_model_50PSI_mapped(35) * predictionXpreviousMapped50(35);
predictionOfXbeing50PSIsuchthatPrevXwas30 = x_motion_model_50PSI_mapped(30) * predictionXpreviousMapped50(30);
predictionOfXbeing50PSIsuchthatPrevXwas25 = x_motion_model_50PSI_mapped(25) * predictionXpreviousMapped50(25);
predictionOfXbeing50PSIsuchthatPrevXwas20 = x_motion_model_50PSI_mapped(20) * predictionXpreviousMapped50(20);
predictionOfXbeing50PSIsuchthatPrevXwas15 = x_motion_model_50PSI_mapped(15) * predictionXpreviousMapped50(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall50PSIchances = predictionOfXbeing50PSIsuchthatPrevXwas60 + predictionOfXbeing50PSIsuchthatPrevXwas55 + predictionOfXbeing50PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing50PSIsuchthatPrevXwas45 + predictionOfXbeing50PSIsuchthatPrevXwas40 + predictionOfXbeing50PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing50PSIsuchthatPrevXwas30 + predictionOfXbeing50PSIsuchthatPrevXwas25 + predictionOfXbeing50PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing50PSIsuchthatPrevXwas15; 

predictionXpreviousMapped45 = containers.Map(x_motion_model_45PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing45PSIsuchthatPrevXwas60 = x_motion_model_45PSI_mapped(60) * predictionXpreviousMapped45(60);
%prediction chances of value being 28PSI 
predictionOfXbeing45PSIsuchthatPrevXwas55 = x_motion_model_45PSI_mapped(55) * predictionXpreviousMapped45(55);
%prediction chances of value being 25PSI
predictionOfXbeing45PSIsuchthatPrevXwas50 = x_motion_model_45PSI_mapped(50) * predictionXpreviousMapped45(50);
predictionOfXbeing45PSIsuchthatPrevXwas45 = x_motion_model_45PSI_mapped(45) * predictionXpreviousMapped45(45);
predictionOfXbeing45PSIsuchthatPrevXwas40 = x_motion_model_45PSI_mapped(40) * predictionXpreviousMapped45(40);
predictionOfXbeing45PSIsuchthatPrevXwas35 = x_motion_model_45PSI_mapped(35) * predictionXpreviousMapped45(35);
predictionOfXbeing45PSIsuchthatPrevXwas30 = x_motion_model_45PSI_mapped(30) * predictionXpreviousMapped45(30);
predictionOfXbeing45PSIsuchthatPrevXwas25 = x_motion_model_45PSI_mapped(25) * predictionXpreviousMapped45(25);
predictionOfXbeing45PSIsuchthatPrevXwas20 = x_motion_model_45PSI_mapped(20) * predictionXpreviousMapped45(20);
predictionOfXbeing45PSIsuchthatPrevXwas15 = x_motion_model_45PSI_mapped(15) * predictionXpreviousMapped45(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall45PSIchances = predictionOfXbeing45PSIsuchthatPrevXwas60 + predictionOfXbeing45PSIsuchthatPrevXwas55 + predictionOfXbeing45PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing45PSIsuchthatPrevXwas45 + predictionOfXbeing45PSIsuchthatPrevXwas40 + predictionOfXbeing45PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing45PSIsuchthatPrevXwas30 + predictionOfXbeing45PSIsuchthatPrevXwas25 + predictionOfXbeing45PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing45PSIsuchthatPrevXwas15;

predictionXpreviousMapped40 = containers.Map(x_motion_model_40PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing40PSIsuchthatPrevXwas60 = x_motion_model_40PSI_mapped(60) * predictionXpreviousMapped40(60);
%prediction chances of value being 28PSI 
predictionOfXbeing40PSIsuchthatPrevXwas55 = x_motion_model_40PSI_mapped(55) * predictionXpreviousMapped40(55);
%prediction chances of value being 25PSI
predictionOfXbeing40PSIsuchthatPrevXwas50 = x_motion_model_40PSI_mapped(50) * predictionXpreviousMapped40(50);
predictionOfXbeing40PSIsuchthatPrevXwas45 = x_motion_model_40PSI_mapped(45) * predictionXpreviousMapped40(45);
predictionOfXbeing40PSIsuchthatPrevXwas40 = x_motion_model_40PSI_mapped(40) * predictionXpreviousMapped40(40);
predictionOfXbeing40PSIsuchthatPrevXwas35 = x_motion_model_40PSI_mapped(35) * predictionXpreviousMapped40(35);
predictionOfXbeing40PSIsuchthatPrevXwas30 = x_motion_model_40PSI_mapped(30) * predictionXpreviousMapped40(30);
predictionOfXbeing40PSIsuchthatPrevXwas25 = x_motion_model_40PSI_mapped(25) * predictionXpreviousMapped40(25);
predictionOfXbeing40PSIsuchthatPrevXwas20 = x_motion_model_40PSI_mapped(20) * predictionXpreviousMapped40(20);
predictionOfXbeing40PSIsuchthatPrevXwas15 = x_motion_model_40PSI_mapped(15) * predictionXpreviousMapped40(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall40PSIchances = predictionOfXbeing40PSIsuchthatPrevXwas60 + predictionOfXbeing40PSIsuchthatPrevXwas55 + predictionOfXbeing40PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing40PSIsuchthatPrevXwas45 + predictionOfXbeing40PSIsuchthatPrevXwas40 + predictionOfXbeing40PSIsuchthatPrevXwas35 + ... 
    predictionOfXbeing40PSIsuchthatPrevXwas30 + predictionOfXbeing40PSIsuchthatPrevXwas25 + predictionOfXbeing40PSIsuchthatPrevXwas20 + ... 
    predictionOfXbeing40PSIsuchthatPrevXwas15; 

predictionXpreviousMapped35 = containers.Map(x_motion_model_35PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing35PSIsuchthatPrevXwas60 = x_motion_model_35PSI_mapped(60) * predictionXpreviousMapped35(60);
%prediction chances of value being 28PSI 
predictionOfXbeing35PSIsuchthatPrevXwas55 = x_motion_model_35PSI_mapped(55) * predictionXpreviousMapped35(55);
%prediction chances of value being 25PSI
predictionOfXbeing35PSIsuchthatPrevXwas50 = x_motion_model_35PSI_mapped(50) * predictionXpreviousMapped35(50);
predictionOfXbeing35PSIsuchthatPrevXwas45 = x_motion_model_35PSI_mapped(45) * predictionXpreviousMapped35(45);
predictionOfXbeing35PSIsuchthatPrevXwas40 = x_motion_model_35PSI_mapped(40) * predictionXpreviousMapped35(40);
predictionOfXbeing35PSIsuchthatPrevXwas35 = x_motion_model_35PSI_mapped(35) * predictionXpreviousMapped35(35);
predictionOfXbeing35PSIsuchthatPrevXwas30 = x_motion_model_35PSI_mapped(30) * predictionXpreviousMapped35(30);
predictionOfXbeing35PSIsuchthatPrevXwas25 = x_motion_model_35PSI_mapped(25) * predictionXpreviousMapped35(25);
predictionOfXbeing35PSIsuchthatPrevXwas20 = x_motion_model_35PSI_mapped(20) * predictionXpreviousMapped35(20);
predictionOfXbeing35PSIsuchthatPrevXwas15 = x_motion_model_35PSI_mapped(15) * predictionXpreviousMapped35(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall35PSIchances = predictionOfXbeing35PSIsuchthatPrevXwas60 + predictionOfXbeing35PSIsuchthatPrevXwas55 + predictionOfXbeing35PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing35PSIsuchthatPrevXwas45 + predictionOfXbeing35PSIsuchthatPrevXwas40 + predictionOfXbeing35PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing35PSIsuchthatPrevXwas30 + predictionOfXbeing35PSIsuchthatPrevXwas25 + predictionOfXbeing35PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing35PSIsuchthatPrevXwas15; 


predictionXpreviousMapped30 = containers.Map(x_motion_model_30PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing30PSIsuchthatPrevXwas60 = x_motion_model_30PSI_mapped(60) * predictionXpreviousMapped30(60);
%prediction chances of value being 28PSI 
predictionOfXbeing30PSIsuchthatPrevXwas55 = x_motion_model_30PSI_mapped(55) * predictionXpreviousMapped30(55);
%prediction chances of value being 25PSI
predictionOfXbeing30PSIsuchthatPrevXwas50 = x_motion_model_30PSI_mapped(50) * predictionXpreviousMapped30(50);
predictionOfXbeing30PSIsuchthatPrevXwas45 = x_motion_model_30PSI_mapped(45) * predictionXpreviousMapped30(45);
predictionOfXbeing30PSIsuchthatPrevXwas40 = x_motion_model_30PSI_mapped(40) * predictionXpreviousMapped30(40);
predictionOfXbeing30PSIsuchthatPrevXwas35 = x_motion_model_30PSI_mapped(35) * predictionXpreviousMapped30(35);
predictionOfXbeing30PSIsuchthatPrevXwas30 = x_motion_model_30PSI_mapped(30) * predictionXpreviousMapped30(30);
predictionOfXbeing30PSIsuchthatPrevXwas25 = x_motion_model_30PSI_mapped(25) * predictionXpreviousMapped30(25);
predictionOfXbeing30PSIsuchthatPrevXwas20 = x_motion_model_30PSI_mapped(20) * predictionXpreviousMapped30(20);
predictionOfXbeing30PSIsuchthatPrevXwas15 = x_motion_model_30PSI_mapped(15) * predictionXpreviousMapped30(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall30PSIchances = predictionOfXbeing30PSIsuchthatPrevXwas60 + predictionOfXbeing30PSIsuchthatPrevXwas55 + predictionOfXbeing30PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing30PSIsuchthatPrevXwas45 + predictionOfXbeing30PSIsuchthatPrevXwas40 + predictionOfXbeing30PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing30PSIsuchthatPrevXwas30 + predictionOfXbeing30PSIsuchthatPrevXwas25 + predictionOfXbeing30PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing30PSIsuchthatPrevXwas15;


predictionXpreviousMapped25 = containers.Map(x_motion_model_25PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing25PSIsuchthatPrevXwas60 = x_motion_model_25PSI_mapped(60) * predictionXpreviousMapped25(60);
%prediction chances of value being 28PSI 
predictionOfXbeing25PSIsuchthatPrevXwas55 = x_motion_model_25PSI_mapped(55) * predictionXpreviousMapped25(55);
%prediction chances of value being 25PSI
predictionOfXbeing25PSIsuchthatPrevXwas50 = x_motion_model_25PSI_mapped(50) * predictionXpreviousMapped25(50);
predictionOfXbeing25PSIsuchthatPrevXwas45 = x_motion_model_25PSI_mapped(45) * predictionXpreviousMapped25(45);
predictionOfXbeing25PSIsuchthatPrevXwas40 = x_motion_model_25PSI_mapped(40) * predictionXpreviousMapped25(40);
predictionOfXbeing25PSIsuchthatPrevXwas35 = x_motion_model_25PSI_mapped(35) * predictionXpreviousMapped25(35);
predictionOfXbeing25PSIsuchthatPrevXwas30 = x_motion_model_25PSI_mapped(30) * predictionXpreviousMapped25(30);
predictionOfXbeing25PSIsuchthatPrevXwas25 = x_motion_model_25PSI_mapped(25) * predictionXpreviousMapped25(25);
predictionOfXbeing25PSIsuchthatPrevXwas20 = x_motion_model_25PSI_mapped(20) * predictionXpreviousMapped25(20);
predictionOfXbeing25PSIsuchthatPrevXwas15 = x_motion_model_25PSI_mapped(15) * predictionXpreviousMapped25(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall25PSIchances = predictionOfXbeing25PSIsuchthatPrevXwas60 + predictionOfXbeing25PSIsuchthatPrevXwas55 + predictionOfXbeing25PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing25PSIsuchthatPrevXwas45 + predictionOfXbeing25PSIsuchthatPrevXwas40 + predictionOfXbeing25PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing25PSIsuchthatPrevXwas30 + predictionOfXbeing25PSIsuchthatPrevXwas25 + predictionOfXbeing25PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing25PSIsuchthatPrevXwas15; 


predictionXpreviousMapped20 = containers.Map(x_motion_model_20PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing20PSIsuchthatPrevXwas60 = x_motion_model_20PSI_mapped(60) * predictionXpreviousMapped20(60);
%prediction chances of value being 28PSI 
predictionOfXbeing20PSIsuchthatPrevXwas55 = x_motion_model_20PSI_mapped(55) * predictionXpreviousMapped20(55);
%prediction chances of value being 25PSI
predictionOfXbeing20PSIsuchthatPrevXwas50 = x_motion_model_20PSI_mapped(50) * predictionXpreviousMapped20(50);
predictionOfXbeing20PSIsuchthatPrevXwas45 = x_motion_model_20PSI_mapped(45) * predictionXpreviousMapped20(45);
predictionOfXbeing20PSIsuchthatPrevXwas40 = x_motion_model_20PSI_mapped(40) * predictionXpreviousMapped20(40);
predictionOfXbeing20PSIsuchthatPrevXwas35 = x_motion_model_20PSI_mapped(35) * predictionXpreviousMapped20(35);
predictionOfXbeing20PSIsuchthatPrevXwas30 = x_motion_model_20PSI_mapped(30) * predictionXpreviousMapped20(30);
predictionOfXbeing20PSIsuchthatPrevXwas25 = x_motion_model_20PSI_mapped(25) * predictionXpreviousMapped20(25);
predictionOfXbeing20PSIsuchthatPrevXwas20 = x_motion_model_20PSI_mapped(20) * predictionXpreviousMapped20(20);
predictionOfXbeing20PSIsuchthatPrevXwas15 = x_motion_model_20PSI_mapped(15) * predictionXpreviousMapped20(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall20PSIchances =  predictionOfXbeing20PSIsuchthatPrevXwas60 + predictionOfXbeing20PSIsuchthatPrevXwas55 + predictionOfXbeing20PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas45 + predictionOfXbeing20PSIsuchthatPrevXwas40 + predictionOfXbeing20PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas30 + predictionOfXbeing20PSIsuchthatPrevXwas25 + predictionOfXbeing20PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas15;


predictionXpreviousMapped15 = containers.Map(x_motion_model_15PSI.previousValue_Keys,predictionPDF.values);
%prediction chances of value being 30PSI = motion_model prob for 30PSI * %previous optimal guess
predictionOfXbeing15PSIsuchthatPrevXwas60 = x_motion_model_15PSI_mapped(60) * predictionXpreviousMapped15(60);
%prediction chances of value being 28PSI 
predictionOfXbeing20PSIsuchthatPrevXwas55 = x_motion_model_15PSI_mapped(55) * predictionXpreviousMapped15(55);
%prediction chances of value being 25PSI
predictionOfXbeing20PSIsuchthatPrevXwas50 = x_motion_model_15PSI_mapped(50) * predictionXpreviousMapped15(50);
predictionOfXbeing20PSIsuchthatPrevXwas45 = x_motion_model_15PSI_mapped(45) * predictionXpreviousMapped15(45);
predictionOfXbeing20PSIsuchthatPrevXwas40 = x_motion_model_15PSI_mapped(40) * predictionXpreviousMapped15(40);
predictionOfXbeing20PSIsuchthatPrevXwas35 = x_motion_model_15PSI_mapped(35) * predictionXpreviousMapped15(35);
predictionOfXbeing20PSIsuchthatPrevXwas30 = x_motion_model_15PSI_mapped(30) * predictionXpreviousMapped15(30);
predictionOfXbeing20PSIsuchthatPrevXwas25 = x_motion_model_15PSI_mapped(25) * predictionXpreviousMapped15(25);
predictionOfXbeing20PSIsuchthatPrevXwas20 = x_motion_model_15PSI_mapped(20) * predictionXpreviousMapped15(20);
predictionOfXbeing20PSIsuchthatPrevXwas15 = x_motion_model_15PSI_mapped(15) * predictionXpreviousMapped15(15);
%Overall chances of 30PSI prediction = predictionOfXbeing30PSIsuchthatPrevXwas30
overall15PSIchances =  predictionOfXbeing15PSIsuchthatPrevXwas60 + predictionOfXbeing20PSIsuchthatPrevXwas55 + predictionOfXbeing20PSIsuchthatPrevXwas50 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas45 + predictionOfXbeing20PSIsuchthatPrevXwas40 + predictionOfXbeing20PSIsuchthatPrevXwas35 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas30 + predictionOfXbeing20PSIsuchthatPrevXwas25 + predictionOfXbeing20PSIsuchthatPrevXwas20 ... 
    + predictionOfXbeing20PSIsuchthatPrevXwas15; 

predictionPDF = struct;
predictionPDF.keys = [15,20,25,30,35,40,45,50,55,60];
predictionPDF.values = [overall15PSIchances,overall20PSIchances,overall25PSIchances,overall30PSIchances,overall35PSIchances,overall40PSIchances,overall45PSIchances,overall50PSIchances,overall55PSIchances,overall60PSIchances];
predictionPDFmap = containers.Map(predictionPDF.keys,predictionPDF.values);

% 2ND STEP IS UPDATE ... now we start using the actual real data readings

% for each possible state do ( measurement_model * prediction ) / ( sumOf measurement_model * prediction )
% ... to create a prob dist with each state having a probability
% updatedProb30PSI =  the real data readings start with 4 for the actual values coming in at 25 PSI 
if isKey(measurementModel_Lidar_60PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI60 = measurementModel_Lidar_60PSI_normPdf_map(dataComingIn(myindex)) * overall60PSIchances;
else
 numeratorPSI60 = 0
end
if isKey(measurementModel_Lidar_55PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI55 = measurementModel_Lidar_55PSI_normPdf_map(dataComingIn(myindex)) * overall55PSIchances;
else
  numeratorPSI55 = 0
end
if isKey(measurementModel_Lidar_50PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI50 = measurementModel_Lidar_50PSI_normPdf_map(dataComingIn(myindex)) * overall50PSIchances;
else
 numeratorPSI50 = 0
end
if isKey(measurementModel_Lidar_45PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI45 = measurementModel_Lidar_45PSI_normPdf_map(dataComingIn(myindex)) * overall45PSIchances;
else
 numeratorPSI45 = 0
end
if isKey(measurementModel_Lidar_40PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI40 = measurementModel_Lidar_40PSI_normPdf_map(dataComingIn(myindex)) * overall40PSIchances;
else
 numeratorPSI40 = 0
end
if isKey(measurementModel_Lidar_35PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI35 = measurementModel_Lidar_35PSI_normPdf_map(dataComingIn(myindex)) * overall35PSIchances;
else
 numeratorPSI35 = 0
end
if isKey(measurementModel_Lidar_30PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI30 = measurementModel_Lidar_30PSI_normPdf_map(dataComingIn(myindex)) * overall30PSIchances;
else
 numeratorPSI30 = 0
end
if isKey(measurementModel_Lidar_25PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI25 = measurementModel_Lidar_25PSI_normPdf_map(dataComingIn(myindex)) * overall25PSIchances;
else
 numeratorPSI25 = 0
end
if isKey(measurementModel_Lidar_20PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI20 = measurementModel_Lidar_20PSI_normPdf_map(dataComingIn(myindex)) * overall20PSIchances;
else
 numeratorPSI20 = 0
end
if isKey(measurementModel_Lidar_15PSI_normPdf_map,dataComingIn(myindex))
 numeratorPSI15 = measurementModel_Lidar_15PSI_normPdf_map(dataComingIn(myindex)) * overall15PSIchances;
else
 numeratorPSI15 = 0
end


% Denom is probability of getting this read sensor data value of 4 given 
% denomProb for 30psi
if isKey(measurementModel_Lidar_60PSI_normPdf_map,dataComingIn(myindex))
 denom60psi = measurementModel_Lidar_60PSI_normPdf_map(dataComingIn(myindex)) * overall60PSIchances;
else 
 denom60psi = 0
end
if isKey(measurementModel_Lidar_55PSI_normPdf_map,dataComingIn(myindex))
 denom55psi = measurementModel_Lidar_55PSI_normPdf_map(dataComingIn(myindex)) * overall55PSIchances;
else 
 denom55psi = 0
end
if isKey(measurementModel_Lidar_50PSI_normPdf_map,dataComingIn(myindex))
 denom50psi = measurementModel_Lidar_50PSI_normPdf_map(dataComingIn(myindex)) * overall50PSIchances;
else
 denom50psi = 0
end
if isKey(measurementModel_Lidar_45PSI_normPdf_map,dataComingIn(myindex))
 denom45psi = measurementModel_Lidar_45PSI_normPdf_map(dataComingIn(myindex)) * overall45PSIchances;
else
 denom45psi = 0
end
if isKey(measurementModel_Lidar_40PSI_normPdf_map,dataComingIn(myindex))
 denom40psi = measurementModel_Lidar_40PSI_normPdf_map(dataComingIn(myindex)) * overall40PSIchances;
else
 denom40psi = 0
end
if isKey(measurementModel_Lidar_35PSI_normPdf_map,dataComingIn(myindex))
 denom35psi = measurementModel_Lidar_35PSI_normPdf_map(dataComingIn(myindex)) * overall35PSIchances;
else
 denom35psi = 0
end
if isKey(measurementModel_Lidar_30PSI_normPdf_map,dataComingIn(myindex))
 denom30psi = measurementModel_Lidar_30PSI_normPdf_map(dataComingIn(myindex)) * overall30PSIchances;
else
 denom30psi = 0
end
if isKey(measurementModel_Lidar_25PSI_normPdf_map,dataComingIn(myindex))
 denom25psi = measurementModel_Lidar_25PSI_normPdf_map(dataComingIn(myindex)) * overall25PSIchances;
else
 denom25psi = 0
end
if isKey(measurementModel_Lidar_20PSI_normPdf_map,dataComingIn(myindex))
 denom20psi = measurementModel_Lidar_20PSI_normPdf_map(dataComingIn(myindex)) * overall20PSIchances;
else
 denom20psi = 0
end
if isKey(measurementModel_Lidar_15PSI_normPdf_map,dataComingIn(myindex))
 denom15psi = measurementModel_Lidar_15PSI_normPdf_map(dataComingIn(myindex)) * overall15PSIchances;
else
 denom15psi = 0
end


denominator = denom60psi + denom55psi + denom50psi + denom45psi + denom40psi + denom35psi + denom30psi + denom25psi + denom20psi + denom15psi;

updatedMap = struct;
updatedMap.keys = [15,20,25,30,35,40,45,50,55,60]
updatedMap.values = [numeratorPSI15 / denominator,numeratorPSI20 / denominator,numeratorPSI25 / denominator,numeratorPSI30 / denominator,numeratorPSI35 / denominator,numeratorPSI40 / denominator,numeratorPSI45 / denominator,numeratorPSI50 / denominator, numeratorPSI55 / denominator, numeratorPSI60 / denominator ]
updatedMapmapped = containers.Map(updatedMap.keys, updatedMap.values);
end