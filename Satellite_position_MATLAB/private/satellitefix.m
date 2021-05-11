function [el,az,satlat,satlon,r] = satellitefix(t,p,obsloc)
% Determines local azimuth and elevation of a satellite at given times
%
% [EL,AZ] = SATELLITEFIX(T,PARAMS,OBS) calculates the elevation (EL), in
% degrees from horizontal, and azimuth (AZ), in degrees from North, of a
% satellite defined by the orbital parameters in the structure PARAMS for
% each time in the datetime array T, as observed from a position specified
% in the 3-element vector OBS, representing the observer's latitude [deg],
% longitude [deg], and altitude [km].
%
% [EL,AZ,LAT,LON,R] = SATELLITEFIX(...) also returns the location of the
% satellite in terms of latitude (LAT), longitude (LON), in Earth-centered
% fixed coordinates, and radius R (in km from the center of the Earth).

% Extract the location components
lat = obsloc(1);
lon = obsloc(2);
alt = obsloc(3);

% cos(phi) and sin(phi) -- used a few times
cp = cosd(lat);
sp = sind(lat);

% Get satellite position in Earth coordinates (lat/lon/r)
[satlat,satlon,r] = satelliteposition(t,p);
% Convert to Cartesian
xsat = r.*cosd(satlon).*cosd(satlat);
ysat = r.*sind(satlon).*cosd(satlat);
zsat = r.*sind(satlat);

% Observer's radial distance
robs = 1/sqrt((cp/6378.135)^2 + (sp/6356.752)^2) + alt;
% Convert to Cartesian coordinates
xobs = robs*cosd(lon)*cosd(lat);
yobs = robs*sind(lon)*cosd(lat);
zobs = robs*sind(lat);

% Difference between satellite location and observer
dx = xsat - xobs;
dy = ysat - yobs;
dz = zsat - zobs;

% Convert to local (Cartesian) coordinates
st = sind(lon);
ct = cosd(lon);
xt = sp*ct*dx + sp*st*dy - cp*dz;
yt = ct*dy - st*dx;
zt = cp*ct*dx + cp*st*dy + sp*dz;

% Convert to az/el
az = mod(180*atan2(yt,-xt)/pi,360);
zt = zt./sqrt(xt.*xt+yt.*yt+zt.*zt);  % normalize (unit vector)
el = asind(zt);
