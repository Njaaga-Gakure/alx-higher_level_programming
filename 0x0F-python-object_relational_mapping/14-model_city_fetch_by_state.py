#!/usr/bin/python3
"""List cities module."""


import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def list_cities():
    """List cities."""
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    list_cities()
