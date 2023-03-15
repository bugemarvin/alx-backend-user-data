#!/usr/bin/env python3
'''creating a model of users
'''
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    '''
        - Model for users
        Return:
                - users
                - users.id: INTEGER
                - users.email: VARCHAR(250)
                - users.hashed_password: VARCHAR(250)
                - users.session_id: VARCHAR(250)
                - users.reset_token: VARCHAR(250)
    '''
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
