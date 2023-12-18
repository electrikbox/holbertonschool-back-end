#!/usr/bin/python3
"""Script that save in csv infos from a given employee"""

import requests
import sys
import csv

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

    # save in csv file
    csv_filename = f"{sys.argv[1]}.csv"

    with open(csv_filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in todo_list_data:
            csv_writer.writerow([sys.argv[1],
                                 user_name,
                                 task['completed'],
                                 task['title']])
