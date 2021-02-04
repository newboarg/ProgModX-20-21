# -*- coding: utf-8 -*-
"""
#LF Muntlig høring
Created on Wed Jan  6 14:52:05 2021

@author: thony
"""
import numpy as np
from matplotlib import pyplot as plt

# KJEKKE FUNKSJONER
def rektangelmetoden(f, t):
    """"Denne funksjonen bruker rektangelmetoden til å integrere verdier 
    for en liste f over en liste med t-verdier t.
    Funksjonen returnerer en liste med verdier I.
    """
    
    N = len(f) # antall verdier
    I = [0] # liste for den integrerte. Startverdi 0
    A = 0 # variabel for å holde sum av rektangler
    
    for i in range(N-1): # x-verdier går fra a til b med mellomrom h
        h = t[i+1] - t[i]
        A += f[i] * h # bruker venstresum
        I.append(A)
    
    return(I)

def derivert_asym(f, t): # funksjon for den deriverte ved Newtons kvotient
    d = []
    for i in range(len(f)-1):
        d.append((f[i+1]-f[i])/(t[i+1]-t[i]))
    return(d)

# PUNKT 1 - IMPORTERING OG PLOTTING AV HASTIGHET
data = np.loadtxt('usainbolt.txt', float, skiprows = 1)

t = data[:,0]
v = data[:,1]

plt.figure()
plt.plot(t,v)
plt.xlabel(r'$t$')
plt.ylabel(r'$v(t)$')

# PUNKT 2 - NUMERISK INTEGRASJON FOR Å FINNE STREKNING
s = rektangelmetoden(v, t)

plt.figure()
plt.plot(t,s)
plt.xlabel(r'$t$')
plt.ylabel(r'$s(t)$')

# PUNKT 3 - NUMERISK DERIVASJON FOR Å FINNE AKSELERASJON
a = derivert_asym(v, t)

plt.figure()
plt.plot(t[:-1], a)
plt.xlabel(r'$t$')
plt.ylabel(r'$a(t)$')

# PLOTTING AV ALT
fig, (ax1, ax2, ax3) = plt.subplots(3,1, sharex = True, figsize = (7,10))
fig.suptitle("Usain Bolt 100m 2009")

ax1.plot(t, s, color = "r")
ax1.set_ylabel(r'$s(t)$')

ax2.plot(t, v, color = "g")
ax2.set_ylabel(r'$v(t)$')

ax3.plot(t[:-1], a)
ax3.set_ylabel(r'$a(t)$')

plt.xlabel(r"$t$")