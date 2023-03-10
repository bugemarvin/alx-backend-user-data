#!/usr/bin/env python3
'''managing api authentication
'''
from flask import request
from typing import Optional, TypeVar, List


class Auth:
    '''defining athentication class
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''ensuring that user is authenticated
        '''
        self.path = path
        self.exclude_paths = excluded_paths
        if excluded_paths == []:
            return True
        if path is None:
            return True
        if excluded_paths is None:
            return True
        for pwds in excluded_paths:
            if path in pwds:
                return False
        if path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        '''creating user auth header for request
        '''
        self.request = request
        if request is None:
            return None
        if not request or not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''checking the current user
        '''
        return request
