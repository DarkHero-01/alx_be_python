task = input ("task description:").lower()
priority = input ("task’s priority (high, medium, low):").lower()
time_bound = input ("Is task time-bound? (yes or no):").lower()

match priority :
    case "high" :
        reminder = print (f"The task {task} is of HIGH priority.")
    case "medium" :
        reminder = print (f"The task {task} is of MEDIUM priority.")
    case "low" :
        reminder = print (f"The task {task} is of LOW priority.")
if time_bound == "yes" :
    print("It requires immediate attention today!")