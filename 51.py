import os, random

if not os.path.exists("ideas.txt"):
    open("ideas.txt", "w").close()

def add(idea):
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
