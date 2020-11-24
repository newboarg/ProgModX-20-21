# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 5 - Oppgave 1

@author: Thomas Nyborg
"""
import numpy as np
from matplotlib import pyplot as plt

def f(x): # definerer funksjonen f(x)
    return(x**2 - 4*x + 5)

def analytisk(x): # funksjon for den analytiske deriverte (utregnet)
    return(2*x- 4)

def derivert(f, x, h): # definerer en funksjon for den deriverte ved Newtons kvotient
    return((f(x+h) - f(x))/h)

xmin = 2
xmax = 5
h = 1e-2

N = int((xmax-xmin)/h)+1 # antall x-verdier

x = np.linspace(xmin, xmax, N) # lager et array med N x-verdier fra xmin til xmax
df = derivert(f, x, h) # lager et array med verdier for den deriverte av f for gitt h
df_analytisk = analytisk(x) # lager et array med verdier for den analytisk deriverte


plt.plot(x, f(x), label = 'f(x)')
plt.plot(x, df, 'b', label = "numerisk") #plotter den numeriske deriverte
plt.plot(x, df_analytisk, 'r', linestyle = '--', label = "analytisk") #plotter den analytiske deriverte
plt.title(f"h={h}")
plt.xlabel("x")
plt.ylabel(r"Derivert")
plt.grid("both")
plt.ylim()
plt.legend()