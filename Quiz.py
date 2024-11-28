#Alte DB löschen
import os
import random

# Name der Datenbankdatei
datenbank_name = "questions.db"

# Überprüfen, ob die Datei existiert
if os.path.exists(datenbank_name):
    os.remove(datenbank_name)  # Datei löschen
    print(f"Datenbank '{datenbank_name}' wurde gelöscht.")
else:
    print(f"Datenbank '{datenbank_name}' existiert nicht.")


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
    level TEXT NOT NULL   
)
""")
connection.commit()



# Funktion zur Frageerstellung, Eingabe durch den Nutzer
score = 0
def frageerstellung():
    Frage = input("Bitte geben Sie eine neue Quizfrage ein:\n")
    AntwortK = input("Bitte die korrekte Antwort eingeben:\n")
    AntwortF1 = input("Bitte eine falsche Antwort (1) eigeben:\n")
    AntwortF2 = input("Bitte eine falsche Antwort (2) eigeben:\n")
    AntwortF3 = input("Bitte eine falsche Antwort (3) eigeben:\n")
    Level = (input("Wie schwierig zu beantworten (A-C) ist diese Frage?"))


    cursor.execute("INSERT INTO questions (question, answer_correct, answer_wrong01, answer_wrong02, answer_wrong03, level) VALUES (?, ?, ?, ?, ?, ?)", (Frage, AntwortK, AntwortF1, AntwortF2, AntwortF3, Level))

def fragen(n):
    cursor.execute("""
    SELECT question, answer_correct, answer_wrong01, answer_wrong02, answer_wrong03, level
    FROM questions
    WHERE id = ?
    """, (n,))

    result = cursor.fetchone()
    liste =[1,2,3,4]
    random.shuffle(liste)
    print(f"Hier unsere erste Frage: \n{result[0]}")
    antwort =input(f"Was ist die richtige Antwort?\n[a]{result[liste[0]]}\n[b]{result[liste[1]]}\n[c]{result[liste[2]]}\n[d]{result[liste[3]]}\n")
    global score
    if (antwort == "a" and liste[0]==1):
        print("Jawohl!")
        score = score + 1
    else:
        if (antwort == "b" and liste[1]==1):
            print("Genau!")
            score = score + 1
        else:
            if (antwort == "c" and liste[2]==1):
                print("Korrekt!")
                score = score + 1
            else:
                if (antwort == "d" and liste[3]==1):
                    print("Das ist richtig!")
                    score = score+1
                else:
                    print("Leider falsch.")

def quiz():
    cursor.execute("SELECT COUNT(*) FROM questions")
    anzahl = cursor.fetchone()[0]
    liste_fragen = (list(range(anzahl)))
    random.shuffle(liste_fragen)
    for i in range(anzahl):
        print (i)
        fragen(liste_fragen[i]+1)

eingabe = ""
while (eingabe != "x"):
    eingabe=input("Was möchtest du gerne machen?\nf - Frage erstellen\nq - Quiz starten\nx - Programm beenden\n")
    if eingabe == "f":
        frageerstellung()
    else:
        if eingabe == "q":
            quiz()
            print(f"Dein Score ist:{score}")
        else:
            print("Tschüss!")




cursor.execute("SELECT * FROM questions")
for row in cursor.fetchall():
    print(row)

