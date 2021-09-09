#!/usr/bin/env python3


from scipy import constants
import numpy as np
import matplotlib.pyplot as plt
k_b = constants.Boltzmann
q = constants.physical_constants["elementary charge"][0]

E_g = 1.13
TNOM = 300.15
T = np.arange(TNOM,TNOM + 100)
n_i_simple = 1.1e10 * 2**((T - TNOM)/11)
n_i_bsim = 1.45e10*(TNOM/300.15) * np.sqrt(T/300.15) \
    * np.exp(21.5565981 - (q*E_g)/(2*k_b*T))
plt.semilogy(T,n_i_simple,label="Simple")
plt.semilogy(T,n_i_bsim,label="BSIM 4.8")
plt.legend()
plt.xlabel("Temperature [K]")
plt.ylabel(" $n_i$ [$1/cm^3$]")
plt.savefig("l6_ni.pdf")
plt.show()
