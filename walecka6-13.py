# walecka6-13.py
# Emma Rice
# 2/25/2020

import numpy as np 
import matplotlib.pyplot as plt

def j1(x):
	j = np.sin(x)/x**2 - np.cos(x)/x
	return j

def F(qR):
	Z = 1
	F = 3*Z*j1(qR)/(qR)
	return F
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

QR = []
Flist = []
for qR in my_range(0.00001, 20.00001,0.0001):
	QR.append(qR)
	Flist.append(F(qR))

fig, ax = plt.subplots(1,1)
ax.plot(QR,Flist, 'r--',label='form factor of uniformly charged sphere') 
ax.set_xlim(0,20)
ax.set_ylim(-.2,2)
ax.set_xlabel('qR')
ax.set_ylabel('F')
ax.set_yscale('log')
fig.savefig('walecka6-13.png',format='PNG') 
