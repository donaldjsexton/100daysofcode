def colorChange(color):
    if color == "r":
        print("\033[31m", end="")
    elif color == " ":
        print("\033[37m", end="")
    elif color == "g":
        print("\033[32m", end="")
    elif color == "y":
        print("\033[33m", end="")
    elif color == "b":
        print("\033[34m", end="")
    elif color == "p":
        print("\033[35m", end="")

sentence = input("What sentence would you like to rainbow-ify? ")
for letter in sentence:
    colorChange(letter.lower())
    print(letter, end="")
print()