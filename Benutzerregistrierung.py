""" 1.	Erstellen Sie ein Benutzerregistrierungssystem mit folgenden Funktionen:
o	Benutzer registrieren (name, email, passwort in die Datenbank einfügen).
o	Benutzer-Login:
	Überprüfen Sie, ob email und passwort korrekt sind.
o	Anzeigen aller registrierten Benutzer.
"""

import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect("user.db")
cursor = connection.cursor()

# Tabelle für Nutzer erstellen (falls noch nicht existiert)
cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
connection.commit()

Ende = 0

while (Ende == 0):
    Name = input("Bitte neuen Nutzernamen eingeben:\n")
    Email = input("Bitte Email eingeben:\n")
    Password = input("Bitte Passwort eingeben:\n")

    cursor.execute("INSERT INTO user (name, email, password) VALUES (?, ?, ?)", (Name, Email, Password))

    if (Name == ""):
        Ende = 1

cursor.execute("SELECT * FROM user")
for row in cursor.fetchall():
    print(row)

Name = input("Bitte geben sie ihren Login Namen ein:\n")
Password = input("Passwort?\n")

# SQL-Abfrage mit WHERE-Bedingung, um Einträge zu filtern
cursor.execute("""
SELECT id, name, email, password
FROM user
WHERE name = ?
""", (Name,))  # Platzhalter für den Parameter verwenden

# Ergebnisse abrufen und ausgeben
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)