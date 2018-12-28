"""
First Task Only!
"""

# Initial list inside a loop
users_list = []

for index in range(1, 11):
    user = input('Please enter your name\n')
    users_list.append(user)


print(users_list)

# Lazy Initial
users_list = ['Enosh', 'Lior', 'Dany', 'Maor', 'Ofer', 'Ori', 'Roy', 'Dorin', 'Ran', 'Yaniv']

# Creating even & odd lists
even_list = []
odd_list = []

for index, value in enumerate(users_list):
    if index % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)

# Even from the even_list
for index, value in enumerate(even_list):
    if index > 4:
        print(value)


# Even from the users_list
for index, value in enumerate(users_list):
    if index % 2 == 0 and index > 4:
        print(value)


# Odd from the odd_list
for index, value in enumerate(odd_list):
    if index != 1 and index != 5:
        print(value)


# Odd from users_list
for index, value in enumerate(users_list):
    if index % 2 != 0 and (1 != index != 5):
        print(value)

# Create a new list of both (even and odd)
final_list = []

for index, value in enumerate(users_list):
    if (index % 2 != 0 and (1 != index != 5)) or (index % 2 == 0 and index > 4):
        final_list.append(value)












