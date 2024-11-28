# Erstellen einer Quizfragen Datenbank

import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect("user.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer_correct TEXT NOT NULL,
    answer_wrong01 TEXT NOT NULL,
    answer_wrong02 TEXT NOT NULL,
    answer_wrong03 TEXT NOT NULL   
)
""")
connection.commit()

# Funktion zur Frageerstellung, Eingabe durch den Nutzer

def frageerstellung():
    Frage = input("Bitte neuen Nutzernamen eingeben:\n")
    AntwortK = input("Bitte die korrekte Antwort eingeben:\n")
    AntwortF1 = input("Bitte eine falsche Antwort (1) eigeben:\n")
    AntwortF2 = input("Bitte eine falsche Antwort (2) eigeben:\n")
    AntwortF3 = input("Bitte eine falsche Antwort (3) eigeben:\n")


    cursor.execute("INSERT INTO user (question, answer_correct, answer_wrong01, answer_wrong02, answer_wrong03) VALUES (?, ?, ?, ?, ?)", (Frage, AntwortK, AntwortF1, AntwortF2, AntwortF3))

cursor.execute("SELECT * FROM questions")
for row in cursor.fetchall():
    print(row)