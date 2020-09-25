"""
Løsningsforslag
Øving 2 - Oppgave 2

@author: Thomas Nyborg
"""

def leg(alder):
    return(alder>=18)


alder = int(input("Hvor gammel er du?"))

if leg(alder):
    print("Du er gammel nok til å kjøre bil.")
    
else:
    print("Du er ikke gammel nok til å kjøre bil.")
