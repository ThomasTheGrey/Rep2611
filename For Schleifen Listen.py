# Aufgabe 11

Liste = [10,20,30,40,50]

for i in Liste:
    print (i)

# Aufgabe 12
j = 0
for i in Liste:
    j = j+i
print (j)

# Aufgabe 13

wort = input("Bitte geben sie ein Wort ein:\n")

for i in wort:
    print (i)

# Aufgabe 14

ListeNeu = []
for i in Liste:
    if (i>10):
        print (i)
        ListeNeu.append(i)
print (ListeNeu)

#Aufgabe 15
j = 0
for i in ListeNeu:
    print (f"Index ={j}", end="")
    print (f"Wert ={i}")
    j = j+1

#Aufgabe 16

for index, zahl in enumerate(ListeNeu):
    print(f"Index: {index}, Wert: {zahl}")

