# This program allows a user to input tasks, mark them as complete, and view progress to completion
# of each task in one output.
# This represents the 3rd step of a Stepwise Refinement exercise.

# This class will house all the functions the program will perform including
# 1. Adding Tasks
# 2. Viewing Tasks
# 3. Marking tasks as completed
# 4. End program

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

# The following function provides the structure for input and rules that the program
# will follow including print features, breaks, and program exit.

def main():
    scheduler = TaskScheduler()
    
    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task description: ")
            scheduler.add_task(task)
            print("Task added successfully.")
        elif choice == '2':
            scheduler.view_tasks()
        elif choice == '3':
            scheduler.view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            scheduler.mark_task_completed(task_number)
        elif choice == '4':
            print("Exiting Task Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()