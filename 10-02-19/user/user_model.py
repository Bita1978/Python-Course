from user.utils import Utils as utils


class User:

    def __init__(self, name, points=0, lives=3):
        self.__name = name
        self.__points = points
        self.__lives = lives

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name:
            utils.print_illegal_value(new_name)
            return
        self.__name = new_name

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, new_value):
        if type(new_value) is not int:
            utils.print_illegal_value(new_value)
            return
        self.__points = new_value

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, new_value):
        if type(new_value) is not int:
            utils.print_illegal_value(new_value)
            return
        self.__lives = new_value

    def __str__(self):
        return f"User (Name: {self.name}, Points: {self.points}, Lives: {self.lives})"

    def from_user_to_dict(self):
        return {
            'name': self.name,
            'points': self.points,
            'lives': self.lives
        }


