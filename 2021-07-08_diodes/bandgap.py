#!/usr/bin/env python3
import numpy as np
from scipy.constants import *
import matplotlib.pyplot as plt


# Use intrinsic carrier concentration at 300 K
import intrinsic as n

Na = 2.5e18
Nd = 1.23e23
#T = 300
Tc = np.arange(-40, 150)# Celcius
T = Tc + 273.15
ic = np.isclose(T,300,rtol=1e-3,atol=1e-3)
i = np.where(ic)[0]

ni = n.calc_ni(T)

n_p = np.power(ni,2)/Na
V = np.multiply(n.k*T,np.log(Nd/n_p))/n.q

print("Bandgap = %g at %d C" % (V[i],Tc[i]))
plt.plot(Tc,V)
plt.grid()
plt.xlabel("Temperature [Celcius]")
plt.ylabel("Bandgap [V]")
plt.show()
