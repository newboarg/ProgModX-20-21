# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 6 - Oppgave 4

@author: Thomas Nyborg
"""

import numpy as np
from matplotlib import pyplot as plt

def f_derivert(t, ft):
    """Funksjon som returnerer den deriverte i henhold til oppgitt difflikning."""
    return(4 + 3*ft) # endres ihht opggave a), b), c) og d)

t_0 = 0 # startverdi for t (initialbetingelse)
f_0 = 0 # startverdi for f (initialbetingelse)
t_slutt = 2 # sluttverdi for t

N = 10000 # antall steg
h = (t_slutt-t_0)/(N-1) # regner ut steglengden

t = np.linspace(t_0, t_slutt, N) # lager et array for verdier av t fra startverdi til sluttverdi
f = np.zeros(N) # lager et array for å lagre verdier for f
f[0] = f_0 # initialbetingelse


#Eulers metode
for i in range(N-1):
    f[i+1] = f[i] + f_derivert(t[i], f[i])*h # bruker formel for å regne ut "neste steg" 

plt.plot(t, f) # plotter løsningen
plt.title(fr"Løsning av difflikning med $t(0)={t_0}$ og $f(0)={f_0}$")
plt.xlabel(r"$t$")
plt.ylabel(r"$f(t)$")