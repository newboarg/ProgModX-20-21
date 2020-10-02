#GLOBAL VARIABEL: Liste med lag i tippeligaen
tippeligaen = ["Molde", "Bodø/Glimt", "Odd", "Rosenborg", "Viking", "KBK", 
            "Brann", "FK Haugesund", "Vålerenga", "Lillestrøm", "Stabæk", 
            "Strømsgodset", "TIL", "Mjøndalen", "Ranheim", "Sarpsborg"]
tippeligaen.sort()   
 
#Funksjoner
def listehandtering(lag): #lag har type string
    
    lag = lag.split()
    
    for item in tippeligaen:
        if item not in lag:
            lag.append(item)
    
    lag.sort()
    
    return(lag)

def opprykk(tippeligalag, oboslag):
    tippeligaen.remove(tippeligalag)
    tippeligaen.append(oboslag)
    tippeligaen.sort()
    return(tippeligaen)


#Oppgave a
lag = "Rosenborg Molde Brann Strømsgodset Ålesund Lillestrøm Ranheim"

print("Oppgave a)")
print(listehandtering(lag))


#Oppgave b
tippeligaen = opprykk("Rosenborg", "Skeid") #Skeid rykker opp, Rosenborg rykker ned
print("Oppgave b)")
print(tippeligaen)
