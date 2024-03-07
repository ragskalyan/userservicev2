"""
User Exceptions
"""
from logger.log import log_error


class MobileNumberIsNotValid(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        log_error(self.message)
