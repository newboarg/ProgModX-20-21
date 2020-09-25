"""
Løsningsforslag
Øving 2 - Oppgave 5

@author: Thomas Nyborg
"""

# Bruker funksjonen faktorer() fra oppgave 4 til å løse oppgave 5.

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

#Kommentar: vi trenger egentlig bare å sjekke opp til x/2 (for partall) 
#eller til x/3 (for oddetall). Hvorfor?


def isPrime(x):
    """Denne funksjonen sjekker om et tall x er et primtall. 
    Bruker funksjonen faktorer(x)."""
    
    f=faktorer(x)
    return(len(f)==2) #hvis det er bare to faktorer (1 og tallet selv) er x et primtall


#input
        
a = int(input("Tall?"))

print(f"Faktorer av {a}: {faktorer(a)}")

if isPrime(a):
    print(f"{a} er et primtall.")