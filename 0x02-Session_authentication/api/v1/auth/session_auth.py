#!/usr/bin/python3
"""
    Authentication for Module for SessionAuthentication
    """
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):

    user_id_by_session_id = []

    def create_session(self, user_id: str = None) -> str:

        if user_id is None:
            return None
        if user_id is not str:
            return None
        else:
            session_id = str(uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        if session_id is None:
            return None
        if session_id is not str:
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):

        session_id = self.session_cookie(request)

        if session_id is None:
            return None

        user_id = self.user_id_by_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):

        if request == None:
            return False
        session_id = self.session_cookie(request)

        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return False

        try:
            del self.user_id_by_session_id['session_id']
        except Exception:
            pass
        return True
