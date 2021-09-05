#!/usr/bin/env python3

from scipy import constants
import numpy as np
h = constants.physical_constants["Planck constant"][0]
k = constants.Boltzmann
q = constants.physical_constants["elementary charge"][0]
c = constants.c
alpha = constants.physical_constants["fine-structure constant"][0]

mu = 2* alpha*h/(c*np.power(q,2))
print("Permiability of free space = %g" % mu)

epsilon = 1/(mu* c**2)
print("Permittivity of free space = %g" % epsilon)
