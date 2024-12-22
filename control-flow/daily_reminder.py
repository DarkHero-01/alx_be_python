task = input ("Enter your task: ")
time_bound = input ("Is it time-bound? (yes or no):")
priority = input ("Priority (high, medium, low):")

match priority :
    case "high" :
        reminder = print (f"The task {task} is of HIGH priority.")
    case "medium" :
        reminder = print (f"The task {task} is of MEDIUM priority.")
    case "low" :
        reminder = print (f"The task {task} is of LOW priority.")
if time_bound == "yes" :
    print("It requires immediate attention today!")