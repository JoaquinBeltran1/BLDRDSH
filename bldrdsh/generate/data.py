import os
import sys
import inquirer

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
        """
        Check if project exists in current directory
        """

        current_dir = ''

        questions = [
            inquirer.List('size',
                            message="What size do you need?",
                            choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
                        ),
            ]

        # answers = inquirer.prompt(questions)
        # result = list(answers.values())[0]
        # print(result)
        arr = os.listdir() # <-- This could check for metadata files in folders in current folder. Print project names, and some summary data (?)

        print(arr)
        project_name = input('Project name: ')
        directory = os.getcwd()
        path = os.path.join(directory, project_name)
        print(path)
        os.mkdir(path)
        print(project_name)
        

        """
        Then verify if existing project
        """
        
if __name__ == '__main__':
    try:
        GenerateData.generate()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)