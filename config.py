from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def session_config(engine):
    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()
    return session

