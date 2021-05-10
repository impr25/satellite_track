# First function to read parameters from settelite files 

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

# <<<<<< Test case 1. >>>>>>

#print(readparameters('iss.txt'))