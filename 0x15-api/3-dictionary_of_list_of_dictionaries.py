#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": td.get("title"),
                "completed": td.get("completed"),
                "username": u.get("username")
            } for td in requests.get(base_url + "todos",
                                     params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
