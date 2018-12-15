import re

"""
First Task
"""

# Initial Persons
persons_list = []

for index in range(1, 4):

    print(f"Person number {index}:")

    person = {
        'name': input('Enter your name\n'),
        'age': int(input('Enter your age\n'))
    }
    persons_list.append(person)


# 1)
for person in persons_list:
    if person['age'] < 27:
        person['name'] = 'Jimmy Hendrix'

print(persons_list)

# 2)
for person in persons_list:
    if 't' in person['name'].lower():
        person['age'] += 1
        print(f"""Happy bday {person['name']}
Your are {person['age']} years old.""")

# 3)
counter = 0

while counter < persons_list[1]['age']:
    if counter % 2 == 0:
        print(counter)
    counter += 1

# 4)
e_letter = 'e'

for person in persons_list:
    if e_letter in person['name'].lower():
        if person['name'][0] == e_letter:
            print(f"{e_letter} in index 0")
        elif person['name'][1] == e_letter:
            print(f"{e_letter} in index 1")
        else:
            print(f"{e_letter} in index {person['name'].find(e_letter)}")

"""
Second Task
"""

# Initial Time
time = int(input('Enter time in minutes'))

hours = int(time / 60)
minutes = time - (hours * 60)

# 1)
if hours >= 1:
    if hours < 2:
        print("Ok...")
    else:
        print("Trilogy")

# 2)
if minutes > hours:
    if minutes % 2 == 0:
        hours *= 2
    else:
        minutes -= 1
else:
    print(hours)

print(f"Hours: {hours}, Minutes: {minutes}")

"""
Third Task
"""

# Creating the file

file_content = """
My my candle candle burns at both ends;
It will not last the night;
But ah, my foes, and oh, my friends—
It gives a lovely light!
"""

file_path = "file.txt"

with open(file_path, mode='w') as my_file:
    my_file.write(file_content)

# Reading the file

with open(file_path, mode='r') as my_file:
    reading_content = my_file.read()

# 1)
all_words = reading_content.split()

# 2)
all_words_set = set({})

for word in all_words:
    word = re.sub(r"[^A-Za-z]+", "", word)
    all_words_set.add(word.lower())

# 3)
for word in all_words_set:
    if word.startswith('t'):
        print(f"Word ({word}) starts with 't'")

# 4)
for word in all_words_set:
    if word.startswith('a'):
        print(f"Word: {word}")
        print("Letters:")
        for letter in word:
            print(letter)

# 5) Short way
words_tuple = tuple(word for word in all_words if 'a' not in word)
print(words_tuple)

# 5) Long way
to_be_tuple = []
for word in all_words:
    if 'a' not in word:
        to_be_tuple.append(word)

to_be_tuple = tuple(to_be_tuple)
print(to_be_tuple)

# 6) Short way
new_e_words = [e_word.replace('e', '3') for e_word in all_words_set if 'e' in e_word]
print(new_e_words)

# 6) Long way
e_to_3 = []

for word in all_words_set:
    if 'e' in word:
        new_word = word.replace('e', '3')
        e_to_3.append(new_word)

print(e_to_3)

