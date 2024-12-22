task = input("task description: ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()

match priority :
    case "high" :
        reminder = print (f"The task {task} is of HIGH priority.")
    case "medium" :
        reminder = print (f"The task {task} is of MEDIUM priority.")
    case "low" :
        reminder = print (f"The task {task} is of LOW priority.")
if time_bound == "yes" :
    print("It requires immediate attention today!")