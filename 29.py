def newPrint(color, word):
    if color == "red":
        print("\033[31m", word, sep="", end="")
    elif color == "green":
        print("\033[32m", word, sep="", end="")
    elif color == "yellow":
        print("\033[33m", word, sep="", end="")
    elif color == "blue":
        print("\033[34m", word, sep="", end="")
    elif color == "purple":
        print("\033[35m", word, sep="", end="")
    else:
        print("\033[30m", word, sep="", end="")

print("Super Subroutine")

while True:
    print("\nChoose a color (red, green, yellow, blue, purple) or type 'exit' to quit:")
    color = input("Color: ").strip().lower()
    if color == "exit":
        break
    word = input("Enter the word to print: ").strip()
    newPrint(color, word)
    print("\033[0m")  # Reset color

print("Program terminated.")