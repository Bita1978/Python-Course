"""
Static & Class Methods
"""

class Employee:

    salary = 19000

    def __str__(self):
        return f"{self.salary}"

    def this_is_me(self):
        print_all(self)

    @classmethod
    def increase_salary(cls):
        cls.salary += 100


e1 = Employee()
e2 = Employee()
e3 = Employee()

e1.salary += 990

Employee.increase_salary()



def print_all(*args):
    for e in args:
        print(e)

# print_all(e1,e2, e3)
# Initial health for all


"""
Static Method
"""


class Utils:

    @staticmethod
    def add_3(number):
        return number + 3

    @staticmethod
    def print_some(some):
        print(f"{some}")


x = Utils.add_3(6)
Utils.print_some(x)
#

