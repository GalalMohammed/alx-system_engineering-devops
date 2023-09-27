#!/usr/bin/python3
"""gets information about his/her TODO list progress,
    and export data in the JSON format.

Example:
    $ python3 2-export_to_JSON.py 2

"""

import json
import requests
import sys


if __name__ == '__main__':
    # Fetch TODO list and user name
    todo = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}',
            timeout=1).json()
    user_name = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}',
            timeout=1).json()['username']
    todo_list = []
    for task in todo:
        task_dict = {}
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        task_dict['username'] = user_name
        todo_list.append(task_dict)

    # Create a JSON file
    with open(sys.argv[1] + '.json', 'w', encoding='utf-8') as file:
        # Write TODO list information to the JSON file
        file.write(json.dumps({sys.argv[1]: todo_list}))
