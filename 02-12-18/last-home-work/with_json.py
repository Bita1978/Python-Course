import json

p1, p2 = {
    'name': input('Enter your name\n'),
    'age': int(input('Enter your age\n')),
    'location': {
        'country': input('Enter your country\n'),
        'city': input('Enter your city\n'),
        'street': input('Enter your street\n'),
        'number': int(input('Enter your number\n'))
    }
}, {
    'name': input('Enter your name\n'),
    'age': int(input('Enter your age\n')),
    'location': {
        'country': input('Enter your country\n'),
        'city': input('Enter your city\n'),
        'street': input('Enter your street\n'),
        'number': int(input('Enter your number\n')),
    }
}

p1_file = 'p1_json_file.txt'
p2_file = 'p2_json_file.txt'

with open(p1_file, mode='w') as my_file:
    my_file.write(json.dumps(p1))

with open(p2_file, mode='w') as my_file:
    my_file.write(json.dumps(p2))

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

with open(p1_file, mode='r') as my_file:
    p1 = json.loads(my_file.read())


with open(p2_file, mode='r') as my_file:
    p2 = json.loads(my_file.read())


p3['friends'] = [p1, p2]

print(p1['name'])
