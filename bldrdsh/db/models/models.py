from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class AgentModel(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(String(30))
    last_name = Column(String, nullable=False)
    experience = Column(Float)
    speed = Column(Float)

    # addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, last_name={self.last_name!r}, experience={self.experience!r}, speed={self.speed!r})"

class CompanyModel(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(String(30))
    uuid = Column(String, nullable=False)
    revenue = Column(Integer, nullable=True)
    employees = Column(Integer, nullable=True)
    owner_id = Column(Integer)
    phone =  Column(String, nullable=True)
    company_type = Column(String, nullable=True)

    contacts = relationship('ContactModel', back_populates='company')


    def __repr__(self):
        return f"Company(id={self.id!r}, name={self.name!r}, uuid={self.uuid}, revenue={self.revenue!r}, employees={self.employees!r}, owner_id={self.owner_id!r}, phone={self.phone!r}, company_type={self.company_type!r}, contacts={self.contacts!r})"


class CompanyHiddenModel(Base):
    __tablename__ = 'company_hidden'

    company_id = Column(Integer, primary_key = True)
    atractiveness = Column(Float)
    need = Column(Float)
    closeness_to_close = Column(Float)

class ContactModel(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(String(30))
    uuid = Column(String, nullable=False)
    company_uuid = Column(String)
    phone =  Column(String, nullable=True)

    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship('CompanyModel', back_populates='contacts')

    def __repr__(self):
        return f"Contact(id={self.id!r}, name={self.name!r}, uuid={self.uuid!r}, company_uuid={self.company_uuid!r}, phone={self.phone!r}, company={self.company!r})"
