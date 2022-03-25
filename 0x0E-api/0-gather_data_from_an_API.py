#!/usr/bin/python3
"""Uses REST API to find an employee ID and return
information about their todo list progress"""
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
        not_done = len(todo_list)

        print("Employee {} is done with tasks({}/{}):".format(
            emp_name, done, not_done))
        for title in finished_tasks:
            print("\t {}".format(title))
