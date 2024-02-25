#!/usr/bin/python3
"""Lists all State objects that contain the letter a."""
import sys
from sqlalchemy import create_engine, engine, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    session = sessionmaker(bind=engine)()

    query_obj = session.query(State).filter(State.name.contains('a'))
    rows = query_obj.order_by(State.id).all()

    for obj in rows:
        print(f"{obj.id}: {obj.name}")

    session.close()
