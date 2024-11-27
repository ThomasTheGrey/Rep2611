import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect("todo_liste.db")
cursor = connection.cursor()

# Tabelle für Aufgaben erstellen (falls noch nicht existiert)
cursor.execute("""
CREATE TABLE IF NOT EXISTS aufgaben (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titel TEXT NOT NULL,
    status TEXT NOT NULL
)
""")
connection.commit()

# Funktion 1: Aufgabe hinzufügen
def aufgabe_hinzufuegen(titel, status="offen"):
    cursor.execute("""
    INSERT INTO aufgaben (titel, status)
    VALUES (?, ?)
    """, (titel, status))
    connection.commit()
    print(f"Aufgabe '{titel}' wurde hinzugefügt.")

# Funktion 2: Alle Aufgaben anzeigen
def alle_aufgaben_anzeigen():
    cursor.execute("SELECT * FROM aufgaben")
    aufgaben = cursor.fetchall()
    if aufgaben:
        print("Alle Aufgaben:")
        for aufgabe in aufgaben:
            print(f"ID: {aufgabe[0]} | Titel: {aufgabe[1]} | Status: {aufgabe[2]}")
    else:
        print("Keine Aufgaben in der Liste.")

# Funktion 3: Aufgabe als erledigt markieren
def aufgabe_erledigt_markieren(aufgabe_id):
    cursor.execute("""
    UPDATE aufgaben
    SET status = 'erledigt'
    WHERE id = ?
    """, (aufgabe_id,))
    connection.commit()
    print(f"Aufgabe mit ID {aufgabe_id} wurde als erledigt markiert.")

# Funktion 4: Aufgabe löschen
def aufgabe_loeschen(aufgabe_id):
    cursor.execute("""
    DELETE FROM aufgaben
    WHERE id = ?
    """, (aufgabe_id,))
    connection.commit()
    print(f"Aufgabe mit ID {aufgabe_id} wurde gelöscht.")

# Testaufrufe (Beispiel)

# Aufgabe hinzufügen

aufgabe = input("Bitte eine Aufgabe eingeben:\n")
aufgabe_hinzufuegen(aufgabe)


# Alle Aufgaben anzeigen
alle_aufgaben_anzeigen()

# Aufgabe als erledigt markieren

index = int(input("welche Aufgabe soll als erledigt markiert werden?\n"))
aufgabe_erledigt_markieren(index)

# Alle Aufgaben nach der Änderung anzeigen
alle_aufgaben_anzeigen()

# Aufgabe löschen

index = int(input("Welche Aufgabe soll gelöscht werden?\n"))
aufgabe_loeschen(index)

# Alle Aufgaben nach der Löschung anzeigen
alle_aufgaben_anzeigen()

# Verbindung zur Datenbank schließen
connection.close()
