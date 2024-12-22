task = str (input("Enter your task: ")).lower()
priority = str (input("Priority (high/medium/low): ")).lower()
time_bound = str (input("Is it time-bound? (yes/no): ")).lower()

match priority :
    case "high" :
        print (f"reminder: {task} is a high priority.")
    case "medium" :
        print (f"reminder: {task} is a medium priority.")
    case "low" :
        print (f"reminder: {task} is a low priority.")
if time_bound == "yes" :
    print("It requires immediate attention today!")