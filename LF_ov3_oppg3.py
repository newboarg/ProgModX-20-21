# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 3 - Oppgave 3

@author: Thomas Nyborg
"""

# GLOBALE VARIABLER
valor = {"kronestykke" : 1, 
         "femkrone" : 5, 
         "tikrone" : 10, 
         "tjuekrone" : 20, 
         "femtilapp" : 50, 
         "hundrelapp" : 100, 
         "tohundrelapp" : 200, 
         "femhundrelapp" : 500, 
         "tusenlapp" : 1000 }

# oppretter en kassabeholdning med 5 av hver valør
kasse = {}
for key in valor:
    kasse[key] = 5


# FUNKSJONER
def vekslepenger(pris, betalt, prnt = 1):
    """
    Funksjon som tar inn pris og betalt beløp, og returnerer en dict med 
    vekslepenger som antall av ulike valører.
    Argumentet prnt avgjør om funksjonen printer ut vekslepengene.

    """
    tilbake = betalt - pris
    
    veksel = {} # dict for å holde vekslepenger som gis tilbake
    for key in valor:
        veksel[key] = 0  
        
    if tilbake<0:
        print("For lite betaling!")
        return()
    else:
        
        while tilbake>0:
            if tilbake >= 1000:
                veksel["tusenlapp"] += 1
                tilbake -= 1000
            elif tilbake >= 500:
                veksel["femhundrelapp"] += 1
                tilbake -= 500
            elif tilbake >= 200:
                veksel["tohundrelapp"] += 1
                tilbake -= 200
            elif tilbake >= 100:
                veksel["hundrelapp"] += 1
                tilbake -= 100 
            elif tilbake >= 50:
                veksel["femtilapp"] += 1
                tilbake -= 50
            elif tilbake >= 20:
                veksel["tjuekrone"] += 1
                tilbake -= 20
            elif tilbake >= 10:
                veksel["tikrone"] += 1
                tilbake -= 10
            elif tilbake >= 5:
                veksel["femkrone"] += 1
                tilbake -= 5
            elif tilbake >= 1:
                veksel["kronestykke"] += 1
                tilbake -= 1
        if prnt:  
            print(f"Vekslepenger (betalt {betalt} kr, pris {pris} kr):")
            print_valorer(veksel)
        
        return(veksel)
    

def innskudd(val, antall):
    """Funksjon for innskudd (oppgave d)."""
    
    print(f"$$$ INNSKUDD $$$\nSetter inn {antall} {val}...")
    print("Beholdning før innskudd:")
    print_valorer(kasse)
    
    kasse[val] += antall
    
    print("Beholdning etter innskudd:")
    print_valorer(kasse)
    
    return(kasse)
    
def uttak(belop):
    """Funksjon for uttak (oppgave d)."""
    print(f"$$$ UTTAK $$$\nTar ut {ut} kr.")
    print("Beholdning før uttak:")
    print_valorer(kasse)
    
    valorer = vekslepenger(0,belop, prnt = 0) 
    # bruker funksjonen vekslepenger til å få beløpet i riktige valører
 
    for val in valorer:
        kasse[val] -= valorer[val]
        if kasse[val] < 0:
            print(f"For lite av valør {val} i kassa!")
            return(0)
        
    print("Beholdning etter uttak:")
    print_valorer(kasse)

    return(kasse)
    


def endre_beholdning(inn_ut, belop):
    """Funksjon for innskudd/uttak (oppgave e)."""
    
    if inn_ut == "inn": # innskudd
        valorer = vekslepenger(0,belop, prnt = 0) 
        # bruker funksjonen vekslepenger til å få beløpet i riktige valører

        for val in valorer:
            kasse = innskudd(val, valorer[val])
    
    elif inn_ut == "ut": # uttak
        kasse = uttak(belop)
        
    return(kasse)

def print_valorer(vals):
    """ Funksjon som printer ut key-value-par i en dict.
    """
    for item in vals:
        print(item, ":", vals[item])
    print("\n")
    

# SKRIPT 
# oppgave b): eksempel, vekslepenger
pris = 132
betalt = 200
vekslepenger(pris, betalt)


# oppgave d): eksempel, innskudd
kasse = innskudd("tusenlapp", 5)


# oppgave d): eksempel,uttak
ut = 4783 #sum som skal tas ut
kasse = uttak(ut)

# oppgave e): eksempel, bruk av sammensatt funksjon
endre_beholdning("ut", 3201)