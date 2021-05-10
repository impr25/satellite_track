'''
import numpy as np 
import math as m

dists = np.arange(0,10,.5)
print(dists)
x = np.array([1,5,2,6,3,12,9,7,1,8])
print(x)
print((x<4) & (x==1))
print((x>8) & (dists>5))

'''

from datetime import datetime, timedelta
import numpy as np 
import math as mt
import dateutil.parser as parser

t1 = ['07-Aug-2020 18:30:00','07-Aug-2020 18:31:00','07-Aug-2020 18:32:00','07-Aug-2020 18:33:00','07-Aug-2020 18:34:00','07-Aug-2020 18:35:00','07-Aug-2020 18:36:00','07-Aug-2020 18:37:00']
t = np.empty((len(t1),1))
t1 = list(map(parser.parse, t1))
t = np.array(t1)

print(t[:2])

def asd():
	a=[1,2,3,5]
	b=[2,5,8,6,9]
	return [a,b]
z = asd()
print(z[0])
z = '2020-Aug-18'
z = parser.parse(z)
print(z)
a = -1
time_zone = timedelta(hours=5,minutes=30)
print(time_zone)
z = z + a* time_zone
print(z)

dt = timedelta(minutes=1)
tspan = timedelta(days=1)
x = z + np.arange(1440)*dt
print(x[:5])
a=[1,2,3,5]
print(any(a))
a = np.identity(6)
print(a.shape[0])

'''
xcv =24234
print("SERVER SIMULATION STEP APPROXIMATION: " 
              ,str(xcv))


print('........................')

a = parser.parse('25-May-2020 12:15:01')
print(a)
print(type(a))
print('...........................')


startDate = datetime(2019,1,1) + timedelta(days=100)
EndDate = datetime(2020,1,1) + timedelta(days=146.5104)
print(type(EndDate))
print(EndDate)

date_list = EndDate + np.arange(20) * timedelta(hours=1,minutes=45)
#date_list = [EndDate + timedelta(minutes=x) for x in range(1,20)]
print(date_list)
#print(type(date_list))
dt = (date_list-startDate)
print(dt) 
dt = dt.astype("timedelta64[s]").astype(float)
dt = dt/(24*3600)
print(type(dt[1]))
print(dt) 
print(10*dt)
dt2 = []
for i in dt:
	#a = i.item()
	#print(type(a))
	#print(timedelta(days=a))
	dt2.append(timedelta(days=i))
	#j += 1
dt2 = np.array(dt2)
print(dt2)
dt1 = EndDate +dt2
print(dt1)
#print(m.floor(dt[1]))
'''

'''

import numpy as np 
a = np.arange(10)
b = np.random.randint(0, 20, 10)
asd = b>4
print(b,asd)
a1 = np.argwhere(~asd)
a2 = np.argwhere(a>3)
print(a1)
print(a2)
print(np.intersect1d(a1,a2))
'''