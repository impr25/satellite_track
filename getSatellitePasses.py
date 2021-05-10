#import readparameters as rdp 
#import plotpos as plts
import horizoncrossings as hzc
import satellitefix as stfx
import matplotlib.pyplot as plt 
import h5py as h5
import numpy as np 
import pandas as pd
import dateutil.parser as parser
from datetime import datetime, timedelta

def readparameters(fname):
	p = dict()
	fh = open(fname)
	txt = fh.read()
	lines = txt.split('\n')
	# Year Extraction 
	ey = int(lines[0][18:20])
	ey = 1900 +ey +100*int(ey<60)
	# Day Exraction
	ed = float(lines[0][20:32])
	#print(ed) 
	#print(ey)
	#print(datetime(ey,1,1)+timedelta(days=ed))


	# Date time Convertion of ey and ed 
	p['epoch'] = datetime(ey,1,1)+timedelta(days=ed)
	p['inclination'] = float(lines[1][8:16])
	p['RAAN'] = float(lines[1][17:25])
	p['eccentricity'] = float('0.'+lines[1][26:33])
	p['argPerigee'] = float(lines[1][34:42])
	p['anomaly'] = float(lines[1][43:51])
	p['motion'] = float(lines[1][52:63])
	fh.close()
	return p

def getSatellitePasses(day,TZ,tspan,dt,files,obsloc):
	##..Day format should be '25-may-2020' like this ....
	##..TZ should be list like [-5,30] it TimeZone value for that position 
	##..tspan should be a number showing no. of days for analysis
	##..dt shold be a number for minutes showing iteration time for analysis
	##..files is a list of file names of 2LE details of satellites like ['iss.txt','iss.txt']

	day = parser.parse(day)
	if TZ[0]<0:
		a = -1
		h = int(np.absolute(TZ[0]))
	m = TZ[1]
	time_zone = timedelta(hours=h,minutes=m)
	day = day + a*time_zone
	dt = timedelta(minutes=dt)
	t = day + np.arange(tspan*24*60)*timedelta(minutes=1)
	satellite = dict()
	for k in range(len(files)):
		p = readparameters(files[k])

		[el,az,satlat,satlon,r] = stfx.satellitefix(t,p,obsloc)
		dict1 = {'satlat':satlat,'satlon':satlon}
		##...Start a panadas dataframe for staring the table with 0,1,2 indexes
		#pos = table(el,az,lat,lon,t,'VariableNames',...
        #{'Elevation','Azimuth','Latitude','Longitude','Time'});
		df = pd.DataFrame(data = dict1)
		
		[trise,tset] = hzc.horizoncrossings(t,p,obsloc,el)
		if el[0]>0:
			trise = [t[0]] + trise
		if el[-1]>0:
			tset = tset + [tset[-1]]

		fig, ax1= plt.subplots()
		n = len(trise)
		passes = dict()
		fh = h5.File('map.mat','r')
		#print(fh.keys())
		#print(type(fh))
		map1 = {}
		for k,v in fh.items():
			map1[k] = v
		ax1.plot(map1['lon'][0],map1['lat'][0], 'k')
		ax1.plot(obsloc[0],obsloc[1],'go')
		for j in range(n):

			idx = (t >= trise[j]) & (t <= tset[j])
			pass_pos = df.iloc[idx]
			lat = pass_pos['satlat'].to_numpy()
			lon = pass_pos['satlon'].to_numpy()

			idx = np.concatenate((np.array([0]),np.cumsum(1+(np.absolute(np.diff(lon))>180))))
			mlon = np.empty((idx[-1]+1))
			mlon[:] = np.NaN
			mlat = np.empty((idx[-1]+1))
			mlat[:] = np.NaN

			mlon[idx] = lon
			mlat[idx] = lat
			time_r = t[0] + timedelta(minutes=int(pass_pos.index[0]))
			#fig = plt.figure()   
			#....This should be strted at get setallite passes function
			#plt.plot(map1['lon'][0],map1['lat'][0], 'k')
			ax1.plot(mlon,mlat,'.-', label=str(time_r)+'start time of the View')
			ax1.legend()
			fh.close()
			#plts.plotpos(pass_pos['satlat'].to_numpy(),pass_pos['satlon'].to_numpy())
		plt.show()


day = '7-Sept-2020'
files = ['iss.txt']
obsloc = [28.70, 77.10, 0]
dt = 1
tspan = 1
timezone1 = [-5,30]
getSatellitePasses(day,timezone1,tspan,dt,files,obsloc)

