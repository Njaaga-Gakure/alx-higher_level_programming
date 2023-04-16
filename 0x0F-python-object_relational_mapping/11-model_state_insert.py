#!/usr/bin/python3
"""Add state."""


import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def add_state():
    """Add state and print it's id."""
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    """Create new state."""
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    """Get id of new state."""
    query = session.query(State)
    state = query.order_by(State.id).filter(State.name == 'Louisiana').first()
    print("{}".format(state.id))
    session.close()


if __name__ == "__main__":
    add_state()
