#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.pyplot as plt

ħ, m = 1, 1

# the functions
def K1(E):         # k1 function
    return np.sqrt(2*m*E / ħ)

def K2(k1, R):     # k2 function
    return k1*((1-np.sqrt(R))/(1+np.sqrt(R)))

def V0(E, k2):     # V_0 function
    return E - (ħ*k2)**2/(2*m)
