# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 6 - Oppgave 5

@author: Thomas Nyborg
"""
import numpy as np
from matplotlib import pyplot as plt

def derivert(f, k):
    """ Funksjon som returnerer en verdi for den deriverte i henhold til
    oppgitt difflikning. k er en konstant og f angir antallet harer."""
    
    return(k*f) 

### VARIABLER OG BETINGELSER
t_0 = 0 # startverdi for t (initialbetingelse)
f_0 = 1000 # startverdi for f (initialbetingelse, antallet harer ved utsetting)
t_slutt = 20 # sluttverdi for t

k = 0.1
 
N = 1000 # Antall steg, bør være minst antall måneder pluss 1.
# dette tilsvarer å evaluere veksten i bestanden etter hver måned.
# Dette vil ikke være helt nøyaktig.
# Hvis vi ønsker å modellere kontinuerlig vekst bør vi gjøre N så 
# stor som mulig for å få best mulig resultat.

h = (t_slutt-t_0)/(N-1) # regner ut steglengden

t = np.linspace(t_0, t_slutt, N) # array for verdier av t
f = np.zeros(N) # array for å lagre verdier for populasjonen av harer
f[0] = f_0 # initialbetingelse


# EULERS METODE
for i in range(N-1):
    f[i+1] = f[i] + derivert(f[i], k) * h # formel for å finne "neste steg" 

### PLOTTING
plt.plot(t, f) # plotter løsningen
plt.xlabel(r"$t$ [måneder]")
plt.ylabel(r"Antall harer ($f(t)$)")
plt.grid()



# KOMMENTAR TIL MODELL
# Modellen er selvfølgelig urealistisk, siden den ikke tar 
# hensyn til at noen kaniner dør.
