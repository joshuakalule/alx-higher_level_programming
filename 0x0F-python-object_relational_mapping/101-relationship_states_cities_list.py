#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects."""
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine, asc
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':

    if len(sys.argv) < 3:
        exit()

    url = URL(
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

    query = session.query(State)
    states = query.order_by(asc(State.id)).all()

    for state_obj in states:
        print(f"{state_obj.id}: {state_obj.name}")
        for city_obj in state_obj.cities:
            print(f"    {city_obj.id}: {city_obj.name}")

    session.close()
