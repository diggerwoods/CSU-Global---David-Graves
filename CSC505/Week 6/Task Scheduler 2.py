import heapq

class TaskScheduler:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task_name, priority):
        # Use a min-heap to store tasks with their priorities
        heapq.heappush(self.task_queue, (priority, task_name))
        print(f"Task '{task_name}' with priority {priority} added.")

    def schedule_tasks(self):
        print("\nScheduling tasks based on priority:")
        while self.task_queue:
            priority, task_name = heapq.heappop(self.task_queue)
            print(f"Perform task '{task_name}' with priority {priority}")

if __name__ == "__main__":
    scheduler = TaskScheduler()
    
    while True:
        print("\n1. Add Task")
        print("\n2. Schedule Tasks")
        print("\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            priority = int(input("Enter task priority (lower number means higher priority): "))
            scheduler.add_task(task_name, priority)
        elif choice == '2':
            scheduler.schedule_tasks()
        elif choice == '3':
            print("Exiting the scheduler.")
            break
        else:
            print("Invalid choice. Please try again.")