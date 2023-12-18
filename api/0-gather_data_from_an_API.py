#!/usr/bin/python3
"""Script that display infos for a given employee"""

import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # user info
    user_request = requests.get(f'{API_URL}/users/{sys.argv[1]}')
    user_data = user_request.json()

    # todo info
    todo_list_request = requests.get(f"{API_URL}/todos?userId={sys.argv[1]}")
    todo_list_data = todo_list_request.json()

    # completed todo
    completed_tasks = [task for task in todo_list_data if task['completed']]

    user_name = user_data["name"]
    len_completed_tasks = len(completed_tasks)
    total_todo = len(todo_list_data)

    print("Employee {} is done with tasks({}/{}):".format(
        user_name,
        len_completed_tasks,
        total_todo))

    for task in completed_tasks:
        print(f"\t {task['title']}")
