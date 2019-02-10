from user.user_model import User
from user.user_io import UserIO as user_io

user_details = user_io.read_from_file()

if not user_details:
    user = User(name="Avner")
    user_dict = user.from_user_to_dict()
    user_io.write_to_file(user_dict)
    user_details = user_io.read_from_file()

print(user_details)
