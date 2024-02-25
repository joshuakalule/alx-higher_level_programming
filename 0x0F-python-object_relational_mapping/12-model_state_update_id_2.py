#!/usr/bin/python3
"""Changes the name of a State object from the database."""
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

    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = 'New Mexico'
        session.commit()

    session.close()
