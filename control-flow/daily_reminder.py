
task = input("Enter your task: ")
priority = input("Enter the task's priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        message = f"Your task '{task}' is HIGH priority."
    case "medium":
        message = f"Your task '{task}' is MEDIUM priority."
    case "low":
        message = f"Your task '{task}' is LOW priority."
    case _:
        message = f"Your task '{task}' has an UNKNOWN priority."


if time_bound == "yes":
    message += " This task requires immediate attention today!"

print(message)
