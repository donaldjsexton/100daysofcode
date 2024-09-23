import os, time, random

trumps ={}
trumps["Captain Kirk"] = {"Intelligence": 169, "Speed": 72, "Guile": 99, "Baldness": 4}
trumps["Captain Picard"] = {"Intelligence": 200, "Speed": 65, "Guile": 115, "Baldness": 126}
trumps["Captain Janeway"] = {"Intelligence": 175, "Speed": 90, "Guile": 99, "Baldness": 5}
trumps["Captain Sisko"] = {"Intelligence": 152, "Speed": 81, "Guile": 120, "Baldness": 200}

while True:
    print("TOP TRUMPS")
    print()
    print("Characters")
    print()
    for key in trumps.keys():
        print(key)
    user = input("Choose a character:\n> ")
    comp = random.choice (list(trumps.keys()))  
    print("Computer chose", comp)

    print("Choose your state: Intelligence, Speed, Guile, Baldness")

    answer = input("> ")

    print(f"{user}: {trumps[user][answer]}")
    print(f"{comp}: {trumps[comp][answer]}")

    if trumps[user][answer] > trumps[comp][answer]:
        print(user, "wins!")
    elif trumps[user][answer] < trumps[comp][answer]:
        print(comp, "wins!")
    else:
        print("It's a draw!")

    time.sleep(2)
    os.system("clear")