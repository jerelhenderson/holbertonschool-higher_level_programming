#!/usr/bin/python3
"""
prints all `State` object with 'name' from database
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

found_obj = 0


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State).order_by(State.id):
        if found in result.name:
            found_obj = found_obj + 1
            print("{}".format(found.id))
        else:
            print("Not found")

    session.close()
