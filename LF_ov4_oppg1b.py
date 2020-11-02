# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 4 - Oppgave 1b

@author: Thomas Nyborg
"""

from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return(np.sin(x))

def g(x):
    return(np.cos(x))

def h(x):
    return(np.tan(x))

def i(x):
    return(2*x**2 - 2)    

x0 = 0 # startverdi for x
x1 = 2*np.pi # sluttverdi for x
dx = 0.1 # steglengde
N = int((x1-x0)/dx + 1) # antall punkter i x-lista

xer = np.linspace(x0, x1, N, endpoint = False) # x-verdier med linspace
 
yer = f(xer) # funksjonsverdier
    
plt.plot(xer,yer)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()