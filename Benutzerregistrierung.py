""" 1.	Erstellen Sie ein Benutzerregistrierungssystem mit folgenden Funktionen:
o	Benutzer registrieren (name, email, passwort in die Datenbank einfügen).
o	Benutzer-Login:
	Überprüfen Sie, ob email und passwort korrekt sind.
o	Anzeigen aller registrierten Benutzer.
"""

import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect("nutzer.db")
cursor = connection.cursor()

# Tabelle für Aufgaben erstellen (falls noch nicht existiert)
cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
    password TEXT NOT NULL
)
""")
connection.commit()

Ende = TRUE

while (Ende):
