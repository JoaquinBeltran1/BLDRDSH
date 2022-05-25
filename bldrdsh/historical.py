import os
import pathlib
import datetime

def generate_historical(params: dict):

    path = str(pathlib.Path().resolve())
    current_time = datetime.datetime.now().strftime("%Y%M%d%H%M%S")
    project_name = params.pop('project_name')
    os.mkdir(path +'/'+ current_time + '_' + project_name )

    metadata = generate_metadata_file(params)
    
    return f"The directory '{project_name}' has been created!"

def generate_metadata_file(params):
    """
    Given initial params, call functions to generate
    historical outputs.
    Big JSON file.
    """
    quantity = params.pop('quantity')
    to_json = "add date, time, title, quantity to json file"
    return "return a summary of to_json but beautify it"

def generate_table():
    """
    Base thing table type, all tables share same "schema".
    Create CSV for now for all tables in sales
    """
    pass