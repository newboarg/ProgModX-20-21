# -*- coding: utf-8 -*-
"""
LØSNINGSFORSLAG - ØVING 10
Programmering og modellering X

Created on Sun Apr 18 2021

@author: Thomas Nyborg
"""

import numpy as np
from matplotlib import pyplot as plt

def dh(h, k):
    """ Den deriverte i henhold til oppgit differensiallikning"""
    return(-k*np.sqrt(h))


   
def find_level(h, h_limit):
    """Funksjon for å finne indeksen i h-arrayet når vannstanden blir mindre 
    enn en gitt verdi h_limit"""
    for i, j in enumerate(h):
        if j<h_limit:
            break
    return(i)


# DIMENSJONER AV TANK
# verdier som angis
h_0 = 9 # angir vannstand i starten (i cm)
d = 9.5 # angir diameter av beholder (i cm)
dp = 0.8 # angir diameter av hull (i cm)

# verdier som beregnes
A = np.pi * (d/2)**2 # areal av vannoverflate
Ap = np.pi * (dp/2)**2 # areal av hull



# TEORETISK MODELL
t_0 = 0
t_slutt = 30
dt = 0.01
N = int((t_slutt-t_0)/dt + 1 )
t = np.linspace(t_0, t_slutt, N) # lager et array for verdier av t fra startverdi til sluttverdi
h = np.zeros(N) # lager et array for å lagre verdier for h
h[0] = h_0 # initialbetingelse

### k0-verdi ###
k0 = 15.5 # denne verdien endres for å tilpasse modell til målinger
###

k = k0 * Ap/A # k-verdi
h_m = h_0/2 # vannstand mål

#EULERS METODE
for i in range(N-1):
    h[i+1] = h[i] + dh(h[i], k)*dt
 
    
t_m = t[find_level(h, h_m)] # tiden der vannstanden kommer under h_mal

# PLOTTING
plt.figure(figsize=(10,6))
plt.plot(t/60, h, label = "Modell") # plotter løsningen
plt.plot(t/60, np.ones_like(h)*h_m, '--g')
plt.plot(np.ones_like(h)*t_m/60,h, '--g')
plt.plot(t_m/60, h_m,'o',label = r"$h < h_0/2$")
plt.title(f"Modell for vannhøyde i tank. \nDiameter tank: {d} cm. Diameter hull: {dp} cm.\nBeregnet tid for halvveis tømming: {t_m//60:.0f} min  {t_m%60:.0f} s (k0 = {k0})")
plt.ylabel("Vannhøyde [cm]")
plt.xlabel("tid [min]")
plt.legend()
plt.grid()