#!/usr/bin/python3
"""Class definition of a state and an instamce."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class."""

    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
