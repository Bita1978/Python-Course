"""
Second Task
"""

# Long way...

name_list = []
pwd_list = []

# Initial name & pwd inside a loop
for index in range(4):
    name = input('Please enter your name\n')
    name_list.append(name)

    pwd = input('Please enter your password\n')
    pwd_list.append(pwd)


print(f"{name_list}\n{pwd_list}")

# Short way
name_list = [input('Enter your name\n') for x in range(4)]
pwd_list = [input('Enter your password\n') for x in range(4)]


# # Lazy Initial
name_list = ['johnathan', 'Sam', 'Bruce']
pwd_list = ['1234', '123#', 'BruceWayne#12']
pwd_winners = {}
#
different_keys = ['~', '`', '!', '@', '$', '%', '^', '&',
                  '*', '(', ')', '_', '-', '+', '=', '|', '\\',
                  '[', '{', ']', '}', ';', ':', "'", '"', '/',
                  '>', '<', ',', '.', '?', '#']
#
# # Longest
longest_len = 0
longest_str = ''
longest_list = []
equal_to_longest = []
#
# # Get the longest string
for index, pwd in enumerate(pwd_list):
    # Saving longest string base on iterations
    if len(pwd) > longest_len:
        longest_len = len(pwd)
        longest_str = pwd
    # Handling two equals longest strings
    elif len(pwd) == longest_len:
        equal_to_longest.append(pwd)

    # Appending on last iteration
    if index == len(pwd_list) - 1:
        longest_list.append(longest_str)
        if len(equal_to_longest) > 0:
            for password in equal_to_longest:
                if len(password) >= longest_len:
                    longest_list.append(password)
#
# # Adding winning points to the longest winners
for longest in longest_list:
    pwd_winners[f"{longest}"] = 1
#
#
# # Validate upper and lower case
upper = False
lower = False
#
for pwd in pwd_list:
    # Checking every letter if its lower or upper case
    for letter in pwd: # AbcD
        if letter.islower():
            lower = True
        else:
            upper = True

    # in case we got both lower and upper
    if upper and lower:
        if pwd not in pwd_winners.keys():
            pwd_winners[f"{pwd}"] = 1
        else:
            pwd_winners[f"{pwd}"] = pwd_winners[f"{pwd}"] + 1
#
#
# # Checking characters that are not letters
for pwd in pwd_list:
    onlyLetters = True

    for letter in pwd:
        if letter in different_keys:
            onlyLetters = False
            break
    # in case there are any different characters
    if not onlyLetters:
        if pwd not in pwd_winners.keys():
            pwd_winners[f"{pwd}"] = 1
        else:
            pwd_winners[f"{pwd}"] = pwd_winners[f"{pwd}"] + 1
#
#
# Reveal the winner ( or winners with the same results )
winners = []
second_winners = {}
best_score = 0
counter = 0
#
#
for key, value in pwd_winners.items():

    # Getting best score base on iteration
    if value > best_score:
        best_score = value
        winner1 = {key: value}
    # Handling two winners with the same results
    elif value == best_score:
        second_winners[key] = value

    counter += 1
    # Last iteration collect all winners
    if counter == len(pwd_winners):
        winners.append(winner1)
        if len(second_winners) > 0:
            for k, v in second_winners.items():
                if v >= best_score:
                    winners.append({k: v})


print(f"The winners: {winners}")

# Get all weak passwords
weak_list = [pwd for pwd in pwd_list if pwd not in pwd_winners]
# Initial weak password with a temporary value
weak_pwd = '12345678'

weak_list_points = 0
weak_pwd_points = 0

counter = 0

while counter < len(weak_list):
    # Checking smallest length & initial weak_pwd
    if len(weak_list[counter]) < len(weak_pwd):
        weak_pwd = weak_list[counter]
    # In case same length, checking different characters
    elif len(weak_pwd) == weak_list[counter]:
        for letter in weak_list[counter]:
            if letter in different_keys:
                weak_list_points += 1
        for letter in weak_pwd:
            if letter in different_keys:
                weak_pwd_points += 1

    if weak_list_points < weak_pwd_points:
        weak_pwd = weak_list[counter]

    # increase counter
    counter += 1

# Print the weakest password
print(weak_pwd)

# Printing user name if his name longer than his password
for name, pwd in zip(name_list, pwd_list):
    if len(name) > len(pwd):
        print(name)

# Printing password if one of its character appears in the user name
for name, pwd in zip(name_list, pwd_list):

    is_show = False

    for letter in name:
        if letter in pwd:
            is_show = True
            break
    if is_show:
        print(pwd)








