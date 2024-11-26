#letzer Teil des Aufgabenzettels - Exceptions und Fehlerbehandlung



try:
    zahl = int(input("Bitte geben sie eine zahl ein:"))
    teiler = int(input("Bitte gib einen Teiler ein:"))


except:
    print("Das ist keine Zahl!")
    zahl = 1
    teiler = 1

try:
    result = zahl/teiler
    print (result)

except:
    print("Durch Null teilen darf man nicht!!")

if (zahl < 0):
    print("Achtung, die Zahl ist negativ!!")
else:
    print("die Zahl ist positiv, alles okay")