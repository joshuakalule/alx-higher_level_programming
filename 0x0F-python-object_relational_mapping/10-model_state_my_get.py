#!/usr/bin/python3
"""Prints the State object with the name passed as argument."""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    if len(sys.argv) < 4:
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

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    try:
        found = session.query(State).filter(State.name == sys.argv[4]).one()
        print(found.id)
    except Exception:
        print("Not found")

    session.close()
