rolodex =[]

def printList():
    print()
    for name in rolodex:
        print(name)
    print()

while True:
    firstName = input("Enter First Name: ").strip().capitalize()
    lastName = input("Enter Last Name: ").strip().capitalize()
    name= f"{firstName} {lastName}"
    if name not in rolodex:
        rolodex.append(name)
    else:
        print("Name already exists in the rolodex.")
    printList()