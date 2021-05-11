%% Analysis of satellite passes
day = [2020 06 02];
files = {'iss.txt','iss.txt'};
obsloc = [28.70 77.10 0];
dt = minutes(1);
tspan = days(1);
satellite = getSatellitePasses(day,tspan,dt,files,obsloc);

%% Total number of satellite passes over all satellites
totalNumPasses = sum([satellite.numpasses]);

%% Mean latitude, longitude, elevation of all satellites
allPasses = [satellite.passes];
allPassPositions = cat(1,allPasses{:});
meanLat = mean(allPassPositions.Latitude);
meanLon = mean(allPassPositions.Longitude);
meanEl = mean(allPassPositions.Elevation);

%% Maximum elevation of each pass
cellfun(@(x) max(x.Elevation), allPasses)

%% Conversions
satelliteTable = struct2table(satellite);
sum(satelliteTable.numpasses)
