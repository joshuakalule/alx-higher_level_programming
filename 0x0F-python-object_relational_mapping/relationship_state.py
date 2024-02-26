#!/usr/bin/python3
"""Class definition of a state with relationship."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class."""

    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
