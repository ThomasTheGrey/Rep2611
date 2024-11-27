import sqlite3

# Aufgabe 1
connection = sqlite3.connect("benutzer.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

data = [("Anna", "Anna@hotmail.com", 22), ("Tom", "Tom@hotmail.com", 30), ("Lisa","Lisa@hotmail.com", 28)]
cursor.executemany("""
INSERT INTO users (name, email, age)
VALUES (?, ?,?)
""", data)
connection.commit()

# Aufgabe 2
cursor.execute("""
SELECT * FROM users
""")
results = cursor.fetchall()  # Alle Ergebnisse abrufen
for row in results:
    print(row)

#Aufgabe 3

Name = input("Bitte geben sie ihren Namen ein:\n")
Email = input("Bitte geben sie ihre email ein:\n")
Alter = int(input("Bitte geben sie ihr Alter ein:\n"))


cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?,?)", (Name, Email, Alter))

cursor.execute("""
SELECT * FROM users
""")
results = cursor.fetchall()  # Alle Ergebnisse abrufen
for row in results:
    print(row)

#Aufgabe 4

index = int(input("Bitte geben sie den index des Nutzers an:\n"))

Email = input("Bitte geben sie die neue Email Adresse ein:\n")


# SQL-Befehl, um die Email eines bestimmten Benutzers zu ändern
cursor.execute("""
UPDATE users
SET email = ?
WHERE id = ?
""", (Email, index))

# Änderungen speichern
connection.commit()

cursor.execute("""
SELECT * FROM users
""")
results = cursor.fetchall()  # Alle Ergebnisse abrufen
for row in results:
    print(row)

# SQL-Abfrage mit WHERE-Bedingung, um Einträge zu filtern
cursor.execute("""
SELECT id, name, email, age
FROM users
WHERE age > ?
""", (25,))

# Ergebnisse abrufen und ausgeben
results = cursor.fetchall()  # Alle Zeilen als Liste von Tupeln

# Durch die Ergebnisse iterieren und ausgeben
for row in results:
    print(row)

Name = input("Name des gesuchten Nutzers eingeben:\n")

cursor.execute("""
SELECT id, name, email, age
FROM users
WHERE name = ?
""", (Name,))

# Ergebnisse abrufen und ausgeben
results = cursor.fetchall()  # Alle Zeilen als Liste von Tupeln

# Durch die Ergebnisse iterieren und ausgeben
for row in results:
    print(row)


connection.close()

