#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
base_url = "https://jsonplaceholder.typicode.com"
user_resp = requests.get(f"{base_url}/users")
users = user_resp.json()
todo_resp = requests.get(f"{base_url}/todos")
todos = todo_resp.json()
task_dict = {}
for user in users:
    user_id = user['id']
    user_name = user['username']
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    task_list = []
    for todo in user_todos:
        task_info = {
            "username": user_name,
            "task": todo['title'],
            "completed": todo['completed']
        }
        task_list.append(task_info)
    task_dict[user_id] = task_list
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(task_dict, json_file)
print("Data has been exported to todo_all_employees.json")
