import re


class User:

    def __init__(self, username, password, email, phone_number):
        self.set_username(username)
        self.set_password(password)
        self.set_email(email)
        self.set_phone_number(phone_number)

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def set_username(self, username):
        # Username's length has to be between 4 and 20.
        # No _ or . at the beginning
        # No _ or . at the end
        pattern = re.compile(r"^(?=.{4,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")

        if pattern.search(username):
            self.__username = username
        else:
            raise ValueError("Wrong username")

    def set_password(self, password):
        # Password must be at least 4 characters, no more than 8 characters
        # Must include at least one upper case letter
        # At least one lower case letter
        # At least one numeric digit.
        pattern = re.compile(r"^(?=.*\d).{4,8}$")

        if pattern.search(password):
            self.__password = password
        else:
            raise ValueError("Wrong password")

    def set_email(self, email):
        pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        if pattern.search(email):
            self.__email = email
        else:
            raise ValueError("Invalid email")

    def set_phone_number(self, phone_number):
        # Mongolian phone number pattern: 8 consecutive numbers
        # Ex: 99674769
        pattern = re.compile(r"^[0-9]{8}$")

        if pattern.search(phone_number):
            self.__phone_number = phone_number
        elif phone_number == "":
            self.__phone_number = ""
        else:
            raise ValueError("Invalid phone number")
