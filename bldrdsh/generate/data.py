from bldrdsh.generate.new_project import create_project_prompt
from bldrdsh.generate.check_project import check_existing_project


class GenerateData():
    """
    Main entry point!!!
    Called within existing project
    or
    Empty folder

    Takes Data Requirements

    Calls all other functions
        - generate.check_project
        - generate.errors
        - generate.new_tables

        - batch.initial_setup
    Should be a class?
    """
    
    
    def create_new_project():
        # Check if exisiting and valid project in current path--> If false, create, if true, return msg
        existing = check_existing_project()
        print(existing)
        if existing:
            return('Folder already contains project')
        else:
            create_project_prompt()

    def generate():
        # Check if exisiting and valid project in current path-->
        # If there is set path to its location. Apply all next function into that path <-- Ça va de soi

        # --------------------------

        # If project has metadata but its corrupted --> This also goes inside check_or_create

        # -------------------------
        pass
