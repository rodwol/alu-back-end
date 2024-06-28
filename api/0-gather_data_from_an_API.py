#!/usr/bin/python3
"""Given an Employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    try:
        EMPLOYEE_ID = int(sys.argv[1])
    except ValueError:
        exit()

    url = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}"
    response = requests.get(url).json()
    EMPLOYEE_NAME = response.get('name')

    url2 = f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}"
    response2= requests.get(url2).json()
    done_tasks = [todo['title'] for todo in response2 if todo['completed']]
    TOTAL_NUMBER_OF_TASKS = len(response2)
    NUMBER_OF_DONE_TASKS = len(done_tasks)

    # Print the progress
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in done_tasks:
        print(f"\t {task}")
