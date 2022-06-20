import os
import sys

from bldrdsh.generate.new_project import create_project_prompt

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
    
    
    def generate():
        # Check if exisiting and valid project -->

        # If there is set path to its location. Apply all next function into that path

        # --------------------------

        # If project has metadata but its corrupted -->

        # -------------------------

        # If there is no project -->
        create_project_prompt()
        # Automatically rerun check if existing and valid project
