import os
import json
from datetime import datetime


def validate_date(my_str_date):
    try:
        datetime.strptime(my_str_date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

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