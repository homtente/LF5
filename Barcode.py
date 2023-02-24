# Anwendung:    Barcode Eingabe
# Autor:        Tom Hente
# Datum:        22.02.2023
# Version:      1.1


#Liste mit Barcodes

Liste_Zeichenkette_Strichcode = []
Liste_Zeichenkette_Ausgabe = []

#Eingabe Barcode

Barcode_Eingabe = str(input("Geben sie den Barcode ein!"))

#Bedingung Barcode  

if len(Barcode_Eingabe) is not 30:                                          #Wenn Barcode keine 30 Stellen hat 

    print ("Deine Eingabe hat zu wenige Stellen")                           #Gebe aus die Eingabe hat zu wenige Stellen

elif Barcode_Eingabe.isalpha():                                              #Wenn Buchstaben in der Eingabe enthalten sind

    print("Fehlercode 1 = String enthält nicht ausschließlich Ziffern")     #Gebe aus "String enthält nicht ausschließlich"

elif Barcode_Eingabe.isdigit():                                             #Wenn nur Zahlen enthalten sind

    print("Die Eingabe ist korrekt und besteht nur aus Ziffern")            #Gebe aus die Eingabe ist korrekt

    Liste_Zeichenkette_Strichcode.append(Barcode_Eingabe)                   #Füge Barcode_Eingabe Liste_Zeichenkette_Strichcode hinzu

    for s_8 in Liste_Zeichenkette_Strichcode:                               #Gehe Liste_Zeichenkette durch

        Nettogewicht = int(s_8[9:14])                                       #Nettogwicht = int von Stellen 9 bis 14 jedes Objekts

        Bruttogewicht = int(s_8[19:24])                                     #Bruttogewicht = int von Stellen 19 bis 24 jedes Objekts

#Wenn Bruttogewicht < Nettogewicht ist dann

        if (Bruttogewicht < Nettogewicht):                                  

            print("Fehlercode 2 = Nettogewicht ist größer als Bruttogewicht")   #Gebe aus Nettogewicht ist größer als Bruttogewicht


#Wenn Bruttogewicht >= Nettogewicht ist

        else: 
            Liste_Zeichenkette_Ausgabe.append(Barcode_Eingabe)              #Füge Barcode Eingabe Liste Ausgabe hinzu
            print("Der Barcode wurde der Liste hinzugefügt")                #Gebe aus Barcode wurde Liste hinzugefügt
