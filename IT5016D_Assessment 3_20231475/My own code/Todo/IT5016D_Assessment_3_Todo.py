# Simple to-do list program
tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found in the list")

def show_tasks():
    print("Tasks:")
    for task in tasks:
        print("-", task)

# Main program
if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice")
