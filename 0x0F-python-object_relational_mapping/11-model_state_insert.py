#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, engine, text
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    if len(sys.argv) < 3:
        exit()

    url = engine.url.URL(
        drivername='mysql',
        username=sys.argv[1],
        password=sys.argv[2],
        host='localhost',
        port=3306,
        database=sys.argv[3],
        query={})

    engine = create_engine(url)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name='Louisiana')

    session.add(new_state)

    session.commit()

    print(new_state.id)

    session.close()
