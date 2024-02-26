#!/usr/bin/python3
"""Creates the State 'Carlifornia' with the City 'San Fransisco'."""
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
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
    # emit DDL to the database 'CREATE IF NOT EXISTS.. etc'
    Base.metadata.create_all(engine)

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)

    session.add_all([new_state, new_city])

    session.commit()
