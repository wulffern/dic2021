#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.05, 4,num=50)

veff = 0.2 # V
mu_n = 0.01*100**2# m/Vs

v = mu_n * veff / (x*1e-6)

vsat = [2.3e5*100]*np.ones(len(x))

c = [3e8]*np.ones(len(x))
plt.semilogy(x,v,label=r"$v = \mu \times \frac{dv}{dx}$")
plt.semilogy(x,vsat,label="speed limit in silicon")
plt.semilogy(x,c,label="speed of light")
plt.legend()
plt.title("Rough estimate!")
plt.savefig("l5_velocity.pdf")
plt.xlabel("L [um]")
plt.ylabel("Velocity [m/s]")
plt.show()
