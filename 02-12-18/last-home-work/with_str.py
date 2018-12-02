# p1, p2 = {
#     'name': input('Enter your name\n'),
#     'age': int(input('Enter your age\n')),
#     'location': {
#         'country': input('Enter your country\n'),
#         'city': input('Enter your city\n'),
#         'street': input('Enter your street\n'),
#         'number': int(input('Enter your number\n'))
#     }
# }, {
#     'name': input('Enter your name\n'),
#     'age': int(input('Enter your age\n')),
#     'location': {
#         'country': input('Enter your country\n'),
#         'city': input('Enter your city\n'),
#         'street': input('Enter your street\n'),
#         'number': int(input('Enter your number\n')),
#     }
# }
#
p1_file = 'p1_file.txt'
p2_file = 'p2_file.txt'
#
# with open(p1_file, mode='w') as my_file:
#
#     details = f"""name {p1['name']}
# age {p1['age']}
# country {p1['location']['country']}
# city {p1['location']['city']}
# street {p1['location']['street']}
# number {p1['location']['number']}
# """
#     my_file.write(details)
#
# with open(p2_file, mode='w') as my_file:
#
#     details = f"""name {p2['name']}
# age {p2['age']}
# country {p2['location']['country']}
# city {p2['location']['city']}
# street {p2['location']['street']}
# number {p2['location']['number']}
# """
#     my_file.write(details)
#

p3 = {
    'name': input('Enter your name\n'),
    'age': int(input('Enter your age\n')),
    'location': {
        'country': input('Enter your country\n'),
        'city': input('Enter your city\n'),
        'street': input('Enter your street\n'),
        'number': int(input('Enter your number\n'))
    }
}

p1, p2 = {}, {}

with open(p1_file,mode='r') as my_file:
    content = my_file.readlines()

    name_list = content[0].splitlines()
    name = name_list[0].split()
    p1[f'{name[0]}'] = name[1]

    age_list = content[1].splitlines()
    age = age_list[0].split()
    p1[f'{age[0]}'] = age[1]

    country_list = content[2].splitlines()
    country = country_list[0].split()
    p1['location'] = {}
    p1['location'][f'{country[0]}'] = country[1]

    city_list = content[3].splitlines()
    city = city_list[0].split()
    p1['location'][f'{city[0]}'] = city[1]

    street_list = content[4].splitlines()
    street = street_list[0].split()
    p1['location'][f'{street[0]}'] = street[1]

    number_list = content[5].splitlines()
    number = number_list[0].split()
    p1['location'][f'{number[0]}'] = number[1]

with open(p2_file, mode='r') as my_file:
    content = my_file.readlines()

    name_list = content[0].splitlines()
    name = name_list[0].split()
    p2[f'{name[0]}'] = name[1]

    age_list = content[1].splitlines()
    age = age_list[0].split()
    p2[f'{age[0]}'] = age[1]

    country_list = content[2].splitlines()
    country = country_list[0].split()
    p2['location'] = {}
    p2['location'][f'{country[0]}'] = country[1]

    city_list = content[3].splitlines()
    city = city_list[0].split()
    p2['location'][f'{city[0]}'] = city[1]

    street_list = content[4].splitlines()
    street = street_list[0].split()
    p2['location'][f'{street[0]}'] = street[1]

    number_list = content[5].splitlines()
    number = number_list[0].split()
    p2['location'][f'{number[0]}'] = number[1]


p3['friends'] = [p1, p2]


print(p3)
