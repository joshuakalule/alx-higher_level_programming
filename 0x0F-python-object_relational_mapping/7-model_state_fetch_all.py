#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    if len(sys.argv) < 3:
        exit()

    # mysql://kalule:kalule@localhost:3306/hbtn_0e_6_usa
    url = engine.url.URL(
        drivername='mysql',
        username=sys.argv[1],
        password=sys.argv[2],
        host='localhost',
        database=sys.argv[3],
        port=3306,
        query=dict())

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    for obj in session.query(State).order_by(State.id):
        print(f"{obj.id}: {obj.name}")

    session.close()
