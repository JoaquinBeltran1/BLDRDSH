import os
import json
from datetime import datetime

def create_folder():
    project_name = input('Project name: ')
    directory = os.getcwd()
    path = os.path.join(directory, project_name)
    return project_name, path


def validate_date(my_str_date):
    try:
        datetime.strptime(my_str_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def write_json(target_path, target_file, data):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), 'w') as f:
        json.dump(data, f, indent=4)

