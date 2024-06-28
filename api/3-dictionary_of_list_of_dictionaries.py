#!/usr/bin/python3
"""
Export data from an API to JSON format.
"""
import json
import requests


if __name__ == "__main__":
    # Fetch the list of all employees
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url).json()

    # Initialize the dictionary to hold all tasks
    all_tasks = {}

    # Iterate through each employee and fetch their TODO list
    for employee in response:
        EMPLOYEE_ID = employee['id']
        EMPLOYEE_NAME = employee['username']

        # Fetch TODO list information for the current employee
        url2 = f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}"
        response2 = requests.get(url2).json()

        # Construct the list of tasks for the current employee
        tasks = []
        for todo in response2:
            task_data = {
                "username": EMPLOYEE_ID,
                "task": todo['title'],
                "completed": todo['completed']
            }
            tasks.append(task_data)

        # Add the employee's tasks to the all_tasks dictionary
        all_tasks[str(EMPLOYEE_ID)] = tasks

    # Write JSON data to file
    json_file = "todo_all_employees.json"
    with open(json_file, mode='w') as file:
        json.dump(all_tasks, file)
