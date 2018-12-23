
"""
How to create a collection using operators inside
"""

my_str = 'Hello world'

str_list = []

for letter in my_str:
    str_list.append(letter)

print(str_list)

str_list = [x for x in my_str]
print(str_list)

my_list = list(range(1,11))
print(my_list)

my_list = [num for num in range(10)]
print(my_list)

my_list = [num * 2 for num in range(1, 11)]
print(my_list)

my_list = [num for num in range(1, 11) if num % 2 == 0]
print(my_list)


"""
Useful operators
"""
my_str = 'Hi there im using what\'s app'

for letter in enumerate(my_str):
    print(letter)

my_list = [0, 3, 'hi', True]

for element in enumerate(my_list):
    print(element)

my_list1 = list(range(1,4))
my_list2 = ['a', 'b', 'c', 'g', 'h']
my_list3 = [True, True, True]

for element in zip(my_list1, my_list2, my_list3):
    print(element)

for x, y, z in zip(my_list1, my_list2, my_list3):
    print(x)
    print(y)
    print(z)
    print("-------")

combine = list(zip(my_list1, my_list2, my_list3))
print(combine)

"""
Break & Continue
"""

members = ['Itsik', 'Iftach', 'Efrat', 'Adi']

for member in members:
    if 'f' in member.lower():
        break
    print(member)

for index in range(0, 11):
    if index == 6:
        break
    print(index)

for member in members:
    if 'f' in member.lower():
        continue
    print(member)
