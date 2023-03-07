#!/usr/bin/env python3
'''managing api authentication
'''
from typing import TypeVar, List
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''ensuring that user is authenticated
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''creating user auth header for request
        '''
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        '''checking the current user
        '''
        return request
