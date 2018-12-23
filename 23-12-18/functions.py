"""
Creating a function - Definition
"""


def print_hi():
    print('hi')


def print_with_name(name):
    print(f'Hi {name}')


print_with_name("Enosh")


def print_name_age(name, age=23):
    print(f'Hi {name} your age is {age}')


print_name_age("Avner")


def create_person(name='avner', age=18, location={}):
    person = {
        'name': name,
        'age': age,
        'location': location
    }

    print(person)

#
# create_person('Itay', 43, {'city': 'Herzelia', 'street': 'Ha Maskit', 'number': 2})

# def create_person(name, age, location):
#     person = {
#         'name': name,
#         'age': age,
#         'location': location
#     }
#
#     return  person


# def numbers_addition(num1, num2):
#     return num1 + num2
#
#
# print(numbers_addition(4, 8))

