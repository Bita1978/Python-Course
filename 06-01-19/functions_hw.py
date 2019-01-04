


def three_arguments(num1, num2, num3):
    """
    Arguments must be numbers
    Checks how many times digit 30 appears in arguments
    And if not, checks if sum of the arguments equals to 30
    :param num1:
    :param num2:
    :param num3:
    :return:None
    """
    numbers = [num1, num2, num3]
    if 30 in numbers and numbers.count(30) == 1:
        print('30')
    elif 30 in numbers and numbers.count(30) > 1:
        numbers_30 = [num for num in numbers if num == 30]
        print(f"Number 30 appears {len(numbers_30)} times")
        print(f"Sum of All: {sum(numbers_30)}")

    if 30 not in numbers:
        if num1 + num2 == 30:
            print(f"{num1} + {num2} = {num1 + num2}")
        elif num1 + num3 == 30:
            print(f"{num1} + {num3} = {num1 + num3}")
        elif num2 + num3 == 30:
            print(f"{num2} + {num3} = {num2 + num3}")
        elif num1 + num2 + num3 == 30:
            print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")


# three_arguments(10, 5, 15)


def infinite_variables(*args):
    """
    Takes infinite number of variables
    Create a person as a dictionary that contains:
    Age - int, Name - str, Story - str
    :param args:
    :return: Dictionary ( person )
    """
    person = {'age': 0, 'name': '', 'story': ''}
    for element in args:
        if type(element) is int:
            person['age'] += element
        elif type(element) is str:
            if element[0].isupper():
                person['name'] += f"{element} "
            elif element[0].islower():
                person['story'] += f"{element} "

    return person


# my_person = infinite_variables(4, 5, 22, 'Yaniv', 'likes', 'computers', 'and stuff', 1, 'Grizzly')
# print(my_person)


def key_value(**kwargs):
    """
    Takes key & value arguments
    Loops over the arguments while index less than 4
    Checks key & values and prints to the console,
    If some condition is true
    :param kwargs:
    :return:
    """
    for index, (key, value) in enumerate(kwargs.items()):
        if index > 4:
            break
        if 'b' in key.lower() and 'e' in key.lower():
            print(f"b and e in {key.lower()} index * 2 = {index * 2}")
        elif 'b' in key.lower():
            print(f"b in index{index}")

        if type(value) is str:
            if 't' in value.lower():
                print('t' * 3)
        elif type(value) is int:
            print(value * 3)


# key_value(a=9, boeb=90, c=87, d=45, eduard='t', f=21, h=76)
