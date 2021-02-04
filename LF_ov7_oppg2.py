# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 7 - Oppgave 2

@author: Thomas Nyborg
"""

from matplotlib import pyplot as plt

def rektangelmetoden(verdier, t, startverdi = 0):
    """"Denne funksjonen bruker rektangelmetoden til å integrere verdier 
    i en liste verdier over en liste med t-verdier t.
    Funksjonen returnerer en liste integrert.
    """
    
    N = len(verdier) # antall verdier
    integrert = [startverdi] # startverdi for integralet
    A = 0 # variabel for å holde sum av rektangler
    
    for i in range(N-1): # x-verdier går fra a til b med mellomrom h
        h = t[i+1] - t[i]
        A += verdier[i] * h #bruker venstresum
        integrert.append(A)
    
    return(integrert)

def databehandling(fil):
    """
    Funksjon som deler opp datasettetet i akselerasjon- og tidsverdier.
    Samme funksjon som databehandling_avanced i oppgave 1.
    fil: string med tekstfil som skal åpnes.
    """
    with open(fil, 'r') as f:
        data = f.read()
        
        aks = [float(val) for val in data.split("[")[1].split("]")[0].split(", ")]
        tid = [float(val) for val in data.split("[")[2].split("]")[0].split(", ")]
    
    return(aks, tid)

    
### DATABEHANDLING ###
filnavn = ["liten fallskjerm.txt", "middels fallskjerm.txt", "stor fallskjerm.txt"]


for fil in filnavn: # finner strekning og plotter for hver av fallskjermene
    a_maling, t_maling = databehandling(fil) # legger måleverdier i to lister
    v_maling = rektangelmetoden(a_maling, t_maling) # finner farten ved integrasjon
    s_maling = rektangelmetoden(v_maling, t_maling) # finner strekning ved integrasjon
    
    # Plotter avstand som funksjon av tid
    plt.plot(t_maling, s_maling, label = fil.split(".")[0].capitalize() + f", s={s_maling[-1]:.2f} m")
    
plt.title("Tilbakelagt strekning")
plt.ylabel('Strekning [m]')
plt.xlabel('Tid [s]')
plt.legend()