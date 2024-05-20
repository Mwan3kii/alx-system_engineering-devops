#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f"{url}users/{user_id}").json()
    user_name = user.get("username")
    tdata = requests.get(f"{url}todos", params={"userId": user_id}).json()
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in tdata:
            writer.writerow([user_id, user_name, todo.get("completed"),
                            todo.get("title")])
    print(f"Data exported to {filename}")
