import os
import json

def create_folder():
    project_name = input('Project name: ')
    directory = os.getcwd()
    path = os.path.join(directory, project_name)
    return project_name, path

def write_json(target_path, target_file, data):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), 'w') as f:
        json.dump(data, f, indent=4)

