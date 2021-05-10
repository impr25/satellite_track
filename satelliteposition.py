import math as m
from datetime import datetime, timedelta 
import numpy as np
import dateutil.parser as parser
from numpy import linalg as LA

def precession(a,e,inc,ndt,aW,w):
	rd = 180/np.pi
	aE = 1
	a1 = a/6378.135
	J2 = 1.082616e-3
	d1 = (3*J2*(aE**2)*(3*np.cos(inc/rd)**2 - 1))/(4*a1**2*(1-e**2)**(3/2))
	a0 = -a1*(134*d1**3/81 + d1**2 + d1/3 - 1)
	p0 = a0*(1-e**2)
	aWt = aW + 360*(-3*J2*aE**2*ndt*np.cos(inc/rd) / (2*p0**2))
	wt = w + 360*(3*J2*aE**2*ndt*(5*np.cos(inc/rd)**2 - 1)/(4*p0**2))
	return [aWt,wt]


def siderealtime(t,lon):

	#.......NOTE........
	#Here one days(t - satparams.epoch) is used in matlab code 
	D = t - datetime(2000,1,1,12,0,0)
	D = D.astype("timedelta64[s]").astype(float)
	D = D/(24*3600)
	GMST = (18.697374558 + 24.06570982441908*D)%24
	LST = (GMST + 1.0027379*lon/15)%24
	return LST


def satelliteposition(t,satparams):
	inc = satparams['inclination']
	e = satparams['eccentricity']
	n = satparams['motion']

	a = (2.975541313977700*10**15/(2*np.pi*n)**2)**(1/3)

	rd = 180/np.pi

	#.......NOTE........ 
	#....Here t is an numpy array 
	#.......NOTE........
	#....Here one days(t - satparams.epoch) is used in matlab code 
	dt = t - satparams['epoch']
	#print(dt[:3])
	dt = dt.astype("timedelta64[s]").astype(np.float64)
	#print(dt[:3])
	dt = dt/float(24*3600)
	#print(dt[:3])
	ndt = n*dt 
	#print(dt[:3])
	
	M = ((satparams['anomaly']+360*(ndt-np.floor(ndt)))%360)/rd
	E = M
	f = e*np.sin(E) +M
	while LA.norm(E-f)>10**(-6):
		E = f
		f = e*np.sin(E) +M
	nu = 2*rd*np.arctan2(np.sqrt((1+e)/(1-e))*np.sin(E/2),np.cos(E/2))

	[aWt,wt] = precession(a,e,inc,ndt,satparams['RAAN'],satparams['argPerigee'])

	mu = (wt+nu)%360
	#print('.............',mu[:4],'.........')
	Da = rd*np.arccos(np.cos(mu/rd)/np.sqrt(1-np.sin(inc/rd)**2*np.sin(mu/rd)**2))
	#print('..........',Da[:4],'........')
	idx = ((inc < 90) & (mu > 180)) | ((90 < inc) & (180 > mu))
	Da[idx] = 360 - Da[idx]

	ag = (aWt+Da)%360
	dg = np.sign(np.sin(mu/rd))*rd*(np.arccos(np.cos(mu/rd)/np.cos(Da/rd)))
	zxc = np.cos(mu/rd)/np.cos(Da/rd)
	#print(zxc[:4])
	#print('.........',len(dg),'........')
	r = a*(1-e**2)/(1+e*np.cos(nu/rd))
	lat = dg
	lon = (ag-15*siderealtime(t,0)+180)%360-180

	return [lat,lon,r] 

# <<<<<Test Case 1. >>>>>

# satparams1 = {'epoch':parser.parse('25-May-2020 12:15:01'),
# 'inclination':51.640600000000000,
# 'RAAN':1.007144000000000e+02,
# 'eccentricity':1.800000000000000e-04,
# 'argPerigee':3.491600000000000e+02,
# 'anomaly':10.951100000000000,
# 'motion':15.493703930000000}

# # ..........t1 list has to be added from test_case.txt.............

# t1 = list(map(parser.parse, t1))
# t2 = np.array(t1)
# [lat,lon,r] = satelliteposition(t2,satparams1)
# print(lat[:2])
# print(r[:2])