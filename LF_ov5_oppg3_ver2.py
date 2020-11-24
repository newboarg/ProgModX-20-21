# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 5 - Oppgave 3, versjon 2
En mer effektiv løsning ved å bruke numpy arrays.

@author: Thomas Nyborg
"""
# IMPORTS
import numpy as np

# FUNKSJONER
def rektangelmetoden(f, x, h, offset = 0):
    """"Denne funksjonen bruker rektangelmetoden til å beregne arealet av  
    en funksjon f(x) for en liste (array) med x-verdier.
    Offset-verdier: 0 = venstresum (standard), 1  = høyresum, 0.5 = midtpunkt."""

    A = f(x+ offset*h)[:-1]*h # A blir et array med arealet av rektanglene
    return(sum(A)) # returnerer summen av alle rektanglene

def trapesmetoden(f, x, h):
    """"Denne funksjonen bruker trapesmetoden til å beregne arealet av  
    en funksjon f(x) for en liste (array) med x-verdier en steglengde på h."""
    
    A = (f(x)[:-1] + f(x)[1:])*h/2 #A blir et array med arealet av trapesene 
    return(sum(A)) # returnerer summen av alle trapesene
    
def f(x):
    "Standard normalfordelingsfunksjon"
    return(1/np.sqrt(2*np.pi) * np.exp(-x**2/2))


# SKRIPT

hs = [1e-1, 1e-5]
ks = [1, 2, 3]

file = open("integrasjon_ver2.txt", "w")

for h in hs:
    for k in ks:
        N = int((2*k)/h + 1) # antall steg tilsvarende h-verdi
        x = np.linspace(-k, k, N) # array med x-verdier
    
        file.write(f"k={k}, h={h}\n")
        file.write(f"Rektangelmetoden: {rektangelmetoden(f, x, h, 0.5):.4f}\n")
        file.write(f"Trapesmetoden: {trapesmetoden(f, x, h):.4f}\n\n")

file.close()
    