#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines 
from scipy.optimize import curve_fit

ħ, m = 1, 1

# the functions
def K1(E):         # k1 function
    return np.sqrt(2*m*E / ħ)
def K2(k1, R):     # k2 function
    return k1*((1-np.sqrt(R))/(1+np.sqrt(R)))
def V0(E, k2):     # V_0 function
    return E - (ħ*k2)**2/(2*m)

# formatting to print full table
fmt = '{:<1} {:<8} {:<12} {:<12} {:<8}'
print(fmt.format('', 'i', 'R', 'V', 'E'))     # for printing later in this cell
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
    print(fmt.format('', i, R[i], '%0.5f' % V[i], E[i]))     # print table including R, V, and E
   

# preparing & plotting
## first plot R and T(=1-R) vs E/V to confirm scattering is unbounded
fake_point_1 = (0, 1)     # R is obviously always 1 before E = 2.0
fake_point_2 = (1, 1)     # so get creative ^_^

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

## confirmed; now get rid of all V's corresponding R=1 for beter fit
for i in range(3):
    V.pop(0)
    
x = np.linspace(0, 1, len(V))     # even spacing number of x's between 0 and 1 equal to the length of the V array
plt.scatter(x, V, color='violet')

def func(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d
    
popt, pcov = curve_fit(func, x, V)
plt.plot(x, func(x, *popt), 'r-', color='dodgerblue')

plt.ylabel(r'$V(x)=ax^3+bx^2+cx+d$', fontsize=13)
plt.xlabel(r"$x$", fontsize=13)
plt.tight_layout()
plt.show()

print("PARAMETERS:")
print('   a =', '%0.3f' % popt[0], '±', "%.3f" % pcov[0,0]**0.5)     #THE 2ND HALF IS CODE FOR CALCULATING FIT UNCERTAINTY
print('   b =', "%0.3f" % popt[1], '±', "%.3f" % pcov[1,1]**0.5)
print('   c =', "%0.3f" % popt[2], '±', "%.3f" % pcov[2,2]**0.5)
print('   d =', "%0.3f" % popt[3], '±', "%.3f" % pcov[3,3]**0.5)
