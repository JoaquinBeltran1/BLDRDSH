import json
import inquirer
from pathlib import Path

from bldrdsh.batch.utils import push_to_db, start_valid_date, open_metadata, write_metadata
from bldrdsh.classes.Agent import Agent

def initial_setup():
    """
    For new projects, first prompt
    """
    """
        Create company and market summary file -> in future Generate scenario. Do you like it? Y/n. if no generate a new one.
    """

    # Start date ting <- returns a valid date to start the project from
    start_date = start_valid_date()

    metadata = open_metadata() # Read and load metadata.json
    metadata['starting_date'] = start_date # Add the selected date from prompt
    write_metadata(metadata) # Override old file.

    agents_trends = generate_company()
    print('This is the metadata content:',metadata)
    print('Printing from inital setup:', agents_trends)
    return None
    
    # return "Initial setup done! Ready to start the batch."


def generate_company():
    """
    Aggregate generating functions here.
    Generate and store trends and agents in JSON file.
    """
    company_profile = select_company_profile_prompt()
    for k, v in company_profile.items():
        value = v

    # Selected profile
    profile = read_profile(value)
    
    # Generate initial setup functions
    trends = generate_trends(profile)
    agents = generate_agents(profile)

    # TODO: Store trends & agents in SQLite tables
    # TODO: if all is good return success message

    return agents, trends
    

def select_company_profile_prompt():
    """
    Prompt with list to select company profile
    1, 2, or 3.
    """
    questions = [
    inquirer.List('company_profile',
                    message="What company profile do you want to choose?",
                    choices=[('Default', 1), ('Early startup',2), ('Incumbent', 3)],
                ),
    ]
    select_company_profile = inquirer.prompt(questions) # TODO: V2 Complex prompt with rich, explanatory text (?). Python inquirer list or Typer + Rich

    return select_company_profile


def read_profile(profile_num: int):
    """
    Read profile values from JSON given profile num. In JSON file store 3 profiles.
    return dict with selected profile values.
    """
    cwd = Path(__file__).parent.parent
    with open(cwd / 'params/company_profiles.json') as f:
        profiles = json.load(f)

    profile = next((profile for profile in profiles if profile["id"] == profile_num), None)
    return profile

def generate_trends(profile):
    # TODO: take profile selected
    """
    Read dict with values. Values can only be correct.

    Small variability functions to add randomness to values <-- This in future AI based

    Save trends in trends.json in correct folder
    """


    # TODO: There is a set monthly/yearly growth: given lengh of batch, and modification in trends, adapt this growth to daily <-- this affects daily results.
    trends = {
        'main_trend': 'default'
    }
    # TODO: store trends in SQL table
    return trends

def generate_agents(profile):
    """
    Small variability functions to add randomness to values <-- This in future AI based
    """
    num_of_agents = profile["agents"]
    list_of_agents = []
    for i in range(num_of_agents):
        new_agent = Agent(profile["type"]).create(i)
        list_of_agents.append(new_agent)
    return list_of_agents

def generate_inital_buffer():
    """
    Generate some contacts and companies.
    Assign inital random task to each
    Assign inital random due date to each
    Return them in one DataFrame
    """

    # Pick random number between 1-50. Normal disitrbution
    number_of_companies = 50
    # This will be the number of initial companies
    # TODO: Add number code to each uuid -> companies = 01, contacts, 02. Use constant seed. for maximum entropy <- what does it mean?
    # Given that number of COs, generate COs and contacts.
    # Use Company and Contact classes
    # Standard creation: 1 company = 1 or more contacts
    # They should be dicts to be stored in DB (using sqlalchemy models)
    # store in db class. Pass in each dataframe. These classes are VERY IMPORTANT!

    pass

def assign_inital_batch():
    """
    Assign contacts and companies from JSON
    to each agent.
    """
    pass

def initial_db_setup():
    """
    Create inital db and tables
    Enter initial data to each table
    """

def generate_companies():
    # for i in range(len(number_of_companies))
    #   company = generate.company(mode='standard')
    # generate.company() include check in db latest company -> incremental number (on top of uuid)
    # Add as hidden value original_batch, uuid, 
    #   push_to_db()
    pass