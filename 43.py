import random

def generate_bingo_card():
    numbers = list(range(1, 91))
    random.shuffle(numbers)
    
    bingo_card = []
    for i in range(5):
        row = numbers[i*5:(i+1)*5]
        bingo_card.append(row)
    
    bingo_card[2][2] = "X"
    
    return bingo_card

def print_bingo_card(bingo_card):
    print("+" + "-" * 23 + "+")
    print("|  B |  I |  N |  G |  O |")
    print("+" + "-" * 23 + "+")
    for row in bingo_card:
        print("| " + " | ".join(f"{num:2}" if isinstance(num, int) else f"{num:2}" for num in row) + " |")
        print("+" + "-" * 23 + "+")

def main():
    while True:
        print("\nMenu:")
        print("1. Generate a new bingo card")
        print("2. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            bingo_card = generate_bingo_card()
            print_bingo_card(bingo_card)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()