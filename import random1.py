import random

anzahl = 1
werte = []
for i in range(anzahl):
    zahl = random.randint(0, 127)
    while zahl < 33:
        zahl = random.randint(0, 127)
    else:
        werte.append(zahl)