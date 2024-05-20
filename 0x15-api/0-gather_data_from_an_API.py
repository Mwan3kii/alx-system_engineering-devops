#!/usr/bin/python3
"""using REST API for employee ID returns TODO list progress"""
import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tdata = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [t.get("title") for t in tdata if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
          emp_user.get("name"), len(completed), len(tdata)))
    [print("\t {}".format(e)) for e in completed]
