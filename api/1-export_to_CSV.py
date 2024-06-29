#!/usr/bin/python3
"""
    python script that exports data in the CSV format
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    user = json.loads(request_employee.text)

    username = user.get("username")

    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    tasks = {}

    user_todos = json.loads(request_todos.text)

    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    with open('{}.csv'.format(argv[1]), mode='w') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            file_editor.writerow([argv[1], username, v, k])

"""
#!/usr/bin/python3
import csv
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
"""