import os
from datetime import datetime

from bldrdsh.utils import check_existing_project
from bldrdsh.create_project.utils import create_folder, write_json

def create():
    # Check if exisiting and valid project in current path--> If false, create, if true, return msg
    existing = check_existing_project()
    print(existing)
    if existing:
        return('Folder already contains project')
    else:
        create_project_prompt()

def create_project_prompt():
    project_name, path = create_folder()
    print(project_name, path)
    
    # Create txt file with user_{number given} in folder data
    # while True:
    #     try:
    #         initial_users = int(input('How many initial users? '))
    #         break
    #     except:
    #         print("That's not a valid option!")

    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M")

    # Project Summary - print some info: project name, date created, num of users. Verify if we are inside a valid folder --> content of metadata file. If we are skip
        
    j_data = {
        "project_name": project_name,
        "date_created": dt_string,
    }

    # OK Create first metadata file -->{prjoect_name}_metadata.json
    os.mkdir(path)
    write_json(path, f'{project_name}_metadata.json', j_data)

