import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100,000 ")
print("Try to guess the number in as few attempts as possible.\n")

while True:
    number = random.randint(1, 100000)
    guess = 0
    attempts = 0
    input("Press Enter to start...")
    
    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Higher!")
        elif guess > number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    
    play_again = input("Would you like to play again? Enter 'yes' or 'no': ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
