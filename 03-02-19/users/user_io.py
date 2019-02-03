import json


class UserIO:

    @staticmethod
    def read_user(path):
        try:
            with open(path, mode="r") as file:
                pass
        except FileNotFoundError:
            print("File...")

    @staticmethod
    def write_user(path, user):
        if type(user) is dict:
            with open(path, mode="w") as file:
                pass
        else:
            pass
