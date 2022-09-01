import os
from datetime import datetime
import random
from typing import List, Optional
import uuid
from sqlalchemy.orm import Session

from bldrdsh.db.init_db import init_db
from bldrdsh.generate.initial_setup.utils import start_valid_date, open_metadata, write_metadata, read_profile
from bldrdsh.generate.initial_setup.prompt import select_company_profile_prompt
from bldrdsh.classes.Agent import Agent # <- this ???

from bldrdsh.db.models.models import CompanyModel, ContactModel

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
    create_inital_buffer()
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
    
    # Create initial setup functions
    trends = create_trends(profile)
    agents = create_agents(profile)

    # TODO: Store trends & agents in SQLite tables
    # TODO: if all is good return success message

    return agents, trends

def create_trends(profile):
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

def create_agents(profile):
    """
    Small variability functions to add randomness to values <-- This in future AI based
    """
    num_of_agents = profile["agents"]
    list_of_agents = []
    for i in range(num_of_agents):
        new_agent = Agent(profile["type"]).create(i)
        list_of_agents.append(new_agent)
    return list_of_agents

def create_inital_buffer():
    """
    Generate some contacts and companies.
    Assign inital random task to each
    Assign inital random due date to each
    Return them in one DataFrame
    """
    start_time = datetime.now()
    
    # TODO: Pick random number between 1-50. Normal distribution
    number_of_companies = 50
    # This will be the number of initial companies
    # TODO: Add number code to each uuid -> companies = 01, contacts, 02. Use constant seed. for maximum entropy <- what does it mean?
    engine = init_db()
    companies = Company.create_many(number_of_companies)
    contacts = Contact.create_from_many_companies(companies)
    session = Session(engine)
    for i in companies:
       session.add(i)
    for i in contacts:
        session.add(i)
    session.commit()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    # Given that number of COs, generate COs and contacts.
    return 'db created! + summary'

def assign_inital_batch():
    """
    Assign contacts and companies from SQLite
    to each agent.
    """
    pass


def generate_companies():
    # for i in range(len(number_of_companies))
    #   company = generate.company(mode='standard')
    # generate.company() include check in db latest company -> incremental number (on top of uuid)
    # Add as hidden value original_batch, uuid, 
    #   push_to_db()
    pass


class Company():
    def _create(i: Optional[int] = None):
        company = {}
        company['name'] = f'company_{i}'
        company['revenue'] = 1000 + i
        company['uuid'] = str(uuid.uuid4())
        new_co = CompanyModel(**company)
        return new_co
    
    def create_one()->list:
        new_one = Company._create(1)
        print('Company created!')
        return list(new_one)
    
    def create_many(how_many:int)->list:
        list_of = []
        for i in range(how_many):
            one = Company._create(i)
            list_of.append(one)
        print('Companies created!')
        return list_of
    
    def create_from_contact():
        pass

class Contact():
    def _create(j, i):
        contact = {}
        contact['name'] = f'contact_{j}'
        contact['uuid'] = str(uuid.uuid4())
        contact['company_uuid'] = i.uuid
        
        new_contact = ContactModel(**contact)
        return new_contact
    def create_from_many_companies(companies: List): # List of companies
        list_of_contacts = []
        for i in companies:
            number_of_contacts = random.choice([1,2])
            for j in range(number_of_contacts):
                new_contact = Contact._create(j, i)
                list_of_contacts.append(new_contact)
        print('Contacts created!')
        return list_of_contacts

        pass
    def create_from_one_company(company): # Company type
        pass

    def create(): # create contact. Inside add Company.create_from_contact()
        pass

    def add_one(company): # add 1 contact to existing company
        pass

    def add_more_than_one(company):
        pass


def delete_db():
    myfile="some.db"

    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
        print('DB deleted.')
    else:    ## Show an error ##
        print("Error: %s file not found" % myfile)