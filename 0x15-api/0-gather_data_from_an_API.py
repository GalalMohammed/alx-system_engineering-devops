#!/usr/bin/python3
"""gets information about his/her TODO list progress.

Example:
    $ python3 0-gather_data_from_an_API.py 2

"""

import sys
import requests


if __name__ == '__main__':
    # Fetch TODO list and user name
    todo = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}',
            timeout=.1).json()
    user_name = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}',
            timeout=.1).json()['name']
    completed_tasks = [task for task in todo if task['completed']]

    # Display progress information
    print(f'Employee {user_name} is done with tasks' +
          f'({len(completed_tasks)}/{len(todo)}):')
    for task in completed_tasks:
        print('\t ' + task['title'])
