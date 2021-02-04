# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 6 - Oppgave 2

@author: Thomas Nyborg
"""
import numpy as np

def f(x):
    """"Funksjonen vi vil finne nullpunkt til"""
    #return((2*x + 1) / (2/3 - 2*x))
    return(np.e**(2*x) - 10)

def derivert(f, x, h):
    """Funksjon for derivert ved Newtons kvotient."""
    return((f(x+h)-f(x))/h)

null = 1e-4 # nøyaktighet for nullpunktet
x0 = -1 # startverdi
max_steps = 100 # for å unngå å lete uendelig lenge

h = 1e-5 # Steglengde for numerisk derivasjon av f ved Newtons kvotient.

counter = 0 # tellevariabel for å holde antall steg som er utført

while abs(f(x0)) > null and counter < max_steps: 
    # Algoritmen kjører så lenge funksjonsverdien er utenfor kravet vi har 
    # satt for øvre og nedre verdi rundt x-aksen, eller til antall steg
    # passerer max_steps
   
    x0 -= f(x0)/derivert(f,x0,h) # Algoritmen beskrevet i Newtons metode
    
    counter += 1 # øker counter med 1


if counter == max_steps:
    print("Max steg nådd!")

else:
    print(f"Nullpunkt: x= {x0:.4f} (nøyaktighet {null}) funnet etter {counter} steg.")
