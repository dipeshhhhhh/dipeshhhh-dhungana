from todo_operation import add_task, view_tasks, delete_task
from utils import clear_screen, get_user_input

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a new to-do item")
    print("2. View all to-do items")
    print("3. Delete an item by its index")
    print("4. Exit")

def main():
    while True:
        clear_screen()
        display_menu()

        # Get the user's choice
        choice = get_user_input("Enter your choice (1-4): ")

        if choice == '1':
            task = get_user_input("Enter the task: ")
            add_task(task)

        elif choice == '2':
            view_tasks()
            get_user_input("\nPress Enter to return to the menu.")

        elif choice == '3':
            view_tasks()
            try:
                index = int(get_user_input("Enter the index of the task to delete: "))
                delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            get_user_input("\nPress Enter to return to the menu.")

        elif choice == '4':
            print("Exiting the To-Do List application.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()