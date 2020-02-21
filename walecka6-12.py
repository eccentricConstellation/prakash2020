# walecka6-12.py
# Emma Rice
# 2/19/2020

import numpy as np 
import matplotlib.pyplot as plt

a1 = 15.75
a2 = 17.8
a3 = .710
a4 = 23.7

def stability(N,Z):
	s = (N+Z)/(a3*(N+Z)**(2/3)/(2*a4) + 2) - Z
	return s
def ndrip(N,Z):
	B = N + Z
	drip = -a1 + 2*a2/(3*(B)**(1/3)) - a3*Z**2/(3*(B)**(4/3)) + a4*(2*(N-Z)/B - (N-Z)**2/B**2)
	return drip
def pdrip(N,Z):
	B = N + Z
	drip = -a1 + 2*a2/(3*(B)**(1/3)) + a3*Z*(6*B-Z)/(3*B**(4/3)) - a4*((3*N+Z)*(N-Z)/B**2)
	return drip
# for every value of Z for fixed N where drip == 0; record and plot Z,N
N = []
Z = []
for n in range(0,160):
	for z in range(1,118):
	#check for fixed N where stability(N,Z) = 0
		if(stability(n,z) < 0.001):
			N.append(n)
			Z.append(z)
			break
NN = []
ZN = []
for n in range(0,160):
	for z in range(1,118):
	#check for fixed N where ndrip(N,Z) = 0
		if(ndrip(n,z) < 0.001):
			NN.append(n)
			ZN.append(z)
			break
NZ = []
ZZ = []
for n in range(0,160):
	for z in range(1,118):
	#check for fixed N where pdrip(N,Z) = 0
		if(pdrip(n,z) < 0.01):
			NZ.append(n)
			ZZ.append(z)
			break

fig1 = plt.figure()
plt.plot(N, Z, 'r--') 
plt.plot(NN, ZN, 'b--')
plt.plot(NZ, ZZ, 'g--')
plt.title('Line of Stability')
plt.xlabel('N')
plt.ylabel('Z')
plt.show() 

