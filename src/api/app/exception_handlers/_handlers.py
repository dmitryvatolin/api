"""
    Florgon server API exception handlers.
    (FastAPI exception handlers)
"""

from app.services.api.response import api_error


from app.services.api.errors import ( 
    ApiErrorCode, 
    ApiErrorException
)


async def _validation_exception_handler(_, exception):
    """ Custom validation exception handler. """
    return api_error(ApiErrorCode.API_INVALID_REQUEST, "Invalid request!", {
        "exc": str(exception)
    })


async def _too_many_requests_handler(_, exception):
    return api_error(ApiErrorCode.API_TOO_MANY_REQUESTS, "Too Many Requests!", {
        "retry-after": int(exception.headers["Retry-After"])
    }, headers=exception.headers)


async def _api_error_exception_handler(_, e: ApiErrorException):
    return api_error(e.api_code, e.message, e.data)


async def _not_found_handler(_, __):
    return api_error(ApiErrorCode.API_METHOD_NOT_FOUND, "Method not found!")


async def _internal_server_error_handler(_, __):
    return api_error(ApiErrorCode.API_INTERNAL_SERVER_ERROR, "Internal server error!")


async def _token_wrong_type_error_handler(_, __):
    return api_error(ApiErrorCode.AUTH_INVALID_TOKEN, "Token has wrong type!")


async def _token_expired_error_handler(_, __):
    return api_error(ApiErrorCode.AUTH_EXPIRED_TOKEN, "Token has been expired!")


async def _token_invalid_signature_error_handler(_, __):
    return api_error(ApiErrorCode.AUTH_INVALID_TOKEN, "Token has invalid signature!")


async def _token_invalid_error_handler(_, __):
    return api_error(ApiErrorCode.AUTH_INVALID_TOKEN, "Token invalid!")