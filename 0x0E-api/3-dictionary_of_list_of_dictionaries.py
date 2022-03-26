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

    user_dict = {}
    for item in employees:
        user_dict[item.get('id')] = item.get('username')
    master_dict = {}
    for user in employees:
        id = user['id']
        master_dict[id] = []
        # print(master_dict)
        for task in todo_list:
            if task['userId'] == id:
                # print(task['userId'])
                new_dict = {
                    'task': task.get('title'),
                    'completed': task.get('completed'),
                    'username': item['username']
                    }
                print(new_dict)
    # info_json = []
    # for items in todo_list:
    #     new_dict = {
    #         'task': items.get('title'),
    #         'completed': items.get('completed'),
    #         'username': employees.get('username')
    #     }
    #     info_json.append(new_dict)
    #     employee_id = str(items.get('userId'))
    # json_dict = {employee_id: info_json}
    # out_file = open("todo_all_employees.json", "w")
    # json.dump(json_dict, out_file)
    # out_file.close()
