#!/usr/bin/python3
"""
Export data from an API to CSV format.
"""
import requests
import sys
import csv

if __name__ == "__main__":
    try:
        EMPLOYEE_ID = int(sys.argv[1])
    except ValueError:
        exit()

    url = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}"
    response = requests.get(url).json()
    EMPLOYEE_NAME = response.get('name')
    username = response.get('username')

    url2 = f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}"
    response2 = requests.get(url2).json()

    # export data to csv
    csv_file = f"{EMPLOYEE_ID}.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in response2:
            writer.writerow([EMPLOYEE_ID, EMPLOYEE_NAME, todo.get('completed'), todo.get('title')])
            # writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
