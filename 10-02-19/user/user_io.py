import json
from user.utils import Utils as utils


class UserIO:

    __path = 'user.txt'

    @classmethod
    def set_path(cls, new_path):
        if type(new_path) is not str:
            utils.print_illegal_value(new_path)
            return
        cls.__path = new_path


    @classmethod
    def read_from_file(cls):
        try:
            with open(cls.__path, mode="r") as file:
                return json.loads(file.read())
        except Exception as err:
            print(f" Error - {err}")

    @classmethod
    def write_to_file(cls, user):
        if type(user) is not dict:
            utils.print_illegal_value(user)
            return
        try:
            with open(cls.__path, mode="w") as file:
                file.write(json.dumps(user))
        except Exception as err:
            print(f"Error - {err}")
