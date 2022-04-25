clear; clc;

load('AccelDataXvals.mat')
load('AccelDataYvals.mat')
load('AccelDataZvals.mat')

load('LidarDataValues.mat')

%Rearrange around origin, due to sensor bias
% Accel15psi_yValues = Accel15psi_yValues + 555;
% Accel20psi_yValues = Accel20psi_yValues + 555;
% Accel25psi_yValues = Accel25psi_yValues + 555;
% Accel30psi_yValues = Accel30psi_yValues + 555;
% Accel35psi_yValues = Accel35psi_yValues + 555;
% Accel40psi_yValues = Accel40psi_yValues + 555;
% Accel45psi_yValues = Accel45psi_yValues + 555;
% Accel50psi_yValues = Accel50psi_yValues + 555;
% Accel55psi_yValues = Accel55psi_yValues + 555;
% Accel60psi_yValues = Accel60psi_yValues + 555;

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

%Remove outliers which seem to occur in Lidar data sometimes, in the form
%of a few crazy high values
Lidar15psi_values(Lidar15psi_values > 550) = 500;
Lidar20psi_values(Lidar20psi_values > 550) = 500;
Lidar25psi_values(Lidar25psi_values > 550) = 500;
Lidar30psi_values(Lidar30psi_values > 550) = 500;
Lidar35psi_values(Lidar35psi_values > 550) = 500;
Lidar40psi_values(Lidar40psi_values > 550) = 500;
Lidar45psi_values(Lidar45psi_values > 550) = 500;
Lidar50psi_values(Lidar50psi_values > 550) = 500;
Lidar55psi_values(Lidar55psi_values > 550) = 500;
Lidar60psi_values(Lidar60psi_values > 550) = 500;

%Remove data below zero so that it doesn't affect peaks when later squared
%  Accel15psi_yValues(Accel15psi_yValues < (-300))=[];
%  Accel20psi_yValues(Accel20psi_yValues < (-300))=[];
%  Accel25psi_yValues(Accel25psi_yValues < (-300))=[];
%  Accel30psi_yValues(Accel30psi_yValues < (-300)) = [];
%  Accel35psi_yValues(Accel35psi_yValues < (-300)) = [];
%  Accel40psi_yValues(Accel40psi_yValues < (-300)) = [];
%  Accel45psi_yValues(Accel45psi_yValues < (-300)) = [];
%  Accel50psi_yValues(Accel50psi_yValues < (-300)) = [];
%  Accel55psi_yValues(Accel55psi_yValues < (-300)) = [];
%  Accel60psi_yValues(Accel60psi_yValues < (-300)) = [];

% figure;
% stem(Accel15psi_yValues); title(' filtered 15psi');
% figure;
% stem(Accel20psi_yValues);title(' filtered 20psi');
% figure;
% stem(Accel25psi_yValues); title(' filtered 25psi');
% figure;
% stem(Accel30psi_yValues); title(' filtered 30psi');
% figure;
% stem(Accel35psi_yValues);title(' filtered 35psi');
% figure;
% stem(Accel40psi_yValues);title(' filtered 40psi');
% figure;
% stem(Accel45psi_yValues);title(' filtered 45psi');
% figure;
% stem(Accel50psi_yValues);title(' filtered 50psi');
% figure;
% stem(Accel55psi_yValues);title('filtered 55psi');
% figure;
% stem(Accel60psi_yValues);title(' filtered 60psi');

%Appy a FIR filter to smooth out noisy data a bit

FILTER_LEN = 5;
FILTER_MULT = 0.2;

%first the x data values
for x = FILTER_LEN:length(Accel15psi_xValues)
    Accel15psi_xValues(x) = (Accel15psi_xValues(x)*FILTER_MULT) + (Accel15psi_xValues(x-1)*FILTER_MULT) + (Accel15psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel15psi_xValues(x-3)*FILTER_MULT) + (Accel15psi_xValues(x-4)*FILTER_MULT); 
% + (Accel15psi_yValues(x-5)*0.1) ...
%         + (Accel15psi_yValues(x-6)*0.1) + (Accel15psi_yValues(x-7)*0.1) + (Accel15psi_yValues(x-8)*0.1) ... 
%         + (Accel15psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel20psi_xValues)
    Accel20psi_xValues(x) = (Accel20psi_xValues(x)*FILTER_MULT) + (Accel20psi_xValues(x-1)*FILTER_MULT) + (Accel20psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel20psi_xValues(x-3)*FILTER_MULT) + (Accel20psi_xValues(x-4)*FILTER_MULT);
