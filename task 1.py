class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task_index):
        try:
            self.tasks.pop(task_index)
            print("Task removed successfully!")
        except IndexError:
            print("Task index out of range!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, task_index, new_task):
        try:
            self.tasks[task_index] = new_task
            print("Task updated successfully!")
        except IndexError:
            print("Task index out of range!")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            task_index = int(input("Enter task index to update: ")) - 1
            new_task = input("Enter new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
