# Step 1 - Initialize the task list
tasks = []

# Step 2 - Add tasks
def add_task(tasks, task_name, priority):
    tasks.append((task_name, priority))

# Step 3 - Sort tasks
def sort_tasks(tasks):
    tasks.sort(key=lambda x: x[1])

# Step 4 - Schedule tasks
def schedule_tasks(tasks):
    for task in tasks:
        print(f"Scheduling task: {task[0]} with priority: {task[1]}")

# Step 5 - Combine all steps
def task_scheduler():
    tasks = []
    
    # Adding tasks
    add_task(tasks, "Task 1", 2)
    add_task(tasks, "Task 2", 1)
    add_task(tasks, "Task 3", 3)
    
    # Sorting tasks by priority
    sort_tasks(tasks)
    
    # Scheduling tasks
    schedule_tasks(tasks)

# Run the task scheduler
task_scheduler()