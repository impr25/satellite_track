import numpy as np 
from scipy import optimize
import math as m
from satellitefix import*
from datetime import datetime, timedelta 

def num_to_dur(t):
	a = []
	#print(t)
	for t1 in t:
		a.append(timedelta(days=t1[0]))
	dt = np.array(a)
	return dt

def horizoncrossings(t,p,obslocation,elevation):
	t1 = [t[0]]
	t1 = np.array(t1)
	
	#elvfun = lambda x : satellitefix(t1+x,p,obslocation)
	def elvfun(t12) :
		#print('done 1')
		#print(t12)
		z = []
		for i in t12:
			z.append(timedelta(days=i))
		t12 = np.array(z)
		x = t1 + t12
		ans =  satellitefix(x,p,obslocation)
		#print('done 2')
		return ans[0]
	#.......NOTE........
	#....Here one days(t - t1) is used in matlab code 
	dt = t - t1
	dt = dt.astype("timedelta64[s]").astype(float)
	dt = dt/(24*3600)
	tnum = dt

	n = len(elevation)

	up = elevation>0
	
	up1 = up[:n]
	up2 = up[1:]
	idx1 = np.argwhere(up2)
	idx2 = np.argwhere(~up1)
	idx = np.intersect1d(idx1,idx2)
	
	n = len(idx)
	trise = np.zeros([n,1])
	
	for k in range(n):

		# Finding Zeros of above lambda function 
		# Finding Zeros of above lambda function
		# Finding Zeros of above lambda function
		x0 = np.array(tnum[idx[k]:idx[k]+2])
		sol1 = optimize.root(elvfun, x0)
		#print('Solution ...........',sol1.x)
		trise[k] = np.mean(sol1.x)

	idx1 = np.argwhere(~up2)
	idx2 = np.argwhere(up1)
	idx = np.intersect1d(idx1,idx2)
	n = len(idx)
	tset= np.zeros([n,1])

	for k in range(n):

		# Finding Zeros of above lambda function 
		# Finding Zeros of above lambda function
		# Finding Zeros of above lambda function
		x0 = np.array(tnum[idx[k]:idx[k]+2])
		sol2 = optimize.root(elvfun, x0)
		#print('Solution ...........',sol2.x)
		tset[k] = np.mean(sol2.x)

	

	trise = t[0] + num_to_dur(trise) 
	tset = t[0] + num_to_dur(tset)


	return [trise,tset]

# >>>>>>>Test Case.1<<<<<<<<....

# p = {'epoch':parser.parse('25-May-2020 12:15:01'),
# 'inclination':51.640600000000000,
# 'RAAN':1.007144000000000e+02,
# 'eccentricity':1.800000000000000e-04,
# 'argPerigee':3.491600000000000e+02,
# 'anomaly':10.951100000000000,
# 'motion':15.493703930000000}

# #..........t1 list has to be coppied from test_case.txt.............

# t1 = list(map(parser.parse, t1))
# t2 = np.array(t1)
# obs_loc = [28.7000000000000,77.1000000000000,0]

# #..........elv list has to be coppied from elv_test.txt.............

# elv = np.array(elv)
# [a,b] = horizoncrossings(t2,p,obs_loc,elv)
# print(a[:3],b[:3])
