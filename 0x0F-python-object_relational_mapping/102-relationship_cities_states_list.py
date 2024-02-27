#!/usr/bin/python3
"""Lists all City objects from the database."""
from sqlalchemy import create_engine, asc
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from relationship_city import City
import sys


if __name__ == "__main__":

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

    query = session.query(City).order_by(asc(City.id)).all()

    for city_obj in query:
        print(f"{city_obj.id}: {city_obj.name} -> {city_obj.state.name}")

    session.close()
