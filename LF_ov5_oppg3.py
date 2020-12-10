# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 5 - Oppgave 3

@author: Thomas Nyborg
"""

import numpy as np

def rektangelmetoden(f, a, b, h, offset):
    """"Denne funksjonen bruker rektangelmetoden til å beregne arealet av  
    en funksjon f(x) fra x=a til x=b med en steglengde på h."""
    
    A = 0 # variabel for å holde summen av arealene 
    
    for x in np.arange(a, b, h): # x-verdier går fra a til b med mellomrom h
        A += f(x + offset*h)*h 
    return(A)

def trapesmetoden(f, a, b, h):
    """"Denne funksjonen bruker trapesmetoden til å beregne arealet av  
    en funksjon f(x) fra x=a til x=b med en steglengde på h."""
    
    A = 0 # variabel for å holde summen av arealene 
    
    for x in np.arange(a, b, h): # x-verdier går fra a til (men ikke med) b med mellomrom h
        A += (f(x) + f(x+h))*h/2 # arealet av et trapes
    return(A)
    
def f(x):
    "Standard normalfordelingsfunksjon"
    return(1/np.sqrt(2*np.pi) * np.exp(-x**2/2))

hs = [1e-1, 1e-5]
ks = [1, 2, 3]

file = open("integrasjon_ver1.txt", "w")

for h in hs:
    for k in ks:
        N = int((2*k)/h + 1) # antall steg tilsvarende h-verdi
        x = np.linspace(-k, k, N) # array med x-verdier
    
        file.write(f"k={k}, h={h}\n")
        file.write(f"Rektangelmetoden: {rektangelmetoden(f, -k, k, h, 0.5):.4f}\n")
        file.write(f"Trapesmetoden: {trapesmetoden(f, -k, k, h):.4f}\n\n")

file.close()
    
