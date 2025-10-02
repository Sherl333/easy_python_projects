import json
import time

tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open("todo_list.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

# Save tasks to file
def save_tasks():
    with open("todo_list.json", "w") as f:
        json.dump(tasks, f, indent=4)

def add_todo():
    task_input = input("Enter task description: ")
    task_id = len(tasks) + 1
    task = {"id": task_id, "description": task_input, "status": "Pending"}
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\nID   | Task                 | Status")
    print("--------------------------------------")
    for task in tasks:
        print(f'{task["id"]:<4} | {task["description"]:<20} | {task["status"]}')

def update_task():
    task_id = int(input("Enter the ID of the task to update: "))
    found = False
    for task in tasks:
        if task["id"] == task_id:
            new_desc = input("Enter new description: ")
            task["description"] = new_desc
            found = True
            print("Task updated successfully!")
            save_tasks()
            break
    if not found:
        print("No task with that ID.")

def change_status_to_done():
    task_id = int(input("Enter the ID of the task to mark done: "))
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Done"
            found = True
            print("Task marked as done!")
            save_tasks()
            break
    if not found:
        print("No task with that ID.")

def delete_task():
    task_id = int(input("Enter the ID of the task to delete: "))
    global tasks
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) < len(tasks):
        tasks = new_tasks
        save_tasks()
        print("Task deleted!")
    else:
        print("No task with that ID.")

def todo_list():
    while True:
        choice = input(
            """\n
            1. Add Task
            2. View Tasks
            3. Update Task
            4. Delete Task
            5. Mark Task as Done
            6. Exit\n
            Enter choice: """
        )

        if choice == "1":
            add_todo()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            change_status_to_done()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Please provide a valid choice of number")

# Run
load_tasks()
todo_list()
