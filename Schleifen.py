
# Teil 1
a = 0

while (a < 11):
    print (a)
    a += 1

# Teil 2

a = int(input("Bitte geben Sie Zahlen ein für die Addition (0 um zu beenden):\n"))
z = a
while (a!=0):
    a = int(input("Bitte die nächste Zahl eingeben:\n"))
    z = z+a

print (z)

# Teil 3

password = "Password123"
eingabe = ""
while (password != eingabe):
    eingabe = input("Bitte geben sie das Password ein:\n")

print("Glückwunsch! Das war das richtige Passwort.")