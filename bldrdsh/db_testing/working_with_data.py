from sqlalchemy import create_engine, insert, Table, Column, Integer, String, MetaData, select, ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship

metadata_obj = MetaData()

engine = create_engine("sqlite:///some.db", future=True)


user_table = Table(
    "user_account",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)

def select_user(user:str):
    stmt = select(user_table).where(user_table.c.name == user)
    print(stmt)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)

def insert_stmt(name:str, fullname:str):
    stmt = insert(user_table).values(name=name, fullname=fullname)
    print(stmt)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()


def order_by():
    stmt = select(user_table).order_by(user_table.c.name)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        print(result.all())
########################################################
Base = declarative_base()

class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key = True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname = {self.fullname!r})"

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key = True)
    email_address = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

def select_user_orm(user:str):
    stmt = select(User).where(User.name == user)
    with Session(engine) as session:
        for row in session.execute(stmt):
            print(row)
def select_first_orm():
    with Session(engine) as session:
        row = session.execute(select(User)).first()
    return row

def order_by():
    stmt = select(User).order_by(User.fullname)
    with Session(engine) as session:
        for row in session.execute(stmt):
            print(row)

def order_by_desc_orm():
    stmt = select(User).order_by(User.fullname.desc())
    with Session(engine) as session:
        for row in session.execute(stmt):
            print(row)
