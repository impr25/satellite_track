'''
import math 
from scipy.optimize import fsolve
import numpy as np 

fun = lambda x : np.cos(2*x)
a = np.array([-1,1])
x = fsolve(fun,a)
print(x)
print(fun(x))
z = [1,23,4,6,121,34,9,7,5]
print(z)
a = np.array([z[:3]])
b = np.array(z[:3])
print(a)
print(b)
a = [1,3,5]
b = [1,6,8]
for k in range(3):
	print(z[a[k]:b[k]])
def fun():
	z = [1,23,4,6,121,34,9,7,5]
	return [z[:3],z[3:6]]
a ,b = fun()
print(a,'    ',b)

'''

import numpy as np 
import matplotlib.pyplot as plt 
import h5py as h5

fh = h5.File('map.mat','r')
print(fh.keys())
print(type(fh))
map1 = {}
for k,v in fh.items():
	map1[k] = v
#print(map1)
print(map1['lat'][0])
print(type(map1['lat'][0]))
print('change made in the vs code')
#fig = plt.figure()
#ax = plt.axes()
#x = np.linspace(0,3,40)
#print(x)
#plt.plot(map1['lon'][0],map1['lat'][0], 'k')
#plt.show()

fh.close()
lon1 = [69.1743772264005,71.4394457876360,73.7694376763162,76.1805929580455,78.6903103256323,81.3173278616715,84.0818624097236,87.0056744000002,90.1120076427424,93.4253308948353,96.9707807390610]

idx1 = [1,2,3,4,5,6,7,8,9,10,11]
idx2 = np.concatenate((np.array([0]),np.cumsum(1+(np.absolute(np.diff(lon1))>180))))
mlon = np.empty((idx2[-1]+1))
mlon[:] = np.NaN
print(idx2)
print(mlon)
mlon[idx2] = lon1
print(mlon)




