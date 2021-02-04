# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 7 - Oppgave 1

@author: Thomas Nyborg
"""

import numpy as np
from matplotlib import pyplot as plt

def rektangelmetoden(a, t):
    """"Denne funksjonen bruker rektangelmetoden til å integrere verdier 
    for akselerasjon i en liste a over en liste med t-verdier t.
    Funksjonen returnerer en liste med fartsverdier v.
    """
    
    N = len(a) # antall verdier
    v = [0] # liste for fartsverdier, startfart 0
    A = 0 # variabel for å holde sum av rektangler
    
    for i in range(N-1): # x-verdier går fra a til b med mellomrom h
        h = t[i+1] - t[i]
        A += a[i] * h #bruker venstresum
        v.append(A)
    
    return(v)

def databehandling(fil):
    """
    Funksjon som deler opp datasettetet i akselerasjon- og tidsverdier.
    fil: string med tekstfil som skal åpnes.
    """
    f = open(fil, 'r')
    data = f.read()

    data_a = data.split("[")[1].split("]")[0].split(", ")
    data_t = data.split("[")[2].split("]")[0].split(", ")

    aks = []
    tid = []

    for val in data_a:
        aks.append(float(val))

    for val in data_t:
        tid.append(float(val))
    
    f.close()
    
    return(aks, tid)

def databehandling_advanced(fil):
    """
    En litt mer kompakt og avansert versjon av databehanding()-funksjonen.
    Begge funksjonene gjør det samme, men denne er mer effektiv.
    fil: string med tekstfil som skal åpnes.
    """
    with open(fil, 'r') as f:
        data = f.read()
        
        aks = [float(val) for val in data.split("[")[1].split("]")[0].split(", ")]
        tid = [float(val) for val in data.split("[")[2].split("]")[0].split(", ")]
    
    return(aks, tid)

def writeToFile(fil, aks, tid):
    """
    Funksjon som skriver akselerasjon- og fartsverdier til fil i kolonneformat.
    fil: filnavn, for type fallskjerm (string)
    aks: akselerasjonsverdier (list)
    tid: tidsverdier (list)
    """

    f = open("processed_"+fil, 'w')
    
    f.write("Aks Tid")
    for i in range(len(aks)):
        f.write(f"\n{aks[i]} {tid[i]}")
    f.close()
        
    
### DATABEHANDLING ###
# input til mode gir en indeks som brukes for å angi filnavn fra en liste med navn
mode = int(input("1: Liten fallskjerm\n2: Middels fallskjerm\n3: Stor fallskjerm\n")) - 1 
filnavn = ["liten fallskjerm.txt", "middels fallskjerm.txt", "stor fallskjerm.txt"][mode]

a_maling, t_maling = databehandling(filnavn) # legger måleverdier i to lister
v_maling = rektangelmetoden(a_maling, t_maling) # finner farten ved integrasjon

writeToFile(filnavn, a_maling, t_maling) # skriver data til fil

### MODELL ###
# Konstanter
g = 9.81 # tyngdeakselerasjon
m = 0.37 # massen av ballen
k = 0.045 # faktor som tar hensyn til formen til ballen, vind, lufftrykk i ballen, m.o.h., temperatur osv.

# Initialbetingelser for modell
t_0 = t_maling[0]
t_s = t_maling[-1]

N = 500 # Antall steg

v = np.zeros(N) # Liste for å lagre fartsverdier
t = np.linspace(t_0, t_s, N)

### EULERS METODE FOR Å FINNE FARTEN (MODELL)
for i in range(N-1):
    h = t[i+1] - t[i]
    v[i+1] = v[i] + h *(g - k * v[i]**2 / m) 

### PLOTTING
plt.plot(t,v, label = 'Modell')
plt.plot(t_maling, v_maling, label = 'Datasett')

plt.xlabel('tid [s]')
plt.ylabel('fart [m/s]')
plt.title(f'{filnavn.split(".")[0]}, k = {k}')
plt.grid()
plt.legend()
