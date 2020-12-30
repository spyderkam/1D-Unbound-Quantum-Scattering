#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines 
from scipy.optimize import curve_fit

ħ, m = 1, 1

# the functions
def K1(E):  
    return np.sqrt(2*m*E / ħ)
def K2(k1, R):  
    return k1*((1-np.sqrt(R))/(1+np.sqrt(R)))
def V0(E, k2):   
    return E - (ħ*k2)**2/(2*m)

# formatting to later print full table which including R, V, and E
fmt = '{:<1} {:<8} {:<12} {:<12} {:<8}'
print(fmt.format('', 'i', 'R', 'V', 'E'))     # prepare the table header
print('__________________________________________')

# importing the experimental data
scatter = os.path.join(os.sep, 'path', 'to', 'scat.txt')     # put scat.txt in home directory to avoid typing path; i.e. just os.path.join(os.sep, 'scat.txt')
scatter = np.loadtxt(scatter)
E = scatter[:, 0]
R = scatter[:, 1]

# 1) obtain k1  2) use k1 to obtain k2  3) use k2 to obtain V
k1 = []     # initialize k1
V = []      # initialize V
for ii in enumerate(E):
    i = ii[0]     # because why not
    k1.append( K1(E[i]) )
    V.append( V0(E[i], K2(k1[i], R[i])) )
    print(fmt.format('', i, R[i], '%0.5f' % V[i], E[i]))     # print the aformentioned table
   

# preparing & plotting
## first plot R and T(=1-R) vs E/V to confirm scattering is unbounded
fake_point_1 = (0, 1)     # R is obviously always 1 before E=2...
fake_point_2 = (1, 1)     # ...so get creative ^_^

plt.plot(E/V, R, fake_point_1, fake_point_2, color='blue')
plt.plot(E/V, 1-R, color='red')

plt.xlabel(r'$E/V$', fontsize=15)
plt.ylabel(r"$R,T$", fontsize=15)

blue_line = mlines.Line2D([], [], color='blue',
                          markersize=10, label='R')
red_line = mlines.Line2D([], [], color='red',
                          markersize=10, label='T')
plt.legend(handles=[blue_line, red_line])
plt.show()     

x = np.linspace(0, 1, len(V))     # even spacing number of x's between 0 and 1 equal to the length of the V array
plt.scatter(x, V, color='violet')

def func(x, a, b, c, d, l, m, n):
    return a*x**6 + b*x**5 + c*x**4 + d*x**3 + l*x**2 + m*x + n
    
popt, pcov = curve_fit(func, x, V)
plt.plot(x, func(x, *popt), 'r-', color='dodgerblue')

plt.ylabel(r'$V(x)$', fontsize=17) #change to just r"$V$"
plt.xlabel(r"$x$", fontsize=17)
plt.tight_layout()
plt.show()

print("PARAMETERS:")
print('   a =', '%0.3f' % popt[0], '±', "%.3f" % pcov[0,0]**0.5) #THE 2ND HALF IS CODE FOR CALCULATING FIT UNCERTAINTY
print('   b =', "%0.3f" % popt[1], '±', "%.3f" % pcov[1,1]**0.5)
print('   c =', "%0.3f" % popt[2], '±', "%.3f" % pcov[2,2]**0.5)
print('   d =', "%0.3f" % popt[3], '±', "%.3f" % pcov[3,3]**0.5)
print('   l =', "%0.3f" % popt[4], '±', "%.3f" % pcov[4,4]**0.5)
print('   m =', "%0.3f" % popt[5], '±', "%.3f" % pcov[5,5]**0.5)
print('   n =', "%0.3f" % popt[6], '±', "%.3f" % pcov[6,6]**0.5)
