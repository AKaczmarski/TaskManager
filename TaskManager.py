def task_manager():
    tasks = []

    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            if tasks:
                print("Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
                index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    print("Task removed.")
                else:
                    print("Invalid number.")
            else:
                print("No tasks to remove.")
        elif choice == '3':
            if tasks:
                print("Your tasks:")
                for t in tasks:
                    print(f"- {t}")
            else:
                print("No tasks.")
        elif choice == '4':
            break
        else:
            print("Unknown option!")

task_manager()
