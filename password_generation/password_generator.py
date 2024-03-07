"""
Password Generator
"""
import string, hashlib
from exceptions.password_exceptions import PasswordLengthIsNotEnough, PasswordDoesNotMeetComplexity, InvalidPassword
from logger.log import log_info, log_error


class PasswordGenerator:

    def __init__(self, password):

        self.length = len(password)
        self.__password = password
        self.symbols = string.punctuation
        self.encrypted_password = None

    def __validate_password(self):
        log_info("Validation Started")
        if self.__password is None:
            raise InvalidPassword("Enter a valid password")
        if len(self.__password) < 12:
            raise PasswordLengthIsNotEnough("Password should contain a minimum of 12 characters")
        if not self.contains_string:
            raise PasswordDoesNotMeetComplexity("Password should contain letters")
        if not self.contains_number:
            raise PasswordDoesNotMeetComplexity("Password should contain numbers")
        if not self.contains_symbol:
            raise PasswordDoesNotMeetComplexity("Password should contain symbols")
        log_info("Validation Completed")

    @property
    def contains_number(self) -> bool:
        return any(char.isdigit() for char in self.__password)

    @property
    def contains_string(self) -> bool:
        return any(char.isalpha() for char in self.__password)

    @property
    def contains_symbol(self) -> bool:
        symbol = set(self.symbols)
        return any(char in symbol for char in self.__password)

    @property
    def is_palindrome(self) -> bool:
        reverse_string = self.__password[::-1]
        return self.__password.lower() == reverse_string.lower()

    def __encrypt(self):
        log_info("Encryption Started")
        message_bytes = self.__password.encode()

        sha256_hash = hashlib.sha256()

        sha256_hash.update(message_bytes)

        hash_digest = sha256_hash.hexdigest()

        return hash_digest

    def main(self) -> bool:

        try:
            self.__validate_password()
            self.encrypted_password = self.__encrypt()
            return True

        except (PasswordDoesNotMeetComplexity, PasswordLengthIsNotEnough) as e:
            log_error(e)
            return False
