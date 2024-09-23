print("List Generator ")
while True:
    starting_number = int(input("\nEnter the starting number: "))
    ending_number = int(input("Enter the ending number: "))
    step = int(input("Enter the increment at which you wish to count: "))
    print("\nList of numbers from", starting_number, "to", ending_number, "with increment of", step, "is:")
    print(list(range(starting_number, ending_number, step)))
    if input("\nEnter 'yes' to generate another list or 'no' to exit: ").lower() == 'no':
        break