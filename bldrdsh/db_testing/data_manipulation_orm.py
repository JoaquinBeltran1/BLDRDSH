from sqlalchemy.orm import Session
from bldrdsh.db_testing.working_with_data import engine, User, Address

def test():
    squidward = User(name="squidward", fullname="Squidward Tentacles")
    print(squidward)

krabs = User(name='ehkrabs', fullname='Eugene H. Krabs')

session = Session(engine)

def add_orm(name:str, fullname:str):
    new_user = User(name=name, fullname=fullname)
    print(new_user)
    session.add(new_user)
    print(session.new)

def flush():
    session.flush()
    # Doesn't commit automatically
    session.commit()