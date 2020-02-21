# script for walecka 6.11
#Emma Rice
# 2/17/2020
import numpy as np

def SEMF(B,Z):
	a1 = 15.75
	a2 = 17.8
	a3 = .710
	a4 = 23.7
	a5 = 34
	if (B % 2 == 0):
		if (Z % 2 == 0):
			lambd = -1
		else:
			lambd = 0
	else:
		lambd = 1
	semf = -a1*B + a2*B**(2/3) + a3*Z**(2)/B**(1/3) + a4*(B-2*Z)**2/B + lambd*a5/B**(3/4)
	return semf

energia = SEMF(134, 50) + SEMF(104,42) - SEMF(238,92)
print("ground state energy of nucleus is",energia)
