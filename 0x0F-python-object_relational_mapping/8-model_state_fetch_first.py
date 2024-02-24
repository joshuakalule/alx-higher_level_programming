#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    if len(sys.argv) < 3:
        exit()

    url = engine.url.URL(
        drivername='mysql',
        username=sys.argv[1],
        password=sys.argv[2],
        host='localhost',
        database=sys.argv[3],
        port=3306,
        query={})

    engine = create_engine(url)

    session = sessionmaker(bind=engine)()

    found = session.query(State).order_by(State.id).first()

    if found:
        print(f"{found.id}: {found.name}")
    else:
        print("Nothing")
