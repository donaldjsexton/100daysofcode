import sqlite3
import datetime
import os
import time

db = sqlite3.connect("diary.db")
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    entry TEXT NOT NULL
)
''')
db.commit()

def addEntry():
    time.sleep(1)
    os.system("clear")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Diary entry for {timestamp}")
    print()
    entry = input(">")
    cursor.execute('''
        INSERT INTO entries (timestamp, entry)
        VALUES (?, ?)
    ''', (timestamp, entry))
    db.commit()

def viewEntry():
    cursor.execute('SELECT timestamp, entry FROM entries ORDER BY id DESC')
    entries = cursor.fetchall()
    for entry in entries:
        time.sleep(1)
        os.system("clear")
        print(f"{entry[0]}: {entry[1]}")
        print()
        opt = input("Next or exit? > ")
        if opt.lower()[0] == "e":
            break

def checkPassword():
    password = "itchymonkey123"
    user_input = input("Enter password: ")
    return user_input == password

if checkPassword():
    while True:
        os.system("clear")
        menu = input("1: Add Entry\n2: View Entries\n> ")
        if menu == "1":
            addEntry()
        elif menu == "2":
            viewEntry()
        else:
            print("Invalid option.")
else:
    print("Incorrect password.")
