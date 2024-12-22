task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time == "yes": print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else: print(f"Note: '{task}' is a high priority task. Although, consider completing it when you have free time.")
    case "medium":
        if time == "yes": print(f"Reminder: '{task}' is a medium priority task that is required today!")
        else: print(f"Note: '{task}' is medium priority task. Ccomplete it when you have free time.")
    case "low":
        if time == "yes": print(f"Reminder: '{task}' is a low priority task. Although it is time bound, complete as soon as you can.")
        else: print(f"Note: '{task}' is low priority task. Complete it on your free time.")