import numpy as np 
import matplotlib.pyplot as plt 
import h5py as h5


def plotpos(lat,lon):
	fh = h5.File('map.mat','r')
	print(fh.keys())
	print(type(fh))
	map1 = {}
	for k,v in fh.items():
		map1[k] = v

	#print(map1)
	#print(map1['lat'][0])
	#print(type(map1['lat'][0]))

	idx = np.concatenate((np.array([0]),np.cumsum(1+(np.absolute(np.diff(lon))>180))))
	mlon = np.empty((idx[-1]+1))
	mlon[:] = np.NaN
	mlat = np.empty((idx[-1]+1))
	mlat[:] = np.NaN

	mlon[idx] = lon
	mlat[idx] = lat


	fig = plt.figure()    #....This should be strted at get setallite passes function

	plt.plot(map1['lon'][0],map1['lat'][0], 'k')
	plt.plot(mlon,mlat,'.-')

	plt.show()
	fh.close()

# <<<<<< Test Case 1.>>>>>>

#lat1 = [10.7541734509934,13.7475847086974,16.7147046145721,19.6486516092179,22.5418261208228,25.3857354388994,28.1707974724688,30.8861229598178,33.5192789522361,36.0560419328958,38.4801577880765]
#lon1 = [69.1743772264005,71.4394457876360,73.7694376763162,76.1805929580455,78.6903103256323,81.3173278616715,84.0818624097236,87.0056744000002,90.1120076427424,93.4253308948353,96.9707807390610]
#idx1 = [1,2,3,4,5,6,7,8,9,10,11]
#mlat1 = [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN]
#mlon1 = [NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN]
#mlat2 = [10.7541734509934,13.7475847086974,16.7147046145721,19.6486516092179,22.5418261208228,25.3857354388994,28.1707974724688,30.8861229598178,33.5192789522361,36.0560419328958,38.4801577880765]
#mlon2 = [69.1743772264005,71.4394457876360,73.7694376763162,76.1805929580455,78.6903103256323,81.3173278616715,84.0818624097236,87.0056744000002,90.1120076427424,93.4253308948353,96.9707807390610]

#plotpos(lat1,lon1)