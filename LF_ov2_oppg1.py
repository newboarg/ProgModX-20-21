"""
Løsningsforslag
Øving 2 - Oppgave 1

@author: Thomas Nyborg
"""

def pi():
    return(3.14159265359)

def omkrets(r):
    return(2*pi()*r)

def areal(r):
    return(pi()*r**2)


r = float(input("Hva er radius i sirkelen? "))

print(f"Omkretsen i sirkelen er {omkrets(r):.2f}. \nArealet er {areal(r):.2f}")
