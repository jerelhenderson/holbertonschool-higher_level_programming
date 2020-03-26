#!/usr/bin/python3
"""
contains class definition of City and instance of Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

City = declarative_base()


class City(Base):
    ''' inherits from Base '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('States.id'), nullable=False)
