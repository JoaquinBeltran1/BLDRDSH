import click



class GenerateData():
    """
    Main entry point!!!
    Called within existing project
    or
    Specifying project path

    Takes Data Requirements

    Calls all other functions
        - generate.check_project
        - generate.errors
        - generate.new_tables

        - batch.initial_setup
    Should be a class?
    """

    def generate():
        if click.confirm('New project?', default=True):
            project_name = input("Name? ")
            quantity = input("Quantity? ")
            curr_dir = click.confirm('Current directory?', default=True)
            print(curr_dir)
            print('You said: %s' % project_name, quantity, curr_dir)
        else:
            print("bye!")
        """
        Then verify if existing project
        
        """
        
if __name__ == '__main__':
    GenerateData.generate()