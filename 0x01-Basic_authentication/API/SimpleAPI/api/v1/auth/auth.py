#!/usr/bin/python3
from flask import request
from typing import List, TypeVar


class Auth:
    """This Class contain three function
    to define list of authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return()

    def authorization_header(self, request=None) -> str:
        return()

    def current_user(self, request=None) -> TypeVar('User'):
        return()
