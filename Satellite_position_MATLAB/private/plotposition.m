function plotposition(lat,lon)
% Draws latitude/longitude position on a map of the Earth
%
% PLOTPOSITION(LAT,LON) plots a map of Earth overlayed with the position of
% an object defined by the latitudes and longitudes in the vectors LAT and
% LON.

% Insert NaNs between points where longitudes wrap around +/- 180
% Create a vector of indices that increase by 2 (instead of 1) whereever
% the wrapping occurs. Wrapping is detected as a difference of more than
% 180 degrees in consecutive elements.
idx = [1;cumsum(1 + (abs(diff(lon))>180))+1];

% Make vectors of all NaNs
mlon = NaN(idx(end),1);
mlat = NaN(idx(end),1);
% Then overwrite with the data. NaNs will remain whereever the indices jump
% (i.e., where the wrapping occurs).
mlon(idx) = lon;
mlat(idx) = lat;

% Check if there is already a map in the current figure window
if isempty(findobj(gcf,'Tag','satelliteTracker:earthMap'))
    % If not, get the Earth map from file & plot it
    map = load('map');
    plot(map.lon,map.lat,'k','Tag','satelliteTracker:earthMap')
end
% Add the object position
hold on
plot(mlon,mlat,'.-')
% Clean up axes
axis equal
xlim([-180,180])
ylim([-90,90])
hold off
