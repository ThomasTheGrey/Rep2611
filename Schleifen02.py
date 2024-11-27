Zahlen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Aufgabe 4
print("Aufgabe 4")
ZahlenA4 = Zahlen[0:10]

for i in ZahlenA4:
    print (i)

# Aufgabe 5
print("Aufgabe 5.1")
ZahlenA51 = Zahlen[1::2]

for i in ZahlenA51:
    print (i)

print("Aufgabe 5.2")
ZahlenA52 = Zahlen[4::5]

for i in ZahlenA52:
    print (i)

#Aufgabe 6
print("Aufgabe 6")
for i in [1,2,3,4,5]:
    print("")
    for j in [1,2,3,4,5]:
        print ("*", end="")


# Aufgabe 7
print("\nAufgabe 7")
ZahlenA7 = Zahlen[9::-1]
print (ZahlenA7)
for i in ZahlenA7:
    print (i)