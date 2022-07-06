from bldrdsh.utils import check_existing_project, check_validity, check_if_new
from bldrdsh.batch.initial_setup import initial_setup

class GenerateData():
    """

    Calls all other functions
        - generate.check_project -- OK
        - generate.errors

        - batch.initial_setup
    Should be a class?
    """
    
    


    def generate():
        # Print summary of inputs from user. Short description of each initial vaºlue, then prompt.
        # Here, include lists (python inquirer).
        # At the end, show summary, and then proceed with the generation.
        # Check if exisiting and valid project in current path-->
        # If there is set path to its location. Apply all next function into that path <-- Ça va de soi

        # --------------------------

        # If project has metadata but its corrupted --> This also goes inside check_or_create

        # -------------------------
        existing = check_existing_project()
        if existing:
            print('There is a project in this folder!')
            new_project = check_if_new()
            if new_project:

                meta_file = initial_setup()


                start_batch()
                print(meta_file)

            else:
                print("Not new project, last batch exists")
                start_batch()
            return 'done! <-- return some summaries'
            valid = check_validity()
            if valid:
                generate_data()
            else:
                return 'Existing project but not valid. <--How to manually debug'

        else:
            return 'There is no project in this folder'


def start_batch():
    pre_batch()
    start_load()
    pass

def pre_batch():
    check_past_tables()
    """
    if no past tables, pass
    """
    check_past_metadata()
    pass

def check_past_tables():
   
    pass


def check_past_metadata():
    """
    ??? Check validity of data?
    """
    pass

def start_load():

    load_agents()
    load_tasks()
    load_contacts()
    load_companies()
    load_trends()
    pass

def load_tasks():
    pass

def load_contacts():
    pass

def load_companies():
    pass

def load_trends():
    pass

def load_agents():
    """
    Store agents. Not really needed (?). Prolly yes.
    Return agents summary
    """
    pass
