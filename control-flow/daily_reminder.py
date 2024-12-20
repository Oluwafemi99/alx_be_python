task = input("Enter your task:")
priority = input("priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a high priority task. make sure to complete it soon."
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a meduim priority task with a deadline. plan accodingly!"
        else:
            reminder = f"'{task}' is a meduim priority task. Complete it when possible!"
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task with a deadline. consider scheduling time for it."
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time"
    case _:
        reminder = "invalid"      
print (f"Reminder: {reminder}")
