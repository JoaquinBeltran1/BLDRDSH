import os
import sys
import json
import inquirer
from datetime import datetime

class GenerateData():
    """
    Main entry point!!!
    Called within existing project
    or
    Specifying project path

    Takes Data Requirements

    Calls all other functions
        - generate.check_project
        - generate.errors
        - generate.new_tables

        - batch.initial_setup
    Should be a class?
    """
    
    
    def generate():
        """
        Check if project exists in current directory
        """

        current_dir = ''

        questions = [
            inquirer.List('size',
                            message="What size do you need?",
                            choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
                        ),
            ]

        # answers = inquirer.prompt(questions)
        # result = list(answers.values())[0]
        # print(result)
        arr = os.listdir() # <-- This could check for metadata files in folders in current folder. Print project names, and some summary data (?)
        print(arr)


        # OK Create folder
        project_name = input('Project name: ')
        directory = os.getcwd()
        path = os.path.join(directory, project_name)
        print(path)
        os.mkdir(path)

        # Create first metadata file -->{porject_name}_metadata.json
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M")

        j_data = {
            "project_name": project_name,
            "date_created": dt_string
        }
        write_json(path, f'{project_name}_metadata.json', j_data)

        # Create txt file with user_{number given}

        # Verify if we are inside a valid folder --> content of metadata file
        

        """
        Then verify if existing project
        """

def write_json(target_path, target_file, data):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    try:
        GenerateData.generate()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)