#!/usr/bin/python3
"""Uses REST API to find an employee ID and return
information about their todo list progress"""
import json
import requests
import sys


if __name__ == '__main__':
    """checks for valid input and returns employee info"""
    if sys.argv[1].isdigit():
        u_id = sys.argv[1]
        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos/?userId={}'
            .format(u_id))
        users = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(u_id))

        finished_tasks = []
        todo_list = response.json()
        employees = users.json()

        for task in todo_list:
            if task.get('completed') is True:
                finished_tasks.append(task.get("title"))

        emp_name = employees.get('name')
        done = len(finished_tasks)
        total = len(todo_list)

        print("Employee {} is done with tasks({}/{}):".format(
            emp_name, done, total))
        for title in finished_tasks:
            print("\t {}".format(title))

    else:
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        users = requests.get('https://jsonplaceholder.typicode.com/users')
        todo_list = response.json()
        employees = users.json()

        all_users = {}
        for user in employees:
            all_users[user['id']] = user['username']
        print(all_users)
        # info_json = []
        # for items in todo_list:
        #     new_dict = {
        #         'task': items.get('title'),
        #         'completed': items.get('completed'),
        #         'username': employees.get('username')
        #     }
        #     info_json.append(new_dict)
        # json_dict = {u_id: info_json}
        # out_file = open("{}.json".format(sys.argv[1]), "w")
        # json.dump(json_dict, out_file)
        # out_file.close()
