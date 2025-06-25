def is_empty(Q_tasks):
    return len(Q_tasks) == 0

def insert(Q_tasks, task):
    Q_tasks.append(task)

def extract(Q_tasks):
    if is_empty(Q_tasks):
        return -1
    return Q_tasks.pop(0)

def peek(Q_tasks):
    if is_empty(Q_tasks):
        return -1
    return Q_tasks[0]   

def complete_next_task(Q_tasks):
    if is_empty(Q_tasks):
        print("No tasks to complete.")
        return
    highest = Q_tasks[0]

    for task in Q_tasks:
        if task['priority'] < highest['priority']:
            highest = task
    index = Q_tasks.index(highest)
    print("Next task to complete:", Q_tasks.pop(index))
    

def search_for_task(Q_tasks, title):
    for i in range(len(Q_tasks)):
        for j in range(0, len(Q_tasks) - i - 1):
            if Q_tasks[j]['title'] > Q_tasks[j + 1]['title']:
                Q_tasks[j], Q_tasks[j + 1] = Q_tasks[j + 1], Q_tasks[j]
    if is_empty(Q_tasks):
        return -1   
    low, high = 0,  len(Q_tasks) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_title = Q_tasks[mid]['title']
        if mid_title == title:
            return Q_tasks[mid]
        elif mid_title < title:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def sort_tasks(Q_tasks):
    if is_empty(Q_tasks):
        return Q_tasks
    for i in range(len(Q_tasks)):
        for j in range(0, len(Q_tasks) - i - 1):
            if Q_tasks[j]['duration'] > Q_tasks[j + 1]['duration']:
                Q_tasks[j], Q_tasks[j + 1] = Q_tasks[j + 1], Q_tasks[j]

    return Q_tasks


Q_tasks = []
nb_of_tasks = int(input("Enter the number of tasks: "))

for i in range(nb_of_tasks):
    title = input("Enter the title of task " + str(i)+": ")
    while True:
        duration = int(input("Enter the duration (in minutes) of task " + str(i) + ": "))
        if duration < 0:
            print("Duration must be a positive number. Try again.")
        else:
            break

    while True:
        priority = int(input("Enter the priority of task " + str(i) + ": "))
        if priority > 0:
            break
        else:
            print("Priority must be a positive number. Try again.")

    task = {
        'title': title,
        'duration': duration,
        'priority': priority
    }
    Q_tasks.append(task)

print("Tasks in the queue:", Q_tasks)

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Complete Next Task")
    print("3. Search for Task")
    print("4. Sort Tasks")


    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        duration = int(input("Enter task duration (in minutes): "))
        priority = int(input("Enter task priority : "))
        task = {
            'title': title,
            'duration': duration,
            'priority': priority
        }
        insert(Q_tasks, task)
        print("Task added.")

    elif choice == "2":
          complete_next_task(Q_tasks)

    elif choice == "3":
        title = input("Enter task title to search: ")
        result = search_for_task(Q_tasks, title)
        if result != -1:
            print("Task found:" + str(result))
        else:
            print("Task not found.")

    elif choice == "4":
       
        Q_tasks = sort_tasks(Q_tasks)
        print("Tasks sorted by duration.")

    else:
        print("Invalid choice. Please try again.")