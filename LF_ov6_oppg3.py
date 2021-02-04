# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 6 - Oppgave 3

@author: Thomas Nyborg
"""
import numpy as np
def y(t):
    """"Funksjonen vi vil finne nullpunkt til"""
    
    return(-1/2*g*t**2 + 18*np.sin(theta)*t)

def x(t):

    return(18*np.cos(theta)*t)

def derivert(f, x, h):
    """Funksjon for derivert ved Newtons kvotient."""
    return((f(x+h)-f(x))/h)

theta = np.pi/10
g = 9.81
  
null = 1e-4 # nøyaktighet for nullpunktet
t0 = 0.7 # startverdi
max_steps = 100 # for å unngå å lete uendelig lenge

h = 1e-5 # Steglengde for numerisk derivasjon av f ved Newtons kvotient.

counter = 0 # tellevariabel for å holde antall steg som er utført

while abs(y(t0)) > null and counter < max_steps: 
    # Algoritmen kjører så lenge funksjonsverdien er utenfor kravet vi har 
    # satt for øvre og nedre verdi rundt x-aksen, eller til antall steg
    # passerer max_steps
   
    t0 -= y(t0)/derivert(y,t0,h) # Algoritmen beskrevet i Newtons metode
    
    counter += 1 # øker counter med 1

if counter == max_steps:
    print("Max steg nådd!")

else:
    print(f"Nullpunkt: t= {t0:.4f} (nøyaktighet {null}) funnet etter {counter} steg.")

    print(f"\"fasit\": {36*np.sin(theta)/g:.4f} ")
    
    print(f"Ballen ble kastet {x(t0):.2f} meter langs bakken.")