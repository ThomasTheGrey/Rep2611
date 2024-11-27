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


connection.close()
