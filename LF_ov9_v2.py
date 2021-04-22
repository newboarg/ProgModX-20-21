# -*- coding: utf-8 -*-
"""
LØSNINGSFORSLAG - ØVING 9 (versjon 2)
Programmering og modellering X

Created on Tue Apr 6 2021

@author: Thomas Nyborg
"""

import numpy as np
from matplotlib import pyplot as plt

### FUNKSJONER
def derivert(T, T_0, k):
    """Derivert i henhold til differensiallikning (Newtons avkjølingslov)"""
    return(k * (T_0 -T))
    
def sort_data(t, T, index_start): 
    """ Funksjon som filtrerer ut gjentatte verdier av samme temperatur i målinger.
    Merk at det er den siste av de gjentatte verdiene som legges til.
    Variabelen index_start velger hvilken måling vi skal starte med, for å
    kunne filtrere ut uønsket data i starten (se plot for rådata).
    Funksjonen gjør også om fra sekunder til minutter i tidsmålingene."""
    t_sorted = []
    T_sorted = []#T[index_start]
    for i in range(index_start, len(T)):
        if T[i] == T[i-1]:
            pass
        else:
            T_sorted.append(T[i-1])
            t_sorted.append((t[i-1])/60)
            
    t_0 = t_sorted[0] # tid for første måling som blir brukt
    return(np.array(t_sorted) - t_0, np.array(T_sorted), t_0) # korrigerer t_sorted slik at tiden starter på 0
 
def find_temp(T, temp):
    """Funksjon for å finne indeksen i T-arrayet når temperaturen blir mindre 
    enn en gitt verdi temp"""
    for i, j in enumerate(T):
        if j<temp:
            break
    return(i)
        
    
### DATABEHANDLING
data = np.loadtxt('temperaturer_test.txt', skiprows=1)
first_index = 15 # brukes for å filtrere bort verdier i starten av datasett
times_raw = data[:,0] 
temps_raw = data[:,1]

times, temps ,t_0 = sort_data(times_raw, temps_raw, first_index) # filtrerte datasett


### TEORETISK MODELL
dt = 1/6  # tidssteg (i minutter)
T_omg = 4 # omgivelsestemperatur
k = 0.0165 # k-verdi (varmetapskoeffisient)

tstart = 0 # start-tid for simulering i modell
tstop = 5*60 # stopp-tid for simulering i modell

N = int((tstop-tstart)/dt + 1) # beregner antall steg
t = np.linspace(tstart, tstop, N) # array med tidsverdier
T = np.zeros_like(t) # array for å lagre temperaturverdier
T[0] = temps[0] # initialbetingelse - starttemperatur

# Eulers metode
for i in range(N-1):
    T[i+1] = T[i] + derivert(T[i], T_omg, k) * dt # bruker formel for å regne ut "neste steg" 
  
# Finner tiden der temperaturen faller under grensen T_limit
T_limit = T_omg + 0.5
t_limit = t[find_temp(T, T_limit)]

### PLOTTING
plt.figure(figsize=(10,6)) # ny figur
plt.title("Databehandling")
plt.plot(times_raw[:first_index], temps_raw[:first_index], 'xr', label = 'Filtreres bort, før index_start')
plt.plot(times_raw[first_index:], temps_raw[first_index:], 'xb', label = 'Filtreres bort, duplikatverdier')
plt.plot((times+ t_0)*60, temps, 'dg', label = "Brukes")
plt.plot((t+t_0)*60, T,'--', label = f"Teoretisk modell, k={k}")
plt.xlim(times_raw[0],times_raw[-1])
plt.ylim(min(temps_raw)-2, max(temps_raw)+2)
plt.xlabel("Tid [s]")
plt.ylabel("Temperatur [C]")
plt.legend()


plt.figure(figsize=(10,6)) # ny figur
plt.title(f"Simulering, k = {k}")
plt.plot(times, temps, 'x', label = "Måledata")
plt.plot(t,T_limit*np.ones_like(t), '--', label = r"$T_{omg} + 0.5$")
plt.plot(t, T, label = "Teoretisk modell")
plt.plot(t_limit, T_limit, "o", label = f"t = {t_limit/60:.0f}h {t_limit%60:.0f} min")
plt.xlabel("Tid [min]")
plt.ylabel("Temperatur [C]")
plt.legend()