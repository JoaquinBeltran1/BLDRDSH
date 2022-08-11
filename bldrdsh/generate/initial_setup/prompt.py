import inquirer

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
    """
    After printing agent + trends, new prompt: how many initial companies? 5, 50, 100?. Create them, and tasks. Then force to normal batch prompt. Not in this file!
    """

    return select_company_profile
