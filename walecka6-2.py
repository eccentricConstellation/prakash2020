# script for walecka 6.2
#Emma Rice
# 2/6/2020
import numpy as np
import matplotlib.pyplot as plt

# solve eigenvalue equation to get V0
# plot the corresponding wavefunction
# plot corresponding probability density

# neutron
m1 = 939.6	# in terms of MeV
# proton
m2 = 938.3	# in terms of MeV
mu = m1*m2/(m1+m2)
hbar2 = (197.3269804)**2 # hbar in units of MeV*F
R = 2 # 2 Fermi
E = 2.22 # binding energy of deuteron in MeV
gamma = (2 * mu * E / hbar2)**(1/2)
#think of eigenvalue problem with change of variables
# -xcot(x)=gamma*R
xcotxList = []
xList = []
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
for x in my_range(0.00001, 2.4, .00001):
	xList.append(x)
	xcotxList.append(-x/np.tan(x))
#plotting eigenvalue solution
Rgamma = R*gamma*np.ones(len(xcotxList))
print("R*gamma =",Rgamma[0])
fig0 = plt.figure()
plt.plot(xList, xcotxList,'r')
plt.plot(xList, Rgamma)
plt.ylim(-3,3)
plt.xlim(0,2.4)
plt.title("eigenvalue solution")
plt.xlabel("dimensionless x = Rkappa")
plt.ylabel("xcotx and Rgamma")
plt.show()

#get values of solutions for V0:
idx = np.argwhere(np.diff(np.sign(Rgamma - xcotxList))).flatten() 
sol = xList[idx[0]] #we want first solution
#now solve for corresponding value of V--sol = R * kappa, kappa = (2 * mu * (V - E) / hbar2)**(1/2)
print("solving xcotx + gamma*R = 0, we find x to be", sol)
V = hbar2 * (sol / R)**2 / (2 * mu) + E
print("the first solution for V0 is", V, "MeV")
#PSInlm(r)=u{nl}(r)/r*Y{lm}(theta,phi)
kappa = (2*mu*(V - E)/hbar2)**(.5)
#Y00=(4*np.pi)**(-1/2)... but we only want the radial bit here :)
A = (2/(R-np.sin(2*kappa*R)/(2*kappa)+(np.sin(kappa*R))**(2)/gamma))**.5
C = A*np.exp(gamma*R)*np.sin(kappa*R)
print("coefficients for radial wavefunction:\nA =",A,"\nC =",C)

def u10(r):
	if r <= R:
		u10 = A*np.sin(kappa*r)
	else:
		u10 = C*np.exp(-gamma*r)
	return u10
#graph it!
rList = []
uList = []
probList = []
for r in my_range(0.00001,2*R,.01):
	rList.append(r)
	u = u10(r)
	uList.append(u)
	prob = u**2
	probList.append(prob)
fig1 = plt.figure()
plt.plot(rList,uList) 
plt.title('stationary state radial wavefunction of deuteron')
plt.xlabel('r (F)')
plt.ylabel('u10(r)')
plt.show() 

#plot probability density too
fig2 = plt.figure()
plt.plot(rList,probList) 
plt.title('probability density of deuteron')
plt.xlabel('r (F)')
plt.ylabel('u10(r)')
plt.show() 

r1List = []
prob1List = []
#integrate |u10|^2 from 0 to R
for r1 in my_range(0.00001,R,.01):
	r1List.append(r1)
	u = u10(r1)
	prob1 = u**2
	prob1List.append(prob1)
integration = np.trapz(prob1List,r1List)
print("integration from 0 to R of the probability density is ", integration)
