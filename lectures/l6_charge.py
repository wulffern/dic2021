#!/usr/bin/env python3

from scipy import constants
import numpy as np
import math
import matplotlib.pyplot as plt
h = constants.physical_constants["Planck constant"][0]
k = constants.Boltzmann
q = constants.physical_constants["elementary charge"][0]
c = constants.c
alpha = constants.physical_constants["fine-structure constant"][0]

mu = 2* alpha*h/(c*np.power(q,2))
epsilon = 1/(mu* c**2)


# Relative permitivity of silicon
Ks = 11.8

V = 5
# Assume a sphere volume of 1/cm^3

# Volume = 4/3*pi*r^3
r = math.pow(1/((4.0/3.0)*np.pi),1.0/3.0)
print("Radius for a 1 cm^3 volume = %r cm" %r)

# Capacitance for a sphere C = 4*pi*epsilon*r

C = 4.0*np.pi*epsilon*Ks*r
num = C*V/q

print("Charge removed per cm^3 for silicon for a %g V difference in intrinsic silicon = %g " % (V,num))
