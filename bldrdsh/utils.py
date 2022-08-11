import os
import json

def check_existing_project():
    arr = os.listdir()
    file = None
    for i in arr:
        if i.endswith(".json"):
            file = i
        else:
            pass
    if file:
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
            if 'last_batch' in data.keys():
                return False
            else:
                print('Tis a new project!')
                return True
    
    
    # returns JSON object as 
    # a dictionary
    
