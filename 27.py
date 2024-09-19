import random, os, time

def rollDice(side):
    result = random.randint(1, side)
    return result

def health ():
    healthStat = ((rollDice(6) * rollDice(12))/2)+10
    return healthStat

def strength ():
    strengthStat = ((rollDice(6) * rollDice(8))/2)+12
    return strengthStat

while True:
   print("⚔️ Character Stats ⚔️")
   print()
   name = input("Enter your character's name: ")
   type = input("Enter your character's race: ")
   print()
   print(name)
   print("Health:", health())
   print("Strength:", strength())
   print()
   print("May your name go down in Legend!")
   print()
   again = input("Would you like to create another character? (yes/no): ")
   if again == "no":
         break
   time.sleep(1)
   os.system('clear')