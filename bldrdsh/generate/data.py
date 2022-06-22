from bldrdsh.utils import check_existing_project, check_validity, check_if_new

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
        print(existing)
        if existing:
            print('Folder contains project')
            new_project = check_if_new()
            if new_project:
                print("New project, no last batch!")
            else:
                print("Not new project, last batch exists")
            return 'done!'
            valid = check_validity()
            if valid:
                generate_data()
            else:
                return 'Existing project but not valid. <--How to manually debug'

        else:
            return 'There is no project in this folder'
