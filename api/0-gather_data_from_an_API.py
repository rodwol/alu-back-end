#!/usr/bin/python3
import requests
import sys

def get_employee_todo_list(employee_id):
    url_user = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    user_response = requests.get(url_user)
    todos_response = requests.get(url_todos)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['name']
    total_tasks = len(todos_data)
    done_tasks = [task['title'] for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_list(employee_id)
        except ValueError:
            print("Please provide a valid employee ID")
