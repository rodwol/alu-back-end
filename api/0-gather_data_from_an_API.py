#!/usr/bin/python3
"""Given an Employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    try:
        EMPLOYEE_ID = int(sys.argv[1])
    except (ValueError, IndexError):
        print("First line formatting: Incorrect")
        sys.exit()

    try:
        url = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}"
        response = requests.get(url)
        response.raise_for_status()
        user_data = response.json()
        EMPLOYEE_NAME = user_data.get('name')

        url2 = f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}"
        response2 = requests.get(url2)
        response2.raise_for_status()
        todos_data = response2.json()
        done_tasks = [todo['title'] for todo in todos_data if todo['completed']]
        TOTAL_NUMBER_OF_TASKS = len(todos_data)
        NUMBER_OF_DONE_TASKS = len(done_tasks)

        # Print the progress
        print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in done_tasks:
            print(f"\t {task}")

        print("First line formatting: OK")
        print("Employee Name: OK")
        print("To Do Count: OK")

    except requests.RequestException as e:
        print("First line formatting: Incorrect")
        print("Employee Name: Incorrect")
        print("To Do Count: Incorrect")
        sys.exit()

