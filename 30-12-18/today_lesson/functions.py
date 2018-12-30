
def my_func():
    print('This is my function')


my_func()


def my_func2():
    """
    This is a function with documentation
    """
    print('This is also a function')


my_func2()

print(help(my_func2))


def say_hallo_to(name):
    """This is a greeting function"""
    print(f'Hi there {name} ')


def say_hello_with_default( name='Harry Potter'):
    """Default argument's value"""
    print(f'Hi there {name}')


def two_arguments(num1, num2):
    """
    Important arguments must be a numbers
    Print the sum of the two arguments
    """
    print(num1 + num2)


two_arguments(3, 4)


def return_value(num1, num2):
    return num1 + num2


my_sum = return_value(4, 5)
print(my_sum)


def calling_another_function(num1, num2, num3):
    """
    Function that calls to another function
    :param num1: must be an int
    :param num2: must be an int
    :param num3: must be an int
    :return: sum of (num1 , num2) + num3
    """
    sum_of_two = return_value(num1, num2)
    another_addition = return_value(sum_of_two, num3)
    return another_addition


print(calling_another_function(3, 7, 10))


def get_many_args(*args):
    for item in args:
        print(item)


get_many_args(1, 2, 4, 6, 6, 3, 2)


def args_with_keys(**kwargs):
    for item in kwargs.items():
        print(item)


args_with_keys(one=1, two=2, three=3)



