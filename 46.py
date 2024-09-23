import random

RED = "\033[91m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
YELLOW = "\033[93m"
GREY = "\033[90m"
RESET = "\033[0m"
WHITE = "\033[97m"

def colored_text(text, color):
    return f"{color}{text}{RESET}"

moke_dex = {}

def add_beast():
    name = input("Enter the name of the beast: ").strip()
    beast_type = input("Enter the type of the beast (Fire, Water, Air, Electric, Stone): ").strip().capitalize()
    special_move = input("Enter the special move of the beast: ").strip()

    starting_hp = random.randint(50, 100)
    starting_ap = random.randint(10, 50)

    moke_dex[name] = {
        "Type": beast_type,
        "Special Move": special_move,
        "Starting HP": str(starting_hp),
        "Starting AP": str(starting_ap)
    }

    color = {
        "Fire": RED,
        "Water": BLUE,
        "Air": PURPLE,
        "Electric": YELLOW,
        "Stone": GREY
    }.get(beast_type, WHITE)

    print("\nMoke-Dex Entry:")
    print(f"{color}Name: {WHITE}{name}{color}")
    print(f"Type: {WHITE}{beast_type}{color}")
    print(f"Special Move: {WHITE}{special_move}{color}")
    print(f"Starting HP: {WHITE}{starting_hp}{color}")
    print(f"Starting AP: {WHITE}{starting_ap}{color}{RESET}")

def view_beasts():
    if not moke_dex:
        print("Moke-Dex is empty.")
    else:
        for name, details in moke_dex.items():
            beast_type = details["Type"]

            color = {
                "Fire": RED,
                "Water": BLUE,
                "Air": PURPLE,
                "Electric": YELLOW,
                "Stone": GREY
            }.get(beast_type, WHITE)

            print(f"\n{color}Name: {WHITE}{name}{color}")
            print(f"Type: {WHITE}{details['Type']}{color}")
            print(f"Special Move: {WHITE}{details['Special Move']}{color}")
            print(f"Starting HP: {WHITE}{details['Starting HP']}{color}")
            print(f"Starting AP: {WHITE}{details['Starting AP']}{color}{RESET}")

def main():
    while True:
        print("""
        +-----------------------------+
        |                             |
        |        MOKE-DEX MENU        |
        |                             |
        +-----------------------------+
        | 1. Add a new beast          |
        | 2. View Moke-Dex            |
        | 3. Exit                     |
        +-----------------------------+
        """)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_beast()
        elif choice == "2":
            view_beasts()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()