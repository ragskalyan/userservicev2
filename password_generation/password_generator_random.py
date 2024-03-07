"""
Password Generator
"""
import random
import string
from exceptions.password_exceptions import PasswordLengthIsNotEnough, PasswordDoesNotMeetComplexity


class PasswordGenerator:

    def __init__(self, password_length=12):
        print("Welcome to Password Generator Application")

        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.symbols = string.punctuation

        if password_length < 12:
            raise PasswordLengthIsNotEnough("Password should contain minimum of 12 characters")
        else:
            self.length = password_length

        self.password = None

    def __generate_password(self):

        password = []

        for _ in range(self.length):
            password.append(random.choice(self.uppercase + self.lowercase + self.digits + self.symbols))

        return "".join(password)

    def __validate_password(self):

        validate_password = (
            self.contains_string, self.contains_symbol, self.contains_number
        )

        if False in validate_password:
            raise PasswordDoesNotMeetComplexity("Password does not meet complexity")
        else:
            return "Password validated successfully"

    @property
    def contains_number(self) -> bool:
        return any(char.isdigit() for char in self.password)

    @property
    def contains_string(self) -> bool:
        return any(char.isalpha() for char in self.password)

    @property
    def contains_symbol(self) -> bool:
        symbol = set(self.symbols)
        return any(char in symbol for char in self.password)

    def main(self) -> bool:

        try:
            self.password = self.__generate_password()
            self.__validate_password()
            return True

        except PasswordDoesNotMeetComplexity as e:
            print(e)
            return False


if __name__ == "__main__":

    try:
        password_generator = PasswordGenerator()

        if password_generator.main():
            print(f"The Generated Password is {password_generator.password}")

    except PasswordLengthIsNotEnough as err:
        print(err)
