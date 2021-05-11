function satellite = getSatellitePasses(day,tspan,dt,files,obsloc)
% Generate paths of satellites while they are visible during a given timespan
%
% SATELLITE = getSatellitePasses(DAY,TSPAN,DT,FILELIST,OBS) generates the
% paths for the satellites defined by the orbital paraemeters in the TLE
% files in FILELIST between the times starting on a given DAY and ending at
% DAY+TSPAN, to within a resolution of DT., as seen by an observer located
% at OBS.
%
% DAY can be specified as a datetime, a string, or a vector that can be
% interpreted as a datetime (i.e., [Y,M,D]). The midnight of the DAY
% represents the starting of the timespan. FILELIST should be a cell array
% of strings containing file names. OBS is a numeric vector with three
% elements: latitude [deg], longitude [deg], and altitude [km]. 
%
% The output, SATELLITE, is a structure array where each element
% corresponds to a different satellite. The structure fields are: FILENAME,
% a string containing the file name; NUMPASSES, a scalar representing the
% number of visible passes during the given day; and PASSES, a cell array
% containing NUMPASSES cells. Each cell of PASSES contains a table with
% variables TIME, ELEVATION, AZIMUTH, LATITUDE, and LONGITUDE, recording
% the position of the satellite at each time step.

% Process inputs
day = datetime(day);
day = dateshift(day,'start','day');
if isempty(day.TimeZone)
    day.TimeZone = 'local';
end
day = day - tzoffset(day);
day.TimeZone = '';
t = (day:dt:(day+tspan))';


% Compute daily passes

% Loop over each satellite
satellite = struct;
for k = 1:length(files)
    p = readparameters(files{k});

    % ...........In Python file it will give p as dictionary 

    % Satellite positions over time
    [el,az,lat,lon] = satellitefix(t,p,obsloc);
	pos = table(el,az,lat,lon,t,'VariableNames',...
        {'Elevation','Azimuth','Latitude','Longitude','Time'});
    
    % Satellite rise/set times
    [trise,tset] = horizoncrossings(t,p,obsloc,el);  
    if (el(1) > 0)
        trise = [t(1);trise]; %#ok<AGROW>
    end
    if (el(end) > 0)
        tset = [tset;t(end)]; %#ok<AGROW>
    ending
    
    % Loop over each pass (rise -> set)
    figure    
    n = length(trise);
    passes = {};
    for j = 1:n
        % Extract portion of the path for this satellite pass
        idx = (t >= trise(j)) & (t <= tset(j));   
        
        % Get satellite positions during pass
        pass_pos = pos(idx,:);
        
        %Plot satellite positions during pass
        plotposition(pass_pos.Latitude,pass_pos.Longitude)      
                
        %Collect the satellite passes together
        passes{j} = pass_pos;
    end 
    
    % Group satellite passes with satellite info
    satellite(k).filename = files{k};
    satellite(k).numpasses = n;
    satellite(k).passes = passes;
end