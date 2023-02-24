# Anwendung:    KundenID Genereator
# Autor:        Tom Hente
# Datum:        21.02.2023
# Version:      1.0




import random

KundenIDs_list = []

#random neun zahlen generieren

neun_zahlen = "".join(
[str(random.randint(0, 9))
for _ in range(10)]
)

#Quersumme aus den Neun Zahlen bilden

def quersumme(neun_zahlen):

    quersumme = 0 

    for zahlen in (neun_zahlen):        #Nehme jede Zahl/Objekt aus string neun_zahl
        quersumme += int(zahlen)        #Rechne jede Zahl als Integer + die Quersumme
    return quersumme                    #Gebe die neue Quersumme zurück

#KD an die Zahlen schreiben

KundenID = "KD" + neun_zahlen + str(quersumme(neun_zahlen))

#Lese hinterlegte Datei kunden_ids.txt aus, um festzustellen welche IDs vorhanden sind

try:

    with open('/Users/tomhente/Programmierung/Python/kunden_ids.txt', 'r') as f:
       KundenIDs_list = f.read().splitlines()

#Wenn kunden_ids.txt nicht vorhanden ist nehme eine neue Liste

except FileNotFoundError:

    KundenIDs_list = []

#Wenn KundenID nicht in KundenIDs_list ist dann

if KundenID not in KundenIDs_list:
    print("Diese Kunden ID ist noch frei!")     #Gebe aus diese KundenID ist noch frei
    KundenIDs_list.append(KundenID)             #Füge neue KundenID der Liste hinzu

#Öffene kunden_ids.txt als f im write Modus

    with open('/Users/tomhente/Programmierung/Python/kunden_ids.txt', 'w') as f:      
        f.write('\n'.join(KundenIDs_list))      #Schreibe KundenIDs_list als join plus Absatz in txt

#Wenn Kunden ID in KundenIDs_list ist 

elif KundenID in KundenIDs_list:
    print("Diese Kunden ID ist bereits vergeben")

#Gebe die KundenIDs_list und neue KundenID aus

print (KundenIDs_list)
print (KundenID)