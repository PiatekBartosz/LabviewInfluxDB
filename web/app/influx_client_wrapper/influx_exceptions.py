class UnknownException(Exception):
    DESCRITPION = "Unknown exception"


class InfluxNotAvailableException(Exception):
    HTTP_RESPONSE_STATUS_CODE = 503
    DESCRITPION = "Enable to connect to InfluxDB"


class InternalServerException(Exception):
    HTTP_RESPONSE_STATUS_CODE = 500
    DESCRIPTION = "Internal server error"


class TooManyRequestsException(Exception):
    HTTP_RESPONSE_STATUS_CODE = 429
    DESCRIPTION = "Too many requests"


class UnprocessableEntryException(Exception):
    HTTP_RESPONSE_STATUS_CODE = 422
    DESCRIPTION = "Unauthorized"


class RequestEntityTooLargeException(Exception):
    HTTP_RESPONSE_STATUS_CODE = 413
    DESCRIPTION = "Request entity too large exception"


class NotFoundException(Exception):
    HTTP_RESPONSE_STATUS_CODE = 404
    DESCRITPION = "Resource not found"


class UnauthorizedException(Exception):
    HTTP_RESPONSE_STATUS_CODE = 401
    DESCRIPTION = "Unauthorized"

class BadRequest(Exception):
    HTTP_RESPONSE_STATUS_CODE = 400
    DESCRITPION = "Bad request"
