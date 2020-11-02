# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 4 - Oppgave 3

@author: Thomas Nyborg
"""
from matplotlib import pyplot as plt
import numpy as np

a = np.loadtxt("akselerasjon.txt", float) # akselerasjon i milli-g

t = np.arange(0, len(a))*5e-3 # tider i s

plt.plot(t,a)
plt.xlabel("tid [s]")
plt.ylabel("akselerasjon [milli-g]")
plt.show()