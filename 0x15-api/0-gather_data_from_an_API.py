#!/usr/bin/python3
import requests
import sys
import json


def employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    emp_url = f"{base_url}/users/{employee_id}"
    emp_resp = requests.get(emp_url)
    emp_data = emp_resp.json()
    emp_name = emp_data.get('name')
    tod_url = f"{base_url}/todos?userId={employee_id}"
    tod_resp = requests.get(tod_url)
    tod_data = tod_resp.json()
    total_tasks = len(tod_data)
    done_tasks = [todo for todo in tod_data if todo.get('completed')]
    completed_tasks = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, completed_tasks, total_tasks))
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_todo_progress(employee_id)
