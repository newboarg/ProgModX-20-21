l0sning = input("Løsningsord?: ").upper()
ordet  = list(l0sning)
bokstaver = len(l0sning)
hangman = list("_"*bokstaver)

fors0k = 0
print(f"Ordet har {bokstaver} bokstaver.")
print(hangman)

while fors0k<bokstaver+4:
    print(f"Forsøk igjen: {bokstaver + 4 - fors0k}")
    
    gjett = input("Tipp en bokstav: ").upper()
    if gjett not in ordet:
        print("Feil tippet!")
    else:
        while gjett in ordet:
            index = ordet.index(gjett)
            hangman[index]=gjett
            ordet[index] = 0
    print(hangman)
        
    fors0k +=1
    if "_" not in hangman: #ferdig
        print("YOU WINS!")
        break
print(f"ordet var: {l0sning}")
