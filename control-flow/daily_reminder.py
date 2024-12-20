Task = input("task description")
Priority = input("enter task’s priority (high, medium, low)")
Time_bound = input("is the task is time-bound? (yes or no)")
match Priority:
    case "high":
        if Time_bound == "yes":
            reminder = f"{Task} is a high priority task that requires immediate attention today!"
        else:
            reminder = f"{Task} is a high priority task. make sure to complete it soon."
    case "medium":
        if Time_bound == "yes":
            reminder = f"{Task} is a meduim priority task with a deadline. plan accodingly!"
        else:
            reminder = f"{Task} is a meduim priority task. Complete it when possible!"
    case "low":
        if Time_bound == "yes":
            reminder = f"{Task} is a low priority task with a deadline. consider scheduling time for it."
        else:
            reminder = f"{Task} is a low priority task. Consider completing it when you have free time"
    case _:
        reminder = "invalid"      
print (reminder)
