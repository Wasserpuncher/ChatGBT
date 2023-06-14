TASKS_FILE = 'tasks.txt'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
    except FileNotFoundError:
        tasks = []
    
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def list_tasks(tasks):
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks.")

def delete_task(tasks):
    list_tasks(tasks)
    task_index = input("Enter the task number to delete: ")
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            deleted_task = tasks.pop(task_index - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("Menu:")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Delete a task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
