from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(String(30))
    last_name = Column(String, nullable=False)
    experience = Column(Float)
    speed = Column(Float)

    # addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, last_name={self.last_name!r}, experience={self.experience!r}, speed={self.speed!r})"

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(String(30))
    revenue = Column(Integer, nullable=True)
    employees = Column(Integer, nullable=True)
    owner_id = Column(Integer)
    phone =  Column(String, nullable=True)
    company_type = Column(String, nullable=True)

    def __repr__(self):
        return f"Company(id={self.id!r}, name={self.name!r}, revenue={self.revenue!r}, employees={self.employees!r}, owner_id={self.owner_id!r}, phone={self.phone!r}, company_type={self.company_type!r})"


class CompanyHidden(Base):
    __tablename__ = 'companies_hidden'

    company_id = Column(Integer, primary_key = True)
    atractiveness = Column(Float)
    need = Column(Float)
    closeness_to_close = Column(Float)