import os
import random
import shutil
from datetime import datetime

backup_done = False

if not os.path.exists("ideas.txt"):
    open("ideas.txt", "w").close()

def backup_file():
    global backup_done
    if not backup_done and os.path.exists("ideas.txt"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"ideas_backup_{timestamp}.txt"
        shutil.copy("ideas.txt", backup_filename)
        print(f"Backup created as '{backup_filename}'")
        backup_done = True

def add(idea):
    backup_file()  
    with open("ideas.txt", "a") as f:  
        f.write(f"{idea}\n")

def show():
    with open("ideas.txt", "r") as f:
        ideas = f.read().splitlines()
    if ideas:
        print(random.choice(ideas))
    else:
        print("No ideas yet!")

while True:
    menu = input("1: Add idea\n2: Show Random Idea\nEnter Number: ")
    
    if menu == "1":
        idea = input("What is your idea? ")
        add(idea)
        print("Idea added!")
    elif menu == "2":
        show()
    else:
        print("Invalid choice, please enter 1 or 2.")
