import os, time, random

def add ():
    os.system("clear")
    f = open("ideas.txt", "a+")
    f.write(f"{idea}\n")
    f.close()

def show ():
    f = open("ideas.txt", "r")
    ideas = f.read().split("\n")
    ideas.remove("")
    print(random.choice(ideas))

while True:
    menu = input("1: Add idea\n2: Show Random Idea\nEnter Number: ")
    if menu == "1":
        add()
        idea = input("What is your idea? ")
    else:
        show()
