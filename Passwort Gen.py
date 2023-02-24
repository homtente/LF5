# Anwendung:    Passwort Generator
# Autor:        Tom Hente
# Datum:        21.02.2023
# Version:      1.0


#Einbindung Bibiliothek Random
import random

#Erstellung zweier Listen für Werte als String und Werte als Output
werte = []
output_list = []

#While Schleife um 10 Werte zu generieren

while len(werte) < 10:                          #Laufe bis 10 Objekte in Liste Werte sind
    password = int(random.randint(0, 127))      #Generiere Random Passwort
    if password > 32:                           #Wenn Passwort größer als 32 ist füge es Liste hinzu
        werte.append(password)

for ziffern in werte:                           #Nehme alle Ziffern aus Werte
    value = int(ziffern)                        #nehme neue Variable Value und ändere Ziffern in int
    output_list.append(value)                   #Füge Value der Liste Output hinzu


#Gebe alle Objekte (von 0-9) aus der Liste Output aus, ohne Leerzeichen dazwischen (sep='')

print(chr(output_list[1]),chr(output_list[2]),chr(output_list[3]),chr(output_list[4]),chr(output_list[5]),
chr(output_list[6]),chr(output_list[7]),chr(output_list[8]),chr(output_list[9]),chr(output_list[0]),sep='')