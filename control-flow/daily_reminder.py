task = input("Enter the task description: ").strip()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()

match priority:
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is of LOW priority."
    case _:
        reminder = f"The task '{task}' has an INVALID priority."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)