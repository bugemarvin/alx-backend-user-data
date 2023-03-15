#!/usr/bin/env python3
'''Basic auths
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''creating a basicauth for header authorization
        Return
            - Base64 header
    '''

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        pass
