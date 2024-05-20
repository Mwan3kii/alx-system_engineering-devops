#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f"{url}users/{user_id}").json()
    user_name = user.get("username")
    tdata = requests.get(f"{url}todos", params={"userId": user_id}).json()
    tasks = [{
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": user_name
    } for todo in tdata]
    data = {user_id: tasks}
    filename = f"{user_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data exported to {filename}")
