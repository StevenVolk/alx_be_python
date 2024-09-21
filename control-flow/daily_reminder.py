#!/usr/bin/env python3
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
sensitivity = input("Is it time-bound? (yes/no): ")
if priority == "high":
    if sensitivity == "yes":
        print("Reminder: '" + task + "' is a high priority task that requires immediate attention today!")
    elif sensitivity == "no":
        print("Note: '" + task + "' is a high priority task. Consider completing it when you have free time.")
elif priority == "medium":
    if sensitivity == "yes":
        print("Reminder: '" + task + "' is a medium priority task that requires attention today!")
    elif sensitivity == "no":
        print("Note: '" + task + "' is a medium priority task. Consider completing it when you have free time.")
elif priority == "low":
    if sensitivity == "yes":
        print("Reminder: '" + task + "' is a low priority task that requires attention today!")
    elif sensitivity == "no":
        print("Note: '" + task + "' is a low priority task. Consider completing it when you have free time.")
