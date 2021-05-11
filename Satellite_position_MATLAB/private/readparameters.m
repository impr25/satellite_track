function p = readparameters(fname)
% Creates a structure of orbital parameters read from file
%
% P = READPARAMETERS(FILE) reads the two-line element set (TLE) file FILE
% (string) and returns a structure P containing the epoch [datetime],
% inclination [degrees], RA of the ascending node [degrees], eccentricity
% [number], argument of perigee [degrees], mean anomaly [degrees], and mean
% motion [revolutions/day]. All angles are given as scalar numbers.

% Get raw text from file; split into two lines
txt = strsplit(fileread(fname),'\n');

% Extract epoch year
ey = str2double(txt{1}(19:20));

% Convert 2-digit epoch year to 4-digit year
% (00-60 -> 2000-2060, 61-99 -> 1961-1999)
ey = 1900 + ey + 100*(ey < 60);
% Extract epoch day
ed = str2double(txt{1}(21:32));
disp(ed);
% Build output structure
p.epoch = datetime(ey,1,1) + days(ed - 1);

p.inclination = str2double(txt{2}(9:16));
p.RAAN = str2double(txt{2}(18:25));
p.eccentricity = str2double(['0.',txt{2}(27:33)]);
p.argPerigee = str2double(txt{2}(35:42));
p.anomaly = str2double(txt{2}(44:51));
p.motion = str2double(txt{2}(53:63));
