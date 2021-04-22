# -*- coding: utf-8 -*-
"""
LØSNINGSFORSLAG - ØVING 9 (versjon 1)
Programmering og modellering X

Created on Tue Apr 6 2021

@author: Thomas Nyborg
"""

import numpy as np
from matplotlib import pyplot as plt

# DATABEHANDLING
filnavn = "temperaturer_test.txt"

data = np.loadtxt(filnavn, float, skiprows = 1)
index_start = 6
tid = data[index_start:, 0]
tid -= tid[0] 

temp = data[index_start:, 1]

plt.figure(figsize=(10,6))
plt.title("Datamateriale")
plt.plot(tid, temp,'x', label = "Målinger")
plt.xlabel("tid (s)")
plt.ylabel("temperatur (C)")


# TEORETISK MODELL
k = 0.00027
T_omg = 4 # utetemperatur
T_0 = temp[0]  # starttemperatur i vannet

h = 1 # mellomrom mellom tidsverdier i modell
t_start = 0
t_slutt = 4.27*60*60 # slutt-tid i sekunder

N = int((t_slutt - t_start) / h + 1)

t = np.linspace(t_start, t_slutt, N)
T = np.zeros(N)
T[0] = T_0

# Eulers metode
for i in range(N-1):
    T[i+1] = T[i] + k*(T_omg - T[i])*h
    

# PLOTTING
plt.figure(figsize=(10,6))
plt.plot(tid, temp, 'x')
plt.plot(t, T, label = "Teoretisk modell")
plt.plot(t, (T_omg + 0.5) *np.ones(N),'--', label = "Utetemperatur + 0.5 grad")
plt.title(f"k = {k}. Siste verdi: T({t[-1]:.0f}) = {T[-1]:.2f}")
plt.legend()


