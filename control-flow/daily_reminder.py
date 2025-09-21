# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process using match case
match priority:
    case "high":
        priority_text = "high priority task"
    case "medium":
        priority_text = "medium priority task"
    case "low":
        priority_text = "low priority task"
    case _:
        priority_text = "task with unknown priority"

# Print final reminder directly with 'Reminder:' in the print
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} that requires immediate attention today!")
else:
    if priority == "low":
        print(f"Reminder: '{task}' is a {priority_text}. Consider completing it when you have free time.")
    else:
        print(f"Reminder: '{task}' is a {priority_text}.")
