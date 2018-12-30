"""
Fourth Task
"""


# All functions
def addition(num1, num2):
    print(num1 + num2)


def subtract(num1, num2):
    print(num1 - num2)


def subdivision(num1, num2):
    if num2 == 0:
        print('You can not divide by 0')
    else:
        print(num1 / num2)


def multiple(num1, num2):
    print(num1 * num2)


operators = ['+', '-', '/', '*']


# Calculator by operators
def calc(num1, num2, operator):
    while operator not in operators:
        operator = input('Please choose a valid operator [+, -, /, *]\n')

    if operator == '+':
        addition(num1, num2)
    elif operator == '-':
        subtract(num1, num2)
    elif operator == '*':
        multiple(num1, num2)
    elif operator == '/':
        subdivision(num1, num2)


calc(3, 7, '?')

