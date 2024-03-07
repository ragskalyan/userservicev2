"""
Password Exceptions
"""
from logger.log import log_error


class PasswordLengthIsNotEnough(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        log_error(self.message)


class PasswordDoesNotMeetComplexity(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        log_error(self.message)


class InvalidPassword(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        log_error(self.message)


