#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User
import typing


class DB(User):
    """DB class
    """
    id = User.id

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
            return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add_user

        Args:
            from User.email as email
            from User.hashed_password as hashed_password

        Returns:
            user as an object in db from email with hashed_password
        """
        self.email = email
        self.hashed_password = hashed_password
        user = User(email=email, hashed_password=hashed_password)
        my_session = self._session
        try:
            my_session.add(user)
            my_session.commit()
        except Exception:
            user = None
        return user
