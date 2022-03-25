#!/usr/bin/python3
"""Uses REST API to find an employee ID and return
information about their todo list progress"""
import csv
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

        with open('{}.csv'.format(u_id), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todo_list:
                writer.writerow(
                    [(u_id), employees.get('username'), task.get(
                        'completed'), task.get('title')])
