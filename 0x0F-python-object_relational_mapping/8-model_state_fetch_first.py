#!/usr/bin/python3
"""List first state module."""


import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def list_first_state():
    """List first state in states table."""
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name)) if state else print("Nothing")
    session.close()


if __name__ == "__main__":
    list_first_state()
