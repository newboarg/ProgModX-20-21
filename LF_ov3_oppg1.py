# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 3 - Oppgave 1

@author: Thomas Nyborg
"""

def faktorer(x, reverse = 1):
    """Dette er en funksjon som returnerer alle faktorene til et argument x.
    argumentet reverse avgjør om faktorene returneres i stigende (reverse=0)
    eller synkende (reverse=1, default) rekkefølge."""
    
    faktorer = []
    
    for i in range(1,x+1):
        if x%i==0:
            faktorer.append(i)
    
    if reverse:
        faktorer.reverse() #synkende rekkefølge
        
    return(faktorer)



def isPrime(x):
    """Denne funksjonen sjekker om et tall x er et primtall. 
    Bruker funksjonen faktorer(x)."""
    
    f=faktorer(x)
    return(len(f)==2) #hvis det er bare to faktorer (1 og tallet selv) er x et primtall


def primtallsum(grense):
    """Denne funksjonen finner primtall fra 2 og oppover og summerer dem helt 
    til en grense for summen er nådd"""
    s = 0 # variabel for sum av primtall
    i = 2 # indeks for å sjekke primtall
    primtall = [] #liste for å lagre primtall

    while s < grense:
        if isPrime(i):
            primtall.append(i)
            s += i
        i += 1
        
    for i, j in enumerate(primtall):
        if isPrime(i):
            print(f"Indeks: {i}, Tall: {j}") # printer indekser som er primtall
    return(len(primtall))



# SKRIPT

sum_grense = 10000
print(f"Antall primtall for å nå primtallsum {sum_grense}: {primtallsum(sum_grense)}")
