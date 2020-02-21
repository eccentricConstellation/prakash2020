# Emma Rice
# 2/6/2020
# descr: solves thomas fermi eqn bc I'm foolish and didn't make this very portable

	# thomas fermi equation:
	#		x^(1/2) * chi''(x) = [chi(x)]^(3/2)
	#		where chi(x) is universal screening function
	#		chi(0) = 1; nucleus at origin
	#		chi(infinity) = 0; neutral atom
# need to reduce order
#du = [u2, x^(-0.5)*u1^(1.5)]
# then start at origin where chi(0) = 1
# can't start with chi'(0)=0. too sensitive to chi'.
# until solution that decreases to 0 for large x is found

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from tabulate import tabulate
def du(u,x):
  udot = [[],[]]
  udot[0] = u[1]
  udot[1] = np.power(x, -0.5)*np.power(u[0], 1.5)
  return udot

x = np.linspace(0.000000000000000001,12,60)
u0 = np.array([1,-1.58807])
U = odeint(du,u0,x)
integration = np.trapz(U[:,0],x)
#print(integration)
# plot results
plt.plot(x,U[:,0])
#plt.plot(x,u[:,1],'k-.')
plt.xticks(np.arange(0, 12.1, step=1))
plt.axis([0, 12, 0, 1.0])
plt.title("SOLUTION TO THOMAS-FERMI EQUATION")
plt.xlabel('Distance x')
plt.ylabel('Thomas Fermi function chi(x)')
plt.show()
#{:.1f}".format(x)?
print(tabulate({"x": x,"Chi(x)": U[:,0]}, headers="keys"))
print(tabulate({"x": x,"Chi'(x)": U[:,1]}, headers="keys"))
# i2 = integration on [0,infinity] of (chi'(x))**2dx
chip2 = U[:,1]
for i in range(0,len(chip2)):
	chip2[i] = (chip2[i])**2
i2 = np.trapz(chip2,x)
print("\ni2 yields:",i2)
