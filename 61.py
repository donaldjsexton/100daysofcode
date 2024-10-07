import sqlite3
import datetime
import os
import time

db = sqlite3.connect("tweeter.db")
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tweets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tweet TEXT NOT NULL,
    timestamp DATETIME NOT NULL
)
''')
db.commit()

def addTweet():
    tweet = input("Tweet Yourself: ")
    timestamp = datetime.datetime.now()

    cursor.execute('''
        INSERT INTO tweets (tweet, timestamp) 
        VALUES (?, ?)
    ''', (tweet, timestamp))
    db.commit()

    time.sleep(1)
    os.system("clear")

def viewTweets():
    cursor.execute('SELECT tweet, timestamp FROM tweets')
    tweets = cursor.fetchall()

    if tweets:
        for tweet in tweets:
            print(f"{tweet[1]} - {tweet[0]}")
    else:
        print("No tweets yet!")
    input("Press Enter to return to the menu...")

while True:
    print("Tweeter")
    menu = input("1: Add Tweet\n2: View Tweets\n> ")
    if menu == "1":
        addTweet()
    elif menu == "2":
        viewTweets()
    else:
        print("Invalid option. Please try again.")
