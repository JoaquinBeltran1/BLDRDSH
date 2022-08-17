from bldrdsh.classes.Base import Base
class Agent(Base):
    def __init__(self, profile_type):
        self.profile_type = profile_type

    def test(self):
        if self.profile_type == "default":
            print("Using Default profile")
            return None
        elif self.profile_type == "startup":
            print("Using Startup profile")
            return None
        elif self.profile_type == "incumbent":
            print("Using Incumbent profile")
            return None
        else:
            # TODO: Return a proper error. Folder Exception/errors
            print("Something went wrong, and it shouldn't!")
    
    def create(self,  agent_number: int):
        agent_uuid = create_uuid(agent_number)
        agent_skills = {
            "experience": 0.5,
            "speed": 0.5
        }
        agent = {
            'uuid': agent_uuid,
            'skills': agent_skills
        }
        return agent


def create_uuid(num: int):
    uuid = num + 10
    return uuid