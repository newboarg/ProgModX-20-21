# -*- coding: utf-8 -*-
"""
Løsningsforslag
Øving 4 - Oppgave 2

@author: Thomas Nyborg
"""
import random

# oppgave a
f = open("tilfeldigetall.txt", "w")

for i in range(100):
    f.write(str(random.randint(0,100)))
    if i != 99:
        f.write(",")

f.close()

# oppgave b
f = open("tilfeldigetall.txt", "r")

tall = f.read().split(",")
tall.sort(reverse = 1)

print(tall)