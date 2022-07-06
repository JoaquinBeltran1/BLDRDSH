from datetime import datetime
from bldrdsh.batch.utils import start_valid_date, open_metadata, write_date_metadata


def initial_setup():
    """
    For new projects, first prompt
    """
    """
    because new project:
        company size prompt: <- only select 1: - default from python inquirer list
            random distr algo create agents - prompt !!! How many agents -> Agent 01 skill: 1, 2, or 3. Agent 0X skil: ...
            random distr algo create trends - prompt !!! Define some macro and micro trends. Market, product-market fit. Tech adoption stage.
            Create company and market summary file -> in future Generate scenario. Do you like it? Y/n. if no generate a new one.
    """

    # Start date ting
    start_date = start_valid_date()

    metadata = open_metadata() # metadata.json
    metadata['starting_date'] = start_date
    # write to metadata.json
    # write_date_metadata(data)

    # prompt company + market type, only 1 availble for now
    """
    pass company + market type number to generate funcs. Given X, generate accordingly.
    """
    print('up to aaaa')
    generate_agents()
    generate_trends()
    return metadata

    # set initial trends to trends file

def generate_agents():
    print('generate agenaaaaaats')

def generate_trends():
    print('generate trends')