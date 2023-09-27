#!/usr/bin/python3
"""gets information TODO list progress,
    and export data in the JSON format.

Example:
    $ python3 3-dictionary_of_list_of_dictionaries.py

"""

import json
import requests


if __name__ == '__main__':
    # Fetch TODO list and user name
    todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos',
            timeout=1).json()
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users',
            timeout=1).json()
    todo_dict = {}
    for task in todo:
        if not task['userId'] in todo_dict:
            todo_dict[task['userId']] = []
        key = task['userId']
        task['task'] = task['title']
        del task['userId']
        del task['id']
        del task['title']
        task['username'] = user[int(key) - 1]['username']
        todo_dict[key].append(task)
    for emp in user:
        if not emp['id'] in todo_dict:
            todo_dict[emp['id']] = []

    # Create a JSON file
    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        # Write TODO list information to the JSON file
        file.write(json.dumps(todo_dict))
