"""
Task 1
"""


class Person:

    def __init__(self, fname, lname, age):
        self.__full_name = f"{fname} {lname}"
        self.__age = self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 1 or new_age > 120:
            print("Illegal age")
            self.__age = 0
            return
        self.__age = new_age

    @property
    def full_name(self):
        return self.__full_name

    def __str__(self):
        return f"Person({self.full_name}, {self.age})"


# p1 = Person("Gil", "Ehud", 43)
# p2 = Person("Dana", "Reuven", -9)
# p3 = Person("Oded", "Ben", 8)
#
# p_list = []

# for i in range(3):
#     p = Person(input("Enter first name:\n"),
#                input("Enter last name:\n"),
#                int(input("Enter age:\n")))
#     p_list.append(p)


"""
Task 2
"""


class Friends:

    __friends = []

    @property
    def friends(self):
        return self.__friends

    def add_friend(self, name):
        if name in self.friends:
            print(f"{name} already exists...")
            return
        self.friends.append(name)

    def remove_friend(self, name):
        if name not in self.friends:
            print(f"Friend {name} does not exists")
            return
        self.friends.remove(name)


# f = Friends()
# print(f.friends)
# f.add_friend("Liat")
# f.add_friend("Liat")
# f.add_friend("Itay")
# print(f.friends)
# f.remove_friend("Shalom")
# f.remove_friend("Liat")
# print(f.friends)

"""
Task 3
"""


class Calc:

    __operator_types = ('+', '-', '*', '/', '%')
    __operator_err_msg = f"Illegal operator, Please change:\n" \
                         f"{__operator_types}"

    def __init__(self, operator):
        self.__operator = self.operator = operator

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator):
        while operator not in self.__operator_types:
            operator = input(self.__operator_err_msg + '\n')
        self.__operator = operator

    def perform(self, num1, num2):
        if self.operator == '+':
            return num1 + num2
        elif self.operator == '-':
            return num1 - num2
        elif self.operator == '*':
            return num1 * num2
        elif self.operator == '/':
            if num2 == 0:
                print("Error, can not preform subdivision with 0")
                return
            return num1 / num2
        elif self.operator == '%':
            return num1 % num2
        else:
            self.operator = '?'


c = Calc('?')
results = c.perform(7, 0)
print(results)
