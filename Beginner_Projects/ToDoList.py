print("To-Do List Application")
#does not allow you to pull in a pre-existing list from a file
todo_list = []

def display_menu():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4: Save tasks to file")
    print("5. Exit")
while True:
    display_menu()
    choice = input("Choose an option (1-5): ").strip()
    if choice == "1":
        task = input("Enter the task to add: ").strip()
        todo_list.append(task)
        print(f'Task "{task}" added to the list.')
    elif choice == "2":
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
    elif choice == "3":
        if not todo_list:
            print("Your to-do list is empty. No tasks to remove.")
        else:
            print("Your to-do list:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: ").strip())
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f'Task "{removed_task}" removed from the list.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        filename = input("Enter the filename to save tasks (e.g., todo): ").strip()
        filename += ".txt"
        try:
            with open(filename, 'w') as file:
                for task in todo_list:
                    file.write(task + '\n')
            print(f"Tasks saved to {filename}")
        except Exception as e:
            print(f"Error saving tasks to file: {e}")
    
    elif choice == "5":
        print("Exiting the To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

