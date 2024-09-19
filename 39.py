import random

listOfWords = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon']

word = random.choice(listOfWords)
letterPicked = []
wrongGuesses = 0
maxWrongGuesses = 6

hangmanStages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

while True:
    print("Fruit Hangman")
    letter = input("Enter a letter: ").lower()
    
    if letter in letterPicked:
        print("You already picked that letter.")
        continue
    
    letterPicked.append(letter)
    
    if letter not in word:
        wrongGuesses += 1
        print("Letter not in word.")
        print(hangmanStages[wrongGuesses])
        if wrongGuesses == maxWrongGuesses:
            print(f"You lost! The word was: {word}")
            break

    wordDisplay = ""
    for i in word:
        if i in letterPicked:
            wordDisplay += i + " "
        else: 
            wordDisplay += "_ "
    print(wordDisplay.strip())
    
    if all(letter in letterPicked for letter in word):
        print("Congratulations! You guessed the word!")
        playAgain = input("Would you like to play again? (yes/no): ").lower()
        if playAgain == 'yes':
            word = random.choice(listOfWords)
            letterPicked = []
            wrongGuesses = 0
        else:
            break
        