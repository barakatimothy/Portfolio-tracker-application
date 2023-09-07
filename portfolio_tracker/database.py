from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def init_db(db_uri):
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()
