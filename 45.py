import os
import time

todo = []

def clear_screen():
    time.sleep(1)
    os.system("clear")

def add_task():
    clear_screen()
    name = input("Enter the task: ").strip()
    date = input("Enter the date (YYYY-MM-DD): ").strip()
    priority = input("Enter the priority (Low, Medium, High): ").strip().capitalize()
    todo.append({"name": name, "date": date, "priority": priority})
    print("\nTask added successfully!")

def remove_task():
    clear_screen()
    name = input("Enter the task to remove: ").strip()
    for task in todo:
        if task["name"].lower() == name.lower():
            todo.remove(task)
            print("\nTask removed successfully!")
            break
    else:
        print("\nTask not found!")

def show_tasks():
    clear_screen()
    if not todo:
        print("No tasks available.")
    else:
        print("All Tasks:\n")
        for idx, task in enumerate(todo, start=1):
            print(f"Task {idx}:")
            print(f"  Name    : {task['name']}")
            print(f"  Date    : {task['date']}")
            print(f"  Priority: {task['priority']}")
            print("-" * 30)

def main_menu():
    while True:
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Exit")
        menu = input("\nPlease choose an option: ").strip()

        if menu == "1":
            add_task()
        elif menu == "2":
            remove_task()
        elif menu == "3":
            show_tasks()
        elif menu == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

        time.sleep(2)
        clear_screen()

if __name__ == "__main__":
    main_menu()