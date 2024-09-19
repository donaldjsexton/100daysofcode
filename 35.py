import os, time
todolist = []

def printlist():
    print()
    for item in todolist:
        print(item)
    print()

while True:
    menu = input("ToDolist Manager\n\nDo you want to add, edit, delete, delete all, or view your list? ")
    if menu == "add":
        item = input("What would you like to add to your list? ")
        todolist.append(item)
    elif menu == "edit":
        old_item = input("Which item would you like to edit? ")
        if old_item in todolist:
            new_item = input("What would you like to change it to? ")
            for i in range(len(todolist)):
                if todolist[i] == old_item:
                    todolist[i] = new_item
        else:
            print("Item not found in the list.")
    elif menu == "delete":
        item = input("Which item would you like to delete? ")
        check = input("Are you sure you want to delete this item? (yes/y) ").lower()
        if check in ['yes', 'y'] and item in todolist:
            todolist.remove(item)
    elif menu == "delete all":
        check = input("Are you sure you want to delete all items? (yes/y) ").lower()
        if check in ['yes', 'y']:
            todolist.clear()
            print("All items have been deleted.")
    elif menu == "view":
        printlist()