function [trise,tset] = horizoncrossings(t,p,obslocation,elevation)

t1 = t(1);

% Create an anonymous function which calls the function satellitefix
elvfun = @(t) satellitefix(t1+t,p,obslocation);

% Get numeric duration from times
% (need numeric representation for calculation)
tnum = days(t - t1);

% Use the elevations to find when the satellite is rising over horizon
n = length(elevation);

% Use logic to see when elevation is positive (satellite is up)
up = elevation > 0;
up1 = up(1:(n-1));  % up at time t(k)
up2 = up(2:n);      % up at time t(k+1)

% Get risings (= wasn't up at t(k), but was up at t(k+1))
idx = find(~up1 & up2);
n = numel(idx);
trise = zeros(n,1);  % preallocate space for array

% Step through times to get exact time in each interval
for k = 1:n
    % Find where in that interval the sign change occured    
    trise(k) = fzero(elvfun,tnum(idx(k):(idx(k)+1)));    
end

% Now settings (= up at t(k), not up at t(k+1))
idx = find(up1 & ~up2);
n = numel(idx);
tset = zeros(n,1);
for k = 1:n
    tset(k) = fzero(elvfun,tnum(idx(k):(idx(k)+1)));
end

% Convert rise/set times back to actual dates (from numeric)
trise = t(1) + days(trise);
tset = t(1) + days(tset);

end

