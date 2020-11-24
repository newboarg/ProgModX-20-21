"""
Løsningsforslag
Øving 5 - Oppgave 2

@author: Thomas Nyborg
"""

import numpy as np
from matplotlib import pyplot as plt

def derivert_asym(s, h): # funksjon for den deriverte ved Newtons kvotient
    v = []
    for i in range(len(s)-1):
        v.append((s[i+1]-s[i])/h)
    return(v)

def derivert_sym(s, h): # funksjon for den deriverte ved Newtons symmetriske kvotient
    v = []
    for i in range(1,len(s)-1):
        v.append((s[i+1]-s[i-1])/(2*h))
    return(v)

data = np.loadtxt("vogn.txt", float, skiprows=1)

t = data[:,0]
s = data[:,1]
h = t[1]-t[0]

plt.plot(t[:-1], derivert_asym(s, h), 'b', label = "asymmetrisk")
plt.plot(t[1:-1], derivert_sym(s, h), 'g', label = "symmetrisk")
plt.plot()
plt.legend()