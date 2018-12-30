"""
Third Task
"""

# Initial Persons
persons = [{'name': input('Enter your name\n'),
            'age': int(input('Enter your age\n'))}
           for i in range(3)]


# Lazy Initial
persons = [{'name': 'Ed', 'age': 43}, {'name': 'Evyatar', 'age': 23}, {'name': 'Yaara', 'age': 12}]

# Printing only persons with age greater than 18
for p in persons:
    if p['age'] <= 18:
        continue

    print(p['age'])


# If one of the name's length > 5 break
counter = 0

for p in persons:
    if len(p['name']) > 5:
        break
    print(counter)
    counter += 1

# Printing every letter of every name
for p in persons:
    for letter in p['name']:
        print(letter)


# Increase age + 12 if name's length smaller than 3 characters
for p in persons:
    if len(p['name']) < 3:
        p['age'] += 12


print(persons)
