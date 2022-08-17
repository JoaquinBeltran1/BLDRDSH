from sqlalchemy import create_engine

from bldrdsh.db.models.models import Base

def init_db():
    """
    Create DB
    """
    engine = create_engine("sqlite:///some.db", echo=True, future=True)
    Base.metadata.create_all(engine)
    return engine