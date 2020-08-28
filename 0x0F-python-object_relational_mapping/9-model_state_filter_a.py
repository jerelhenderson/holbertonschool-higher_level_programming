#!/usr/bin/python3
"""
lists all `State` objects from database containing 'a'
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State).order_by(State.id).all():
        if 'a' in result.name:
            print("{}: {}".format(result.id, result.name))

    session.close()
