# walecka6-13.py
# Emma Rice
# 2/19/2020

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
for qR in my_range(0.00001, 20.00001,0.00001):
	QR.append(qR)
	Flist.append(F(qR))

fig1 = plt.figure()
plt.plot(QR,Flist, 'r--') 
plt.title('form factor of uniformly charged sphere')
plt.axis([0, 20, -.2, 1.1])
plt.xlabel('qR')
plt.ylabel('F')
plt.show() 
