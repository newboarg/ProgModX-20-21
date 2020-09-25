"""
Løsningsforslag
Øving 2 - Oppgave 4

@author: Thomas Nyborg
"""

#funksjoner
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


#input
        
a = int(input("Tall?"))

print(f"Faktorer av {a}: {faktorer(a)}")

if isPrime(a):
    print(f"{a} er et primtall.")