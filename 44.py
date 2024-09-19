import random

def generate_bingo_card():
    numbers = list(range(1, 91))
    random.shuffle(numbers)
    
    bingo_card = []
    for i in range(5):
        row = numbers[i*5:(i+1)*5]
        bingo_card.append(row)
    
    bingo_card[2][2] = "B"
    
    return bingo_card

def print_bingo_card(bingo_card):
    print("+" + "-" * 23 + "+")
    print("|  B |  I |  N |  G |  O |")
    print("+" + "-" * 23 + "+")
    for row in bingo_card:
        print("| " + " | ".join(f"{num:2}" if isinstance(num, int) else f"{num:2}" for num in row) + " |")
        print("+" + "-" * 23 + "+")

def mark_bingo_card(bingo_card, number):
    for row in bingo_card:
        for i in range(len(row)):
            if row[i] == number:
                row[i] = "X"

def main():
    called_numbers = []
    bingo_card = generate_bingo_card()
    
    while True:
        print("\nMenu:")
        print("1. Enter a called number")
        print("2. Show called numbers")
        print("3. Show bingo card")
        print("4. Generate new bingo card")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                number = int(input("Enter the called number (1-90): "))
                if number < 1 or number > 90:
                    print("Invalid number. Please enter a number between 1 and 90.")
                elif number in called_numbers:
                    print("Number already called. Please enter a different number.")
                else:
                    called_numbers.append(number)
                    mark_bingo_card(bingo_card, number)
                    print_bingo_card(bingo_card)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            print("Called numbers:", called_numbers)
        elif choice == '3':
            print_bingo_card(bingo_card)
        elif choice == '4':
            bingo_card = generate_bingo_card()
            called_numbers = []
            print("New bingo card generated.")
            print_bingo_card(bingo_card)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()