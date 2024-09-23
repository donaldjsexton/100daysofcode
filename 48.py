import os, time

while True:
    print("High Scores")
    print()
    name = input("Enter your initials: ").upper()
    score = input("Enter your score: ")
    print()

    f = open("highscores.txt", "a+")
    f.write(f"{name} {score}\n")
    f.close()

    print("Added")
    time.sleep(1)
    os.system("clear")
