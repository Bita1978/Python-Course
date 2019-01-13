class Book:

    def __init__(self, name, genre, pages_amount):
        self.name = name
        self.genre = genre
        self.pages_amount = pages_amount

    def __len__(self):
        return self.pages_amount


my_book = Book("Harry Potter", "Fantasy", 320)
print(len(my_book))

class Person:

    def __init__(self, name="", age=None, hobby=''):
        self.name = name
        self.age = age
        self.hobby = hobby

    def __str__(self):
        return f"Person [name: {self.name}, age: {self.age}, hobby: {self.hobby}] "

p4 = Person(7)
p5 = Person(age="", hobby=8, name="Secret name!!")

print(p5.name)


class Person:

    def __init__(self ,some_x):
        self.set_x(some_x)

    def get_x(self):
        return self.__x

    def set_x(self, some_x):
        if type(some_x) is not int:
            print("Not cool..")
            return
        self.__x = some_x


p = Person("k")

class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name.lower() == "maor":
            print("Not cool")
            return
        self.__name = new_name



p = Person("Avner")
print(p.name)
p.name = "Itay"
print(p.name)