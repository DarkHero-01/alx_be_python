task = str (input("Enter your task: ")).lower()
priority = str (input("Priority (high/medium/low): ")).lower()
time_bound = str (input("Is it time-bound? (yes/no): ")).lower()

match priority :
    case "high" :
        reminder = (f"The task {task} is a high priority.")
    case "medium" :
        reminder = (f"The task {task} is a medium priority.")
    case "low" :
        reminder = (f"The task {task} is a low priority.")
if time_bound == "yes" :
    print("It requires immediate attention today!")