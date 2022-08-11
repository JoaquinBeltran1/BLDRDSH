from bldrdsh.generate.initial_setup.create import initial_setup
from bldrdsh.utils import check_existing_project, check_validity, check_if_new

class GenerateData():
    """
    """
    def generate():
        # Print summary of inputs from user. Short description of each initial value, then prompt.
        # At the end, show summary, and then proceed with the generation.
        # If there is set path to its location. Apply all next function into that path <-- Ça va de soi

        # --------------------------

        # If project has metadata but its corrupted --> This also goes inside check_or_create

        # -------------------------
        existing = check_existing_project()
        if existing:
            print('There is a project in this folder!')
            new_project = check_if_new()
            if new_project:

                initial_setup()

                print('Successful initial setup!')
                generate_batch()
                

            else:
                print("Not new project, last batch exists")
                generate_batch()
            return 'done! <-- return some summaries'
            valid = check_validity()
            if valid:
                generate_data()
            else:
                return 'Existing project but not valid. <--How to manually debug'

        else:
            return 'There is no project in this folder'


def generate_batch():
    """
    Main batch entry point. Here goes the prompt

    Check if first batch.
    If yes, prepare first batch


    Given batch objective (days running or new customers),
    generate new day of data. <- This reads db!!!
    At end of each day, check with objectives.
    Update distance (?).
    Then new day or if distance 0 stop batch.

    """

    pre_batch()
    start_load()
    day_loop()
    pass

def pre_batch():
    check_past_tables()
    """
    if no past tables, pass
    """
    check_past_metadata()
    pass

def check_past_tables():
    """
    Check all tables.
    Here we check if we've done a correct inital setup = 
    we have a project starting date
    """
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

def day_loop():
    """
    Entry function for each day
    """