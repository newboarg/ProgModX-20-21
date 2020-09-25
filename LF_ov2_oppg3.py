"""
Løsningsforslag
Øving 2 - Oppgave 3

@author: Thomas Nyborg
"""

def pytTrip(a,b,c):
    sider = [a,b,c]
    sider.sort()
    
    return(sider[0]**2 + sider[1]**2 == sider[2]**2)


a = int(input("Side 1?"))
b = int(input("Side 2?"))
c = int(input("Side 3?"))

if pytTrip(a,b,c):
    print("Huzzah! Dette er et Pytagoreisk trippel.")

else:
    print("NOPE. Dette er et ikke et Pytagoreisk trippel.")
