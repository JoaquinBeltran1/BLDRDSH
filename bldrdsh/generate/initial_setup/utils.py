import os
import json
from datetime import datetime
from pathlib import Path



def start_valid_date():
    start_date = input('Enter a starting date of the format dd/mm/YYYY (default: 01/01/2010): ') or '01/01/2010' 
    valid = False
    # TODO: Validate things like 1/1/2001 or 01/7/1993
    # TODO: Limit early date. 2000 maybe (?)
    while not valid:
        try:
            date = datetime.strptime(
                start_date, "%d/%m/%Y").strftime("%d/%m/%Y")
            valid = True
        except ValueError:
            start_date = input("Incorrect date format. Please try again (default: 01/01/2010): ") or '01/01/2010'
    
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

def write_metadata(metadata):
    keyword = 'metadata'
    for filename in os.listdir():
        if keyword in filename:
            with open(f'{filename}', 'w') as f:
                json.dump(metadata, f, indent=4)

def push_to_db():
    """
    Whatever is passed in this function,
    push it to a table in sqlite
    """

def read_profile(profile_num: int):
    """
    Read profile values from JSON given profile num. In JSON file store 3 profiles.
    return dict with selected profile values.
    """
    cwd = Path(__file__).parent.parent
    with open(cwd / 'params/company_profiles.json') as f:
        profiles = json.load(f)

    profile = next((profile for profile in profiles if profile["id"] == profile_num), None)
    return profile

