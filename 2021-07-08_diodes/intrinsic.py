#!/usr/bin/env python3
######################################################################
##        Copyright (c) 2021 Carsten Wulff Software, Norway
## ###################################################################
## Created       : wulff at 2021-8-11
## ###################################################################
##  The MIT License (MIT)
##
##  Permission is hereby granted, free of charge, to any person obtaining a copy
##  of this software and associated documentation files (the "Software"), to deal
##  in the Software without restriction, including without limitation the rights
##  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##  copies of the Software, and to permit persons to whom the Software is
##  furnished to do so, subject to the following conditions:
##
##  The above copyright notice and this permission notice shall be included in all
##  copies or substantial portions of the Software.
##
##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##  SOFTWARE.
##
##

# based on Streetman

from scipy import constants
import numpy as np
import matplotlib.pyplot as plt
######################################################################
# Intrinsic carrier concentration
######################################################################
#
#
# Constants
# 300 K ~ 27 C

h = constants.physical_constants["Planck constant"][0]
k = constants.Boltzmann
pi = constants.pi
m0 = constants.m_e
q = constants.physical_constants["elementary charge"][0]
eV = constants.physical_constants["electron volt"][0]


def calc_ni(T):
    #Calculate intrinsic carrier concentration as a function of temperature in Kelvin

#
#
# |----------------- Ec = Conduction band
# |  |
# |  Eg  = Band gap
# |  |
# |  |
# |----------------- Ev = Valence band
#
    Eg = 1.1 *eV  #Bandgap of Silicon, changes with temperature, but we ignore that

# The mass of electrons and holes are not constant with temperature, however, let's assume they are, and let's ignore the
# fact that the effective mass is not the same for holes and electrons
    mn = 1*m0
    mp = 1*m0

# The intrinsic carrier concentration depends on the fermi level and the density of states, which depends
# on the effective mass of electrons and holes. See page 90 - 95 in Streetman

    Nc = 2*np.sqrt(np.power((2*pi*k*T*mn)/(h*h),3))
    Nv = 2*np.sqrt(np.power((2*pi*k*T*mp)/(h*h),3))

    ni = np.sqrt(Nc*Nv)*np.exp(-Eg/(2*k*T))
    return ni

if __name__ == "__main__":

    K0 = -273.15
    Tc = np.arange(-40, 150)# Celcius
    T = Tc - K0
    ic = np.isclose(T,300,rtol=1e-3,atol=1e-3)
    i = np.where(ic)[0]
    ni = calc_ni(T)
    print("Intrinsic carrier concentration (no) = %g at %d C"%(ni[i], Tc[i]))

    plt.semilogy(Tc,ni,label="Electrons")
    plt.grid()
    plt.ylabel("Intrinsic carrier concentration [1/m^3]")
    plt.xlabel("Temperature [Celcius]")
    #plt.plot(T,p,label="Holes")
    plt.show()
