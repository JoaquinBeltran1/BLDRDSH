import os
import pathlib
import datetime
from typing import List

def generate_historical(params: dict):

    path = str(pathlib.Path().resolve())
    current_time = datetime.datetime.now().strftime("%Y%M%d%H%M%S")
    project_name = params.pop('project_name')
    os.mkdir(path +'/'+ current_time + '_' + project_name )

    metadata = DocsTest.generate_metadata_file(params)
    
    return f"The directory '{project_name}' has been created!"

class DocsTest:
    """
    Testing docs for mkdocstrings.
    
    Now mkdocstrings is watching for changes in bldrdsh.


    """


    def test(funcs: List):
        """do something.
        
        Arguments:
            funcs: functions that indicate which items to keep
        """
        return funcs

    def generate_metadata_file(params):
        """
        Given initial params, call functions to generate
        historical outputs.
        Big JSON file.

        Usage:

        ```python
        def some_func(a,b,c):
            return a + b + c

        ```
        """
        quantity = params.pop('quantity')
        to_json = "add date, time, title, quantity to json file"
        return "return a summary of to_json but beautify it"

    def agg(self, **kwargs):
        """
        Does some agg.
        """
        pass

def generate_table():
    """
    Base thing table type, all tables share same "schema".
    Create CSV for now for all tables in sales.
    Then sqlite3
    Then postgresql
    """
    pass

def get_name():
    project_name = input("Name? ")
    quantity = input("Quantity? ")
    print(project_name, quantity)