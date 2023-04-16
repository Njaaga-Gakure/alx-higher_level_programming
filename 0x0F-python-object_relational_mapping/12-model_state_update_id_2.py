#!/usr/bin/python3
"""Update state name."""


import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def update_state():
    """Update state that has an id of 2."""
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    """Upadate state name."""
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == "__main__":
    update_state()
