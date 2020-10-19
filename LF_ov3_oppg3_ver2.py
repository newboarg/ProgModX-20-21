valor = {"kronestykke" : 1, 
         "femkrone" : 5, 
         "tikrone" : 10, 
         "tjuekrone" : 20, 
         "femtilapp" : 50, 
         "hundrelapp" : 100, 
         "tohundrelapp" : 200, 
         "femhundrelapp" : 500, 
         "tusenlapp" : 1000 }

# sorterer dict fra høyeste til laveste valør
valor = {k:v for k, v in sorted(valor.items(), key = lambda item: item[1], reverse=1)}

# oppretter dict for kassabeholdning
kasse = {k:5 for k in valor}

def vekslepenger(pris, betalt, prnt = 1):
    """
    Funksjon som tar inn pris og betalt beløp, og returnerer en dict med 
    vekslepenger som antall av ulike valører.
    Argumentet prnt avgjør om funksjonen printer ut vekslepengene.

    """
    tilbake = betalt - pris
    
    veksel = {k:0 for k in valor} # dict for å holde vekslepenger som gis tilbake
        
    if tilbake<0:
        print("For lite betaling!")
        return()
    else:   
        # oversetter mellom beløp og antall valører
        while tilbake > 0:
           for val in valor:
               while tilbake >= valor[val]:
                   tilbake -= valor[val]
                   veksel[val] += 1
           
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
    print(f"$$$ UTTAK $$$\nTar ut {belop} kr.")
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