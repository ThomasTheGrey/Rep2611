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



