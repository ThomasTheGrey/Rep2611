# Erstellen einer Quizfragen Datenbank

import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect("questions.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer_correct TEXT NOT NULL,
    answer_wrong01 TEXT NOT NULL,
    answer_wrong02 TEXT NOT NULL,
    answer_wrong03 TEXT NOT NULL,
    level INTEGER   
)
""")
connection.commit()

# Funktion zur Frageerstellung, Eingabe durch den Nutzer

def frageerstellung():
    Frage = input("Bitte geben Sie eine neue Quizfrage ein:\n")
    AntwortK = input("Bitte die korrekte Antwort eingeben:\n")
    AntwortF1 = input("Bitte eine falsche Antwort (1) eigeben:\n")
    AntwortF2 = input("Bitte eine falsche Antwort (2) eigeben:\n")
    AntwortF3 = input("Bitte eine falsche Antwort (3) eigeben:\n")
    Level = int(input("Wie schwierig zu beantworten (1-3) ist diese Frage?"))


    cursor.execute("INSERT INTO questions (question, answer_correct, answer_wrong01, answer_wrong02, answer_wrong03, level) VALUES (?, ?, ?, ?, ?)", (Frage, AntwortK, AntwortF1, AntwortF2, AntwortF3, Level))

def fragen(n):
    cursor.execute("""
    SELECT question, answer_correct, answer_wrong01, answer_wrong02, answer_wrong03, level
    FROM questions
    WHERE id = ?
    """, (n,))

    result = cursor.fetchone()

    print(f"Hier unsere erste Frage: {result[1]}")
    print(f"Was ist die richtige Antwort?\n[A]{result[2]}\n[B]{result[3]}\n[C]{result[4]}\n[D]{result[5]}")

frageerstellung()
frageerstellung()
fragen(1)

cursor.execute("SELECT * FROM questions")
for row in cursor.fetchall():
    print(row)