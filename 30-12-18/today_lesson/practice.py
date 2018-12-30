
def age_calc(name, birth_year):
    """
    Calculate the age by year of birth
    :param name:
    :param birth_year:
    :return: age
    """
    age = 2018 - birth_year
    print(f"Hello {name} your age is {age}")
    return age


age = age_calc("Enosh", 1989)


def key_n_value(**kwargs):
    """
    Prints value if int
    calculates sum if there is more than one int
    """
    optional = []
    for item in kwargs.values():
        if type(item) is int:
            optional.append(item)
            print(item)

    if len(optional) > 0:
        return sum(optional)
    else:
        return 0


a = key_n_value(a=1, b=4 ,shalom="Yaniv")

print(f"a is {a}")
