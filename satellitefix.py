import math as m 
from satelliteposition import*
import numpy as np 

def satellitefix(t,p,obs_loc):

	# Location of Observer 
	lat = obs_loc[0]
	lon = obs_loc[1]
	alt = obs_loc[2]
	rd = 180/np.pi
	
	cp = m.cos(lat/rd)
	sp = m.sin(lat/rd)

	#print(lat,lon,alt,cp,sp)

	#satellite position in earth coordinates
	[satlat,satlon,r] = satelliteposition(t,p)

	xsat = r*np.cos(satlon/rd)*np.cos(satlat/rd)
	ysat = r*np.sin(satlon/rd)*np.cos(satlat/rd)
	zsat = r*np.sin(satlat/rd)

	# Observer's radial distance
	robs = 1/np.sqrt(((cp/6378.135)**2) + (sp/6356.752)**2) + alt
	# % Convert to Cartesian coordinates
	xobs = robs*m.cos(lon/rd)*m.cos(lat/rd)
	yobs = robs*m.sin(lon/rd)*m.cos(lat/rd)
	zobs = robs*m.sin(lat/rd)

	# Difference between satellite location and observer 
	dx = xsat - xobs
	dy = ysat - yobs
	dz = zsat - zobs

	# Convert to local (catesian) coordinates
	st = m.sin(lon/rd)
	ct = m.cos(lon/rd)
	xt = sp*ct*dx + sp*st*dy - cp*dz
	yt = ct*dy - st*dx
	zt = cp*ct*dx + cp*st*dy +sp*dz

	# Convertto az/el
	az = (180*np.arctan2(yt,-xt)/m.pi)%360 
	zt = zt/np.sqrt(xt*xt + yt*yt + zt*zt)
	el = np.arcsin(zt)*rd
	return [el,az,satlat,satlon,r]

# <<<<Test Case 1. >>>>

# p = {'epoch':parser.parse('25-May-2020 12:15:01'),
# 'inclination':51.640600000000000,
# 'RAAN':1.007144000000000e+02,
# 'eccentricity':1.800000000000000e-04,
# 'argPerigee':3.491600000000000e+02,
# 'anomaly':10.951100000000000,
# 'motion':15.493703930000000}

# #..........t1 list has to be added from test_case.txt.............

# t1 = list(map(parser.parse, t1))
# t2 = np.array(t1)
# obs_loc = [28.7000000000000,77.1000000000000,0]
# [a,b,c,d,e] = satellitefix(t2,p,obs_loc)
# print(a[:3],b[:3])