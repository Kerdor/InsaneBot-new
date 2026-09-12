from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass


import bot.storage.models

engine = create_engine('sqlite:///data/bot.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)