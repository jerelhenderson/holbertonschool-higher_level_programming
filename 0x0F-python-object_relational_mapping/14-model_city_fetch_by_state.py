#!/usr/bin/python3
"""
create a class definition 'City'
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

new_state = "New Mexico"


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(State, City).filter(City.state_id \
                                                  == State.id):
        print ("{}: ({}) {}".format(city[0].name, \
                                     city[1].id, \
                                     city[1].name))

    session.close()
