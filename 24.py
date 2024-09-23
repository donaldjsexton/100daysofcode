import random

def dice(sides):
    return random.randint(1, sides)

print("Infinity Dice Roller")

while True:
    sides = int(input("How many sides does the dice have? "))
    print("You rolled a", dice(sides))
    
    tryAgain = input("Would you like to roll again? (y/n) ")
    if tryAgain.lower() != "y":
        break