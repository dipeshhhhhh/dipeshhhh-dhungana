# List to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(index):
    try:
        task = tasks.pop(index - 1)
        print(f"Task '{task}' deleted.")
    except IndexError:
        print("Invalid index. Please try again.")