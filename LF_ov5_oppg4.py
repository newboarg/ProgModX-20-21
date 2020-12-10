# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 5 - Oppgave 4

@author: Thomas Nyborg
"""

import numpy as np
from matplotlib import pyplot as plt

def rektangelmetoden(a, t):
    """"Denne funksjonen bruker rektangelmetoden til å integrere verdier 
    for akselerasjon i en liste a over en liste med t-verdier t.
    Funksjonen returnerer en liste med fartsverdier v.
    """
    
    N = len(aks) # antall verdier
    v = [0] # liste for fartsverdier, startfart 0
    A = 0 # variabel for å holde sum av rektangler
    
    for i in range(N-1): # x-verdier går fra a til b med mellomrom h
        h = t[i+1] - t[i]
        A += a[i] * h #bruker venstresum
        v.append(A)
    
    return(v)


def trapesmetoden(a, t):
    """"Denne funksjonen bruker trapesmetoden til å beregne arealet av  
    en funksjon f(x) fra x=a til x=b med en steglengde på h."""
    
    N = len(aks)
    v = [0] # liste for fartsverdier, startfart 0 
    A = 0
    
    for i in range(N-1):
        h = t[i+1] - t[i]
        A += (a[i+1] + a[i])/2 * h  # arealet av et trapes
        v.append(A)
        
    return(v)


data = np.loadtxt('fallskjermmålinger.txt', skiprows = 1)

tid = data[:,0]
aks = data[:, 1]


v_rekt = rektangelmetoden(aks, tid)
v_trap = trapesmetoden(aks, tid)

fig, (ax1, ax2, ax3) = plt.subplots(3,1, sharex = True, figsize = (7,10) )
ax1.plot(tid, aks)
ax1.set_ylabel(r'$a(t)$')
ax2.plot(tid, v_rekt, color = "g", label = 'Rektangelmetoden')
ax2.set_ylabel(r'$v(t)$')
ax2.legend()
ax3.plot(tid, v_trap, color = "b", label = 'Trapesmetoden')
ax3.set_ylabel(r'$v(t)$')
ax3.legend()
plt.xlabel(r"$t$")
