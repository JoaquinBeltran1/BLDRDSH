from sqlalchemy import select
from sqlalchemy.orm import Session
from bldrdsh.db_testing.working_with_data import engine, User, Address

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

def select_user(name:str):
    user = session.execute(select(User).filter_by(name=name)).scalar_one()
    print(user)
    return user