#!/usr/bin/env python3
'''managing api authentication
'''
from flask import request
from typing import TypeVar, List


class Auth:
    '''defining athentication class
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''ensuring that user is authenticated
        '''
        self.path = path
        self.exclude_paths = excluded_paths
        if path is None:
            return True
        if excluded_paths is None and len(excluded_paths) == 0:
            return True
        for pwds in excluded_paths:
            if path in pwds:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''creating user auth header for request
        '''
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        '''checking the current user
        '''
        return request