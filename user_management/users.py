"""
User Class
"""
from password_generation.password_generator import PasswordGenerator
from exceptions.password_exceptions import InvalidPassword
from exceptions.user_exceptions import MobileNumberIsNotValid
from logger.log import log_info


class UserCreation:

    def __init__(self, first_name, second_name, email_id, mobile_number, password):

        self.first_name = first_name
        self.last_name = second_name
        self.password = self.__encrypt_password(password)
        self.email_id = email_id
        self.mobile_number = self.__validate_mobile_number(mobile_number)

    @staticmethod
    def __encrypt_password(password):
        password_generator = PasswordGenerator(password)
        if password_generator.main():
            log_info("Encryption Completed")
            return password_generator.encrypted_password
        else:
            raise InvalidPassword("Password does not meet the policy")

    @staticmethod
    def __validate_mobile_number(mobile_number):

        if len(mobile_number) == 10 and isinstance(int(mobile_number), int):
            return mobile_number

        else:
            raise MobileNumberIsNotValid("Mobile number should contain 10 digits")

    def to_user(self) -> dict:

        return {
            "first_name": self.first_name,
            "second_name": self.last_name,
            "password": self.password,
            "mobile_number": self.mobile_number,
            "email_id": self.email_id
        }