%         + (Accel20psi_yValues(x-5)*0.1) ...
%         + (Accel20psi_yValues(x-6)*0.1) + (Accel20psi_yValues(x-7)*0.1) + (Accel20psi_yValues(x-8)*0.1) ... 
%         + (Accel20psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel25psi_xValues)
    Accel25psi_xValues(x) = (Accel25psi_xValues(x)*FILTER_MULT) + (Accel25psi_xValues(x-1)*FILTER_MULT) + (Accel25psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel25psi_xValues(x-3)*FILTER_MULT) + (Accel25psi_xValues(x-4)*FILTER_MULT);
%         + (Accel25psi_yValues(x-5)*0.1) ;
%         + (Accel25psi_yValues(x-6)*0.1) + (Accel25psi_yValues(x-7)*0.1) + (Accel25psi_yValues(x-8)*0.1) ... 
%         + (Accel25psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel30psi_xValues)
    Accel30psi_xValues(x) = (Accel30psi_xValues(x)*FILTER_MULT) + (Accel30psi_xValues(x-1)*FILTER_MULT) + (Accel30psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel30psi_xValues(x-3)*FILTER_MULT) + (Accel30psi_xValues(x-4)*FILTER_MULT) ;
%         + (Accel30psi_yValues(x-5)*0.1) ;
%         + (Accel30psi_yValues(x-6)*0.1) + (Accel30psi_yValues(x-7)*0.1) + (Accel30psi_yValues(x-8)*0.1) ... 
%         + (Accel30psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel35psi_xValues)
    Accel35psi_xValues(x) = (Accel35psi_xValues(x)*FILTER_MULT) + (Accel35psi_xValues(x-1)*FILTER_MULT) + (Accel35psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel35psi_xValues(x-3)*FILTER_MULT) + (Accel35psi_xValues(x-4)*FILTER_MULT) ;
%         + (Accel35psi_yValues(x-5)*0.1) ;
%         + (Accel35psi_yValues(x-6)*0.1) + (Accel35psi_yValues(x-7)*0.1) + (Accel35psi_yValues(x-8)*0.1) ... 
%         + (Accel35psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel40psi_xValues)
    Accel40psi_xValues(x) = (Accel40psi_xValues(x)*FILTER_MULT) + (Accel40psi_xValues(x-1)*FILTER_MULT) + (Accel40psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel40psi_xValues(x-3)*FILTER_MULT) + (Accel40psi_xValues(x-4)*FILTER_MULT) ;
%     + (Accel40psi_yValues(x-5)*0.1) ...
%         + (Accel40psi_yValues(x-6)*0.1) + (Accel40psi_yValues(x-7)*0.1) ;
%         + (Accel40psi_yValues(x-8)*0.1) ... 
%         + (Accel40psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel45psi_xValues)
    Accel45psi_xValues(x) = (Accel45psi_xValues(x)*FILTER_MULT) + (Accel45psi_xValues(x-1)*FILTER_MULT) + (Accel45psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel45psi_xValues(x-3)*FILTER_MULT) + (Accel45psi_xValues(x-4)*FILTER_MULT); 
%     + (Accel45psi_yValues(x-5)*0.1) ...
%         + (Accel45psi_yValues(x-6)*0.1) + (Accel45psi_yValues(x-7)*0.1) ...
%         + (Accel45psi_yValues(x-8)*0.1) ... 
%         + (Accel45psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel50psi_xValues)
    Accel50psi_xValues(x) = (Accel50psi_xValues(x)*FILTER_MULT) + (Accel50psi_xValues(x-1)*FILTER_MULT) + (Accel50psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel50psi_xValues(x-3)*FILTER_MULT) + (Accel50psi_xValues(x-4)*FILTER_MULT) ;
%     + (Accel50psi_yValues(x-5)*0.1) ...
%         + (Accel50psi_yValues(x-6)*0.1) + (Accel50psi_yValues(x-7)*0.1) ... 
%         + (Accel50psi_yValues(x-8)*0.1) ... 
%         + (Accel50psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel55psi_xValues)
    Accel55psi_xValues(x) = (Accel55psi_xValues(x)*FILTER_MULT) + (Accel55psi_xValues(x-1)*FILTER_MULT) + (Accel55psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel55psi_xValues(x-3)*FILTER_MULT) + (Accel55psi_xValues(x-4)*FILTER_MULT) ;
