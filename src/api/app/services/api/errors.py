"""
    Standartized API error cpdes container.
"""

from enum import Enum


class ApiErrorCode(Enum):
    """ API Standartized error codes. """

    # Auth field is taken.
    AUTH_USERNAME_TAKEN = 0, 400
    AUTH_EMAIL_TAKEN = 1, 400

    # Auth token.
    AUTH_INVALID_TOKEN = 10, 400
    AUTH_EXPIRED_TOKEN = 11, 400

    # Other auth related.
    AUTH_INVALID_CREDENTIALS = 20, 400
    AUTH_REQUIRED = 21, 401
    AUTH_EMAIL_INVALID = 30, 400
    AUTH_PASSWORD_INVALID = 31, 400
    AUTH_USERNAME_INVALID = 32, 400
    AUTH_INSUFFICIENT_PERMISSSIONS = 33, 403
    
    # API.
    API_INVALID_REQUEST = 40, 400
    API_NOT_IMPLEMENTED = 41, 400
    API_INTERNAL_SERVER_ERROR = 42, 500
    API_METHOD_NOT_FOUND = 43, 404

    # Email confirmation.
    EMAIL_CONFIRMATION_TOKEN_INVALID = 50, 400
    EMAIL_CONFIRMATION_USER_NOT_FOUND = 51, 404
    EMAIL_CONFIRMATION_ALREADY_CONFIRMED = 52, 409

    # OAUTH.
    OAUTH_CLIENT_NOT_FOUND = 60, 404
    OAUTH_CLIENT_FORBIDDEN = 61, 403
    OAUTH_CLIENT_REDIRECT_URI_MISMATCH = 62, 400
    OAUTH_CLIENT_ID_MISMATCH = 63, 400
    OAUTH_CLIENT_SECRET_MISMATCH = 64, 400

    # Other.
    USER_DEACTIVATED = 100, 403
    USER_EMAIL_NOT_CONFIRMED = 101, 403
    USER_NOT_FOUND = 102, 404
    USER_PROFILE_PRIVATE = 103, 403
    USER_PROFILE_AUTH_REQUIRED = 104, 401


class ApiErrorException(Exception):
    def __init__(self, api_code: ApiErrorCode, message: str="", data: dict | None = None):
        self.api_code = api_code
        self.message = message
        self.data = data