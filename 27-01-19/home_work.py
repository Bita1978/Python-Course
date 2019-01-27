"""
Task 1
"""


class App:

    app_version = 0

    def __init__(self, app_name):
        self.__app_name = app_name

    @property
    def name(self):
        return self.__app_name

    @classmethod
    def update_version(cls, new_version):
        if new_version > cls.app_version:
            cls.app_version = new_version

    def __str__(self):
        return f"App (name = {self.name}, version = {self.app_version})"


app1 = App("What's App")
app2 = App("Chrome Browser")
app3 = App("Facebook")

App.update_version(-9)


def print_args(*args):
    for a in args:
        print(a)
    print(f"Done {'-' * 30}")


# print_args(app1, app2, app3)
App.update_version(8)
# print_args(app1, app2, app3)


"""
Task 2
"""


class Filter:

    @staticmethod
    def is_str(content):
        return type(content) is str

    @staticmethod
    def is_empty(content):
        return len(content) == 0

    @staticmethod
    def to_title(content):
        return content.title()


content1 = "python is awesome"
content2 = 9


def using_filter(content):
    if Filter.is_str(content):
        if not Filter.is_empty(content):
            return Filter.to_title(content)
    return content


content1 = using_filter(content1)
content2 = using_filter(content2)

# print_args(content1, content2)


"""
Task 3
"""


class Animal:

    def __init__(self, name):
        self.__name = name
        self.__speak_msg = f"Hello my name is {self.name}"

    @property
    def name(self):
        return self.__name

    @property
    def speak_msg(self):
        return self.__speak_msg

    def speak(self):
        return self.speak_msg


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed

    @property
    def breed(self):
        return self.__breed

    def speak(self):
        if self.breed.lower() == 'pincher':
            return f"{self.speak_msg} " * 2
        return self.speak_msg


class Cat(Animal):

    def __init__(self, name, spot):
        super().__init__(name)
        self.__spot = spot

    @property
    def spot(self):
        return self.__spot

    def speak(self):
        if self.spot.lower() == 'kitchen':
            return self.speak_msg
        return "Not interested."


dog1 = Dog(name="Cashew", breed="mixed")
dog2 = Dog(name="Charlie", breed="pincher")

cat1 = Cat(name="Alfredo", spot="badroom")
cat2 = Cat(name="Mitsi", spot="kitchen")

# print(dog1.speak())
# print(dog2.speak())
# print(cat1.speak())
# print(cat2.speak())
