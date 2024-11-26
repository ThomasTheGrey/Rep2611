# Testcomment to check remote 2
#Aufgabe 1
startwert = 10
zwischenwert = startwert + 5
endwert = zwischenwert * 2
print (F"{startwert},{zwischenwert},{endwert}")

#Aufgabe 2

zahl = input("Bitte geben Sie eine Zahl ein:\n")

try:
    zahl = float(zahl)  # oder `int(eingabe)` für Ganzzahlen
    print("Die Eingabe ist eine Zahl.")
except ValueError:
    print("Die Eingabe ist keine Zahl.")

if (zahl % 2 == 0):
    print("die Zahl ist gerade!")
else: print("die Zahl ist ungerade")

if (zahl > 100):
    print("die Zahl ist größer als 100!")
else:
    if (zahl == 100):
        print("die Zahl ist = 100!")
    else:
        print("die Zahl ist kleiner als 100!")

if ((zahl <= 100)and(zahl>=50)):
    print("Die Zahl liegt zwischen 50 und 100")
else:
    print("Die Zahl liegt nicht zwischen 50 und 100")



password = input("Bitte geben sie jetzt das Passwort ein!\n")
if password == "123456":
    print("Access granted")
else:
    print("Access denied!")

alter = input("Bitte geben sie ihr Alter ein")
if (alter>=18):
    print("Du darfst Auto fahren!")
else:
    if (alter>=16):
        print("Du darfst den Führerschein machen")
    else:
        print("Du bist zu jung für den Führerschein")

