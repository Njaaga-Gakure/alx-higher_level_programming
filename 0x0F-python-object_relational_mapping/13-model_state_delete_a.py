#!/usr/bin/python3
"""Delete states."""


import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def delete_states():
    """Delete states that have the character 'a'."""
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    """Delete states containing letter 'a'."""
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states()
