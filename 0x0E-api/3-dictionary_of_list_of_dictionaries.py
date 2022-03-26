#!/usr/bin/python3
"""Uses REST API to find an employee ID and return
information about their todo list progress"""
import json
import requests
import sys


if __name__ == '__main__':
    """checks for valid input and returns employee info"""
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todo_list = response.json()
    employees = users.json()

    master_dict = {}
    for user in employees:
        id = user['id']
        master_dict[id] = []
        for task in todo_list:
            if task['userId'] == id:
                new_dict = {
                    'username': user['username'],
                    'task': task.get('title'),
                    'completed': task.get('completed')
                    }
                master_dict[id].append(new_dict)
        out_file = open("todo_all_employees.json", "w")
        json.dump(master_dict, out_file)
        out_file.close()
