import argparse
from user_management.users import UserCreation
from exceptions.password_exceptions import InvalidPassword
from exceptions.user_exceptions import MobileNumberIsNotValid
from logger.log import log_info, log_error


def create_user(args):
    try:
        user = UserCreation(
            args.first_name,
            args.last_name,
            args.email,
            args.mobile_number,
            args.password
        )
        return user.to_user()
    except (MobileNumberIsNotValid, InvalidPassword) as e:
        log_error(e)
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new user")
    parser.add_argument("first_name", help="First name of the user")
    parser.add_argument("last_name", help="Last name of the user")
    parser.add_argument("email", help="Email ID of the user")
    parser.add_argument("mobile_number", help="Mobile number of the user")
    parser.add_argument("password", help="Password for the user")
    args = parser.parse_args()

    user_info = create_user(args)

    if user_info:
        print("User created successfully")
        print(user_info)
        log_info("User created successfully")
        log_info(user_info)
    else:
        print("Failed to create user")
        log_error("Failed to create user")
