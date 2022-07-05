import os
import json
from datetime import datetime


def start_valid_date():
    start_date = input('Enter a starting date of the format dd/mm/YYY (default: 01/01/2010): ') or '01/01/2010' 
    valid = False
    
    while not valid:
        try:
            date = datetime.strptime(
                start_date, "%m/%d/%Y").strftime("%m/%d/%Y")
            valid = True
        except ValueError:
            start_date = input("Incorrect date format. Please try again: ")
    
    return start_date

def open_metadata():
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
    return data

def write_date_metadata(date):
    keyword = 'metadata'
    for filename in os.listdir():
        if keyword in filename:
            with open(f'{filename}', 'w') as f:
                json.dump(date, f, indent=4)