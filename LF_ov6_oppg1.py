# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 6 - Oppgave 1

@author: Thomas Nyborg
"""

def f(x):
    """Funksjon tilsvarende likning som skal løses.
    Kommenter ut return som ikke skal brukes"""
    #return(2*x - 1) # Funksjon tilsvarende likning i a)
    return(x**2 - x - 6)  # Funksjon tilsvarende likning i b)

null = 1e-4 # nøyaktighet for nullpunktet

a = 0 # nedre startverdi for x
b = 5 # øvre startverdi for x

if f(a)*f(b) < 0: # funksjonsverdi i startpunkter har motsatt fortegn -> OK
    m = (a+b)/2 # regner ut midtpunkt
    
    while abs(f(m)) > null: # fortsetter algoritmen helt til funksjonsverdi i 
                            # midtpunktet er mindre enn 0
                            
        if f(a)*f(m) > 0: #f(a) og f(b) har samme fortegn
            a = m # setter midtpunkt som ny nedre verdi
        else:
            b = m # setter midtpunkt som ny øvre verdi
            
        m = (a+b)/2 # nytt midtpunkt
            
    print(f"Nullpunkt: x = {m} (nøyaktighet {null})")

else:
    print("Error. Startverdier har samme fortegn:")
    print(f"a = ({a},{f(a)})")
    print(f"b = ({b},{f(b)})")
    

    