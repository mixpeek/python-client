class MixpeekException(Exception):
    pass

class AuthenticationError(MixpeekException):
    pass

class BadRequestError(MixpeekException):
    pass

class NotFoundError(MixpeekException):
    pass

# Define more exceptions as needed
