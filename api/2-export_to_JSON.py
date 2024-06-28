#!/usr/bin/python3
"""
Export data from an API to JSON format.
"""
import requests
import sys
import json

if __name__ == "__main__":
    try:
        EMPLOYEE_ID = int(sys.argv[1])
    except ValueError:
        exit()

    url = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}"
    response = requests.get(url).json()
    EMPLOYEE_NAME = response.get('username')

    url2 = f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}"
    response2 = requests.get(url2).json()
    done_tasks = [todo['title'] for todo in response2 if todo['completed']]
    TOTAL_NUMBER_OF_TASKS = len(response2)
    NUMBER_OF_DONE_TASKS = len(done_tasks)

    tasks = []
    for todo in response2:
        task_data = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": EMPLOYEE_NAME
        }
        tasks.append(task_data)

    output_data = {
        str(EMPLOYEE_ID): tasks
    }

    # Write JSON data to file
    json_file = f"{EMPLOYEE_ID}.json"
    with open(json_file, mode='w') as file:
        json.dump(output_data, file)
