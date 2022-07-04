import os
import json

def check_existing_project():
    arr = os.listdir()
    print('Tis the metadata file: ', arr)
    for i in arr:
        if i.endswith(".json"):
            return True
        else:
            return False

def check_validity():
    """
    Check if existing project is valid and new
    or
    Valid and NOT new
    """
    


def check_if_new():
    """
    Check contents of metadata file, and if it's the only
    file inside the directory
    """

    # Read metadata file
    keyword = 'metadata'
    for filename in os.listdir():
        if keyword in filename:
            f = open(f'{filename}')
            data = json.load(f)
            print(data)
            if 'last_batch' in data.keys():
                return False
            else:
                return True

        else:
            print("No metadata.json file!")
    
    
    # returns JSON object as 
    # a dictionary
    
