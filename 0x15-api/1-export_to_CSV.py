#!/usr/bin/python3
"""gets information about his/her TODO list progress,
    and export data in the CSV format.

Example:
    $ python3 1-export_to_CSV.py 2

"""

import csv
import requests
import sys


if __name__ == '__main__':
    # Fetch TODO list and user name
    todo = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}',
            timeout=.1).json()
    user_name = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}',
            timeout=.1).json()['name']

    # Create a CSV file
    with open(sys.argv[1] + '.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write TODO list information to the CSV file
        for task in todo:
            writer.writerow([sys.argv[1], user_name, task['completed'],
                            task['title']])