%     + (Accel55psi_yValues(x-5)*0.1) ...
%         + (Accel55psi_yValues(x-6)*0.1) + (Accel55psi_yValues(x-7)*0.1) ... 
%         + (Accel55psi_yValues(x-8)*0.1) ... 
%         + (Accel55psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel60psi_xValues)
    Accel60psi_xValues(x) = (Accel60psi_xValues(x)*FILTER_MULT) + (Accel60psi_xValues(x-1)*FILTER_MULT) + (Accel60psi_xValues(x-2)*FILTER_MULT) ...
        + (Accel60psi_xValues(x-3)*FILTER_MULT) + (Accel60psi_xValues(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

%now for the y data values

for x = FILTER_LEN:length(Accel15psi_yValues)
    Accel15psi_yValues(x) = (Accel15psi_yValues(x)*FILTER_MULT) + (Accel15psi_yValues(x-1)*FILTER_MULT) + (Accel15psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel15psi_yValues(x-3)*FILTER_MULT) + (Accel15psi_yValues(x-4)*FILTER_MULT); 
% + (Accel15psi_yValues(x-5)*0.1) ...
%         + (Accel15psi_yValues(x-6)*0.1) + (Accel15psi_yValues(x-7)*0.1) + (Accel15psi_yValues(x-8)*0.1) ... 
%         + (Accel15psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel20psi_yValues)
    Accel20psi_yValues(x) = (Accel20psi_yValues(x)*FILTER_MULT) + (Accel20psi_yValues(x-1)*FILTER_MULT) + (Accel20psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel20psi_yValues(x-3)*FILTER_MULT) + (Accel20psi_yValues(x-4)*FILTER_MULT);
%         + (Accel20psi_yValues(x-5)*0.1) ...
%         + (Accel20psi_yValues(x-6)*0.1) + (Accel20psi_yValues(x-7)*0.1) + (Accel20psi_yValues(x-8)*0.1) ... 
%         + (Accel20psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel25psi_yValues)
    Accel25psi_yValues(x) = (Accel25psi_yValues(x)*FILTER_MULT) + (Accel25psi_yValues(x-1)*FILTER_MULT) + (Accel25psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel25psi_yValues(x-3)*FILTER_MULT) + (Accel25psi_yValues(x-4)*FILTER_MULT);
%         + (Accel25psi_yValues(x-5)*0.1) ;
%         + (Accel25psi_yValues(x-6)*0.1) + (Accel25psi_yValues(x-7)*0.1) + (Accel25psi_yValues(x-8)*0.1) ... 
%         + (Accel25psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel30psi_yValues)
    Accel30psi_yValues(x) = (Accel30psi_yValues(x)*FILTER_MULT) + (Accel30psi_yValues(x-1)*FILTER_MULT) + (Accel30psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel30psi_yValues(x-3)*FILTER_MULT) + (Accel30psi_yValues(x-4)*FILTER_MULT) ;
%         + (Accel30psi_yValues(x-5)*0.1) ;
%         + (Accel30psi_yValues(x-6)*0.1) + (Accel30psi_yValues(x-7)*0.1) + (Accel30psi_yValues(x-8)*0.1) ... 
%         + (Accel30psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel35psi_yValues)
    Accel35psi_yValues(x) = (Accel35psi_yValues(x)*FILTER_MULT) + (Accel35psi_yValues(x-1)*FILTER_MULT) + (Accel35psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel35psi_yValues(x-3)*FILTER_MULT) + (Accel35psi_yValues(x-4)*FILTER_MULT) ;
%         + (Accel35psi_yValues(x-5)*0.1) ;
%         + (Accel35psi_yValues(x-6)*0.1) + (Accel35psi_yValues(x-7)*0.1) + (Accel35psi_yValues(x-8)*0.1) ... 
%         + (Accel35psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel40psi_yValues)
    Accel40psi_yValues(x) = (Accel40psi_yValues(x)*FILTER_MULT) + (Accel40psi_yValues(x-1)*FILTER_MULT) + (Accel40psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel40psi_yValues(x-3)*FILTER_MULT) + (Accel40psi_yValues(x-4)*FILTER_MULT) ;
%     + (Accel40psi_yValues(x-5)*0.1) ...
%         + (Accel40psi_yValues(x-6)*0.1) + (Accel40psi_yValues(x-7)*0.1) ;
%         + (Accel40psi_yValues(x-8)*0.1) ... 
%         + (Accel40psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel45psi_yValues)
    Accel45psi_yValues(x) = (Accel45psi_yValues(x)*FILTER_MULT) + (Accel45psi_yValues(x-1)*FILTER_MULT) + (Accel45psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel45psi_yValues(x-3)*FILTER_MULT) + (Accel45psi_yValues(x-4)*FILTER_MULT); 
%     + (Accel45psi_yValues(x-5)*0.1) ...
%         + (Accel45psi_yValues(x-6)*0.1) + (Accel45psi_yValues(x-7)*0.1) ...
%         + (Accel45psi_yValues(x-8)*0.1) ... 
%         + (Accel45psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel50psi_yValues)
    Accel50psi_yValues(x) = (Accel50psi_yValues(x)*FILTER_MULT) + (Accel50psi_yValues(x-1)*FILTER_MULT) + (Accel50psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel50psi_yValues(x-3)*FILTER_MULT) + (Accel50psi_yValues(x-4)*FILTER_MULT) ;
%     + (Accel50psi_yValues(x-5)*0.1) ...
%         + (Accel50psi_yValues(x-6)*0.1) + (Accel50psi_yValues(x-7)*0.1) ... 
%         + (Accel50psi_yValues(x-8)*0.1) ... 
%         + (Accel50psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel55psi_yValues)
    Accel55psi_yValues(x) = (Accel55psi_yValues(x)*FILTER_MULT) + (Accel55psi_yValues(x-1)*FILTER_MULT) + (Accel55psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel55psi_yValues(x-3)*FILTER_MULT) + (Accel55psi_yValues(x-4)*FILTER_MULT) ;
%     + (Accel55psi_yValues(x-5)*0.1) ...
%         + (Accel55psi_yValues(x-6)*0.1) + (Accel55psi_yValues(x-7)*0.1) ... 
%         + (Accel55psi_yValues(x-8)*0.1) ... 
%         + (Accel55psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel60psi_yValues)
    Accel60psi_yValues(x) = (Accel60psi_yValues(x)*FILTER_MULT) + (Accel60psi_yValues(x-1)*FILTER_MULT) + (Accel60psi_yValues(x-2)*FILTER_MULT) ...
        + (Accel60psi_yValues(x-3)*FILTER_MULT) + (Accel60psi_yValues(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

%and z accel data values

for x = FILTER_LEN:length(Accel15psi_zValues)
    Accel15psi_zValues(x) = (Accel15psi_zValues(x)*FILTER_MULT) + (Accel15psi_zValues(x-1)*FILTER_MULT) + (Accel15psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel15psi_zValues(x-3)*FILTER_MULT) + (Accel15psi_zValues(x-4)*FILTER_MULT); 
% + (Accel15psi_yValues(x-5)*0.1) ...
%         + (Accel15psi_yValues(x-6)*0.1) + (Accel15psi_yValues(x-7)*0.1) + (Accel15psi_yValues(x-8)*0.1) ... 
%         + (Accel15psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel20psi_zValues)
    Accel20psi_zValues(x) = (Accel20psi_zValues(x)*FILTER_MULT) + (Accel20psi_zValues(x-1)*FILTER_MULT) + (Accel20psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel20psi_zValues(x-3)*FILTER_MULT) + (Accel20psi_zValues(x-4)*FILTER_MULT);
%         + (Accel20psi_yValues(x-5)*0.1) ...
%         + (Accel20psi_yValues(x-6)*0.1) + (Accel20psi_yValues(x-7)*0.1) + (Accel20psi_yValues(x-8)*0.1) ... 
%         + (Accel20psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel25psi_zValues)
    Accel25psi_zValues(x) = (Accel25psi_zValues(x)*FILTER_MULT) + (Accel25psi_zValues(x-1)*FILTER_MULT) + (Accel25psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel25psi_zValues(x-3)*FILTER_MULT) + (Accel25psi_zValues(x-4)*FILTER_MULT);
%         + (Accel25psi_yValues(x-5)*0.1) ;
%         + (Accel25psi_yValues(x-6)*0.1) + (Accel25psi_yValues(x-7)*0.1) + (Accel25psi_yValues(x-8)*0.1) ... 
%         + (Accel25psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel30psi_zValues)
    Accel30psi_zValues(x) = (Accel30psi_zValues(x)*FILTER_MULT) + (Accel30psi_zValues(x-1)*FILTER_MULT) + (Accel30psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel30psi_zValues(x-3)*FILTER_MULT) + (Accel30psi_zValues(x-4)*FILTER_MULT) ;
%         + (Accel30psi_yValues(x-5)*0.1) ;
%         + (Accel30psi_yValues(x-6)*0.1) + (Accel30psi_yValues(x-7)*0.1) + (Accel30psi_yValues(x-8)*0.1) ... 
%         + (Accel30psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel35psi_zValues)
    Accel35psi_zValues(x) = (Accel35psi_zValues(x)*FILTER_MULT) + (Accel35psi_zValues(x-1)*FILTER_MULT) + (Accel35psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel35psi_zValues(x-3)*FILTER_MULT) + (Accel35psi_zValues(x-4)*FILTER_MULT) ;
%         + (Accel35psi_yValues(x-5)*0.1) ;
%         + (Accel35psi_yValues(x-6)*0.1) + (Accel35psi_yValues(x-7)*0.1) + (Accel35psi_yValues(x-8)*0.1) ... 
%         + (Accel35psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel40psi_zValues)
    Accel40psi_zValues(x) = (Accel40psi_zValues(x)*FILTER_MULT) + (Accel40psi_zValues(x-1)*FILTER_MULT) + (Accel40psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel40psi_zValues(x-3)*FILTER_MULT) + (Accel40psi_zValues(x-4)*FILTER_MULT) ;
%     + (Accel40psi_yValues(x-5)*0.1) ...
%         + (Accel40psi_yValues(x-6)*0.1) + (Accel40psi_yValues(x-7)*0.1) ;
%         + (Accel40psi_yValues(x-8)*0.1) ... 
%         + (Accel40psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel45psi_zValues)
    Accel45psi_zValues(x) = (Accel45psi_zValues(x)*FILTER_MULT) + (Accel45psi_zValues(x-1)*FILTER_MULT) + (Accel45psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel45psi_zValues(x-3)*FILTER_MULT) + (Accel45psi_zValues(x-4)*FILTER_MULT); 
%     + (Accel45psi_yValues(x-5)*0.1) ...
%         + (Accel45psi_yValues(x-6)*0.1) + (Accel45psi_yValues(x-7)*0.1) ...
%         + (Accel45psi_yValues(x-8)*0.1) ... 
%         + (Accel45psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel50psi_zValues)
    Accel50psi_zValues(x) = (Accel50psi_zValues(x)*FILTER_MULT) + (Accel50psi_zValues(x-1)*FILTER_MULT) + (Accel50psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel50psi_zValues(x-3)*FILTER_MULT) + (Accel50psi_zValues(x-4)*FILTER_MULT) ;
%     + (Accel50psi_yValues(x-5)*0.1) ...
%         + (Accel50psi_yValues(x-6)*0.1) + (Accel50psi_yValues(x-7)*0.1) ... 
%         + (Accel50psi_yValues(x-8)*0.1) ... 
%         + (Accel50psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel55psi_zValues)
    Accel55psi_zValues(x) = (Accel55psi_zValues(x)*FILTER_MULT) + (Accel55psi_zValues(x-1)*FILTER_MULT) + (Accel55psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel55psi_zValues(x-3)*FILTER_MULT) + (Accel55psi_zValues(x-4)*FILTER_MULT) ;
%     + (Accel55psi_yValues(x-5)*0.1) ...
%         + (Accel55psi_yValues(x-6)*0.1) + (Accel55psi_yValues(x-7)*0.1) ... 
%         + (Accel55psi_yValues(x-8)*0.1) ... 
%         + (Accel55psi_yValues(x-9)*0.1) ;
end

for x = FILTER_LEN:length(Accel60psi_zValues)
    Accel60psi_zValues(x) = (Accel60psi_zValues(x)*FILTER_MULT) + (Accel60psi_zValues(x-1)*FILTER_MULT) + (Accel60psi_zValues(x-2)*FILTER_MULT) ...
        + (Accel60psi_zValues(x-3)*FILTER_MULT) + (Accel60psi_zValues(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end




%Now filter Lidar data too - actually I found that filtering LIDAR produces
%worse results, probably because it's not as erratic as the accelerometer
%so doesn't need smoothing the same, and FIRing it just removes important
%differentiating information :| 

LIDAR_FILTER_LEN = 4;
LIDAR_FILTER_MULT = 0.25;

for x = LIDAR_FILTER_LEN:length(Lidar15psi_values)
    Lidar15psi_values(x) = (Lidar15psi_values(x)*LIDAR_FILTER_MULT) + (Lidar15psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar15psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar15psi_values(x-3)*LIDAR_FILTER_MULT); % + (Lidar15psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar20psi_values)
    Lidar20psi_values(x) = (Lidar20psi_values(x)*LIDAR_FILTER_MULT) + (Lidar20psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar20psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar20psi_values(x-3)*LIDAR_FILTER_MULT); % + (Lidar20psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar25psi_values)
    Lidar25psi_values(x) = (Lidar25psi_values(x)*LIDAR_FILTER_MULT) + (Lidar25psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar25psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar25psi_values(x-3)*LIDAR_FILTER_MULT) ; % + (Lidar25psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar30psi_values)
    Lidar30psi_values(x) = (Lidar30psi_values(x)*LIDAR_FILTER_MULT) + (Lidar30psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar30psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar30psi_values(x-3)*LIDAR_FILTER_MULT) ; % + (Lidar30psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar35psi_values)
    Lidar35psi_values(x) = (Lidar35psi_values(x)*LIDAR_FILTER_MULT) + (Lidar35psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar35psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar35psi_values(x-3)*LIDAR_FILTER_MULT) ; %+ (Lidar35psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar40psi_values)
    Lidar40psi_values(x) = (Lidar40psi_values(x)*LIDAR_FILTER_MULT) + (Lidar40psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar40psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar40psi_values(x-3)*LIDAR_FILTER_MULT) ; % + (Lidar40psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar45psi_values)
    Lidar45psi_values(x) = (Lidar45psi_values(x)*LIDAR_FILTER_MULT) + (Lidar45psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar45psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar45psi_values(x-3)*LIDAR_FILTER_MULT) ; % + (Lidar45psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar50psi_values)
    Lidar50psi_values(x) = (Lidar50psi_values(x)*LIDAR_FILTER_MULT) + (Lidar50psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar50psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar50psi_values(x-3)*LIDAR_FILTER_MULT) ; % + (Lidar50psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar55psi_values)
    Lidar55psi_values(x) = (Lidar55psi_values(x)*LIDAR_FILTER_MULT) + (Lidar55psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar55psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar55psi_values(x-3)*LIDAR_FILTER_MULT) ; %+ (Lidar55psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

for x = LIDAR_FILTER_LEN:length(Lidar60psi_values)
    Lidar60psi_values(x) = (Lidar60psi_values(x)*LIDAR_FILTER_MULT) + (Lidar60psi_values(x-1)*LIDAR_FILTER_MULT) + (Lidar60psi_values(x-2)*LIDAR_FILTER_MULT) ...
        + (Lidar60psi_values(x-3)*LIDAR_FILTER_MULT) ; % + (Lidar60psi_values(x-4)*FILTER_MULT);
%     + (Accel60psi_yValues(x-5)*0.1) ...
%         + (Accel60psi_yValues(x-6)*0.1) + (Accel60psi_yValues(x-7)*0.1) ... 
%         + (Accel60psi_yValues(x-8)*0.1) ... 
%         + (Accel60psi_yValues(x-9)*0.1) ;
end

%Try short window variance calculations :) 

WINDOW_SIZE = 5

%for x values first....

varholderx15 = [];
numWindows = length(Accel15psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx15(i) = var(Accel15psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx20 = [];
numWindows = length(Accel20psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx20(i) = var(Accel20psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx25 = [];
numWindows = length(Accel25psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx25(i) = var(Accel25psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx30 = [];
numWindows = length(Accel30psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx30(i) = var(Accel30psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx35 = [];
numWindows = length(Accel35psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx35(i) = var(Accel35psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx40 = [];
numWindows = length(Accel40psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx40(i) = var(Accel40psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx45 = [];
numWindows = length(Accel45psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx45(i) = var(Accel45psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx50 = [];
numWindows = length(Accel50psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx50(i) = var(Accel50psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx55 = [];
numWindows = length(Accel55psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx55(i) = var(Accel55psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderx60 = [];
numWindows = length(Accel60psi_xValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderx60(i) = var(Accel60psi_xValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

%now for y data values

varholdery15 = [];
numWindows = length(Accel15psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery15(i) = var(Accel15psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery20 = [];
numWindows = length(Accel20psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery20(i) = var(Accel20psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery25 = [];
numWindows = length(Accel25psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery25(i) = var(Accel25psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery30 = [];
numWindows = length(Accel30psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery30(i) = var(Accel30psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery35 = [];
numWindows = length(Accel35psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery35(i) = var(Accel35psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery40 = [];
numWindows = length(Accel40psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery40(i) = var(Accel40psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery45 = [];
numWindows = length(Accel45psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery45(i) = var(Accel45psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery50 = [];
numWindows = length(Accel50psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery50(i) = var(Accel50psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery55 = [];
numWindows = length(Accel55psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery55(i) = var(Accel55psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholdery60 = [];
numWindows = length(Accel60psi_yValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholdery60(i) = var(Accel60psi_yValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

%now for z data values

varholderz15 = [];
numWindows = length(Accel15psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz15(i) = var(Accel15psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz20 = [];
numWindows = length(Accel20psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz20(i) = var(Accel20psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz25 = [];
numWindows = length(Accel25psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz25(i) = var(Accel25psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz30 = [];
numWindows = length(Accel30psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz30(i) = var(Accel30psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz35 = [];
numWindows = length(Accel35psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz35(i) = var(Accel35psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz40 = [];
numWindows = length(Accel40psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz40(i) = var(Accel40psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz45 = [];
numWindows = length(Accel45psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz45(i) = var(Accel45psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz50 = [];
numWindows = length(Accel50psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz50(i) = var(Accel50psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz55 = [];
numWindows = length(Accel55psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz55(i) = var(Accel55psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

varholderz60 = [];
numWindows = length(Accel60psi_zValues) / WINDOW_SIZE;
lower = 1;
upper = WINDOW_SIZE;
for( i = 1:numWindows)
    varholderz60(i) = var(Accel60psi_zValues(lower:upper));
    lower = lower + WINDOW_SIZE;
    upper = upper + WINDOW_SIZE;
end

% Now for Lidar data values

LIDAR_WINDOW_SIZE = 20

varholderLidar15 = [];
numWindows = length(Lidar15psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar15(i) = var(Lidar15psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar20 = [];
numWindows = length(Lidar20psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar20(i) = var(Lidar20psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar25 = [];
numWindows = length(Lidar25psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar25(i) = var(Lidar25psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar30 = [];
numWindows = length(Lidar30psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar30(i) = var(Lidar30psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar35 = [];
numWindows = length(Lidar35psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar35(i) = var(Lidar35psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar40 = [];
numWindows = length(Lidar40psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar40(i) = var(Lidar40psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar45 = [];
numWindows = length(Lidar45psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar45(i) = var(Lidar45psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar50 = [];
numWindows = length(Lidar50psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar50(i) = var(Lidar50psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar55 = [];
numWindows = length(Lidar55psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar55(i) = var(Lidar55psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

varholderLidar60 = [];
numWindows = length(Lidar60psi_values) / LIDAR_WINDOW_SIZE;
lower = 1;
upper = LIDAR_WINDOW_SIZE;
for( i = 1:numWindows)
    varholderLidar60(i) = var(Lidar60psi_values(lower:upper));
    lower = lower + LIDAR_WINDOW_SIZE;
    upper = upper + LIDAR_WINDOW_SIZE;
end

% title15 = sprintf('short window (%d) variance: 15psi',WINDOW_SIZE);
% figure;stem(varholder15);title(title15);
% title20 = sprintf('short window (%d) variance: 20psi',WINDOW_SIZE);
% figure;stem(varholder20);title(title20);
% title25 = sprintf('short window (%d) variance: 25psi',WINDOW_SIZE);
% figure;stem(varholder25);title(title25);
% title30 = sprintf('short window (%d) variance: 30psi',WINDOW_SIZE);
% figure;stem(varholder30);title(title30);
% title35 = sprintf('short window (%d) variance: 35psi',WINDOW_SIZE);
% figure;stem(varholder35);title(title35);
% title40 = sprintf('short window (%d) variance: 40psi',WINDOW_SIZE);
% figure;stem(varholder40);title(title40);
% title45 = sprintf('short window (%d) variance: 45psi',WINDOW_SIZE);
% figure;stem(varholder45);title(title45);
% title50 = sprintf('short window (%d) variance: 50psi',WINDOW_SIZE);
% figure;stem(varholder50);title(title50);
% title55 = sprintf('short window (%d) variance: 55psi',WINDOW_SIZE);
% figure;stem(varholder55);title(title55);
% title60 = sprintf('short window (%d) variance: 60psi',WINDOW_SIZE);
% figure;stem(varholder60);title(title60);

%Now filter outliers from the variance data, e.g. in Lidar15 there's a
%brief section with crazy outliers which mess up the overall variance
%values.....
% meanOfVarLidar15 = mean(varholderLidar15);
% varholderLidar15(varholderLidar15 > 500) = [];
% 
% meanOfVarLidar20 = mean(varholderLidar20);
% varholderLidar20(varholderLidar20 > 500) = [];
% 
% meanOfVarLidar25 = mean(varholderLidar25);
% varholderLidar25(varholderLidar25 > 500) = [];
% 
% meanOfVarLidar30 = mean(varholderLidar30);
% varholderLidar30(varholderLidar30 > 500) = [];
% 
% meanOfVarLidar35 = mean(varholderLidar35);
% varholderLidar35(varholderLidar35 > 500) = [];
% 
% meanOfVarLidar40 = mean(varholderLidar40);
% varholderLidar40(varholderLidar40 > 500) = [];
% 
% meanOfVarLidar45 = mean(varholderLidar45);
% varholderLidar45(varholderLidar45 > 500) = [];
% 
% meanOfVarLidar50 = mean(varholderLidar50);
% varholderLidar50(varholderLidar50 > 500) = [];
% 
% meanOfVarLidar55 = mean(varholderLidar55);
% varholderLidar55(varholderLidar55 > 500) = [];
% 
% meanOfVarLidar60 = mean(varholderLidar60);
% varholderLidar60(varholderLidar60 > 500) = [];

% meanOfVarLidar15 = mean(varholderLidar15)
% meanOfVarLidar60 = mean(varholderLidar60)
% varholderLidar15( varholderLidar15 > (meanOfVarLidar15 * 20) ) = [] %filter out large outliers > mean * 20
% varholderLidar60( varholderLidar60 > (meanOfVarLidar60 * 20) ) = [] %filter out large outliers > mean * 20

meanvarholdersx = [ mean(varholderx15) mean(varholderx20) mean(varholderx25) mean(varholderx30) mean(varholderx35) ...
    mean(varholderx40) mean(varholderx45) mean(varholderx50) mean(varholderx55) ...
    mean(varholderx60)]

modevarholdersx = [ mode(varholderx15) mode(varholderx20) mode(varholderx25) mode(varholderx30) mode(varholderx35) ...
     mean(varholderx40) mean(varholderx45) mean(varholderx50) mean(varholderx55) ...
    mean(varholderx60)]

meanvarholdersy = [ mean(varholdery15) mean(varholdery20) mean(varholdery25) mean(varholdery30) mean(varholdery35) ...
    mean(varholdery40) mean(varholdery45) mean(varholdery50) mean(varholdery55) ...
    mean(varholdery60)]

modevarholdersy = [ mode(varholdery15) mode(varholdery20) mode(varholdery25) mode(varholdery30) mode(varholdery35) ...
     mean(varholdery40) mean(varholdery45) mean(varholdery50) mean(varholdery55) ...
    mean(varholdery60)]

meanvarholdersz = [ mean(varholderz15) mean(varholderz20) mean(varholderz25) mean(varholderz30) mean(varholderz35) ...
    mean(varholderz40) mean(varholderz45) mean(varholderz50) mean(varholderz55) ...
    mean(varholderz60)]

modevarholdersz = [ mode(varholderz15) mode(varholderz20) mode(varholderz25) mode(varholderz30) mode(varholderz35) ...
     mean(varholderz40) mean(varholderz45) mean(varholderz50) mean(varholderz55) ...
    mean(varholderz60)]

meanvarholderLidar = [  mean(varholderLidar15) mean(varholderLidar20) mean(varholderLidar25) mean(varholderLidar30) ... 
    mean(varholderLidar35)  mean(varholderLidar40) mean(varholderLidar45) mean(varholderLidar50) mean(varholderLidar55) mean(varholderLidar60) ]

modevarholderLidar = [  mode(varholderLidar15) mode(varholderLidar20) mode(varholderLidar25) mode(varholderLidar30) ... 
    mode(varholderLidar35)  mode(varholderLidar40) mode(varholderLidar45) mode(varholderLidar50) mode(varholderLidar55) mode(varholderLidar60) ]

normalisedModeVarX = modevarholdersx / max(modevarholdersx)
normalisedModeVarY = modevarholdersy / max(modevarholdersy)
normalisedModeVarZ = modevarholdersz / max(modevarholdersz)
normalisedModeVarLidar = modevarholderLidar / max(modevarholderLidar)

sensorFusionModel = normalisedModeVarX + normalisedModeVarY + normalisedModeVarLidar

normalisedSensorFusionModel = sensorFusionModel / max(sensorFusionModel)


