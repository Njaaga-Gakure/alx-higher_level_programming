#!/usr/bin/python3
"""Get state by id depending on user input."""


import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def get_state_id():
    """Print id of state based ob user input."""
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = session.query(State)
    state = query.order_by(State.id).filter(State.name == sys.argv[4]).first()
    if (state):
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    get_state_id()
