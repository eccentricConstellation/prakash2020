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
Flistabs = []
for qR in my_range(0.00001, 20.00001,0.000001):
	QR.append(qR)
	Flist.append(F(qR))
	Flistabs.append(abs(F(qR)))

fig, ax = plt.subplots(1, 2)
ax[0].plot(QR,Flist, 'r--') #row=0, col=0
ax[0].set_xlim(0,20)
ax[0].set_ylim(-.2,1.1)
ax[0].set_xlabel('qR')
ax[0].set_ylabel('F')
ax[0].set_yscale('linear')
ax[0].set_title('Linear Form Factor')
ax[1].plot(QR,Flistabs, 'r--') #row=0, col=1
ax[1].set_xlim(0,20)
ax[1].set_ylim(0.000001,2)
ax[1].set_xlabel('qR')
ax[1].set_ylabel('F')
ax[1].set_yscale('log')
ax[1].set_title('Log Form Factor')
fig.savefig('walecka6-13.png',format='PNG')
fig.show()
