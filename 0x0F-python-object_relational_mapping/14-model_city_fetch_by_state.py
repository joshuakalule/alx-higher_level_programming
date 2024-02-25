#!/usr/bin/python3
"""Prints all City objects from the database."""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, engine, asc
from model_city import City
from model_state import State

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

    try:
        query = session.query(City, State).join(State)
        rows = query.order_by(asc(City.id)).all()
        for city_obj, state_obj in rows:
            print("{}: ({}) {}".format(state_obj.name,
                                       city_obj.id, city_obj.name))
    except Exception:
        pass

    session.close()
