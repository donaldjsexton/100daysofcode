import os, time
todolist=[]

def printlist():
  print()
  for item in todolist:
    print(item)
  print()

while True:
    menu = input("ToDolist Manager\n\nDo you want to add, delete, or view your list? ")
    if menu == "add":
       item = input("What would you like to add to your list? ")
       todolist.append(item)
    elif menu == "delete":
        item = input("Which item would you like to delete? ")
        if item in todolist:
          todolist.remove(item)
    elif menu == "view":
        printlist()