# 1)
# Initial list
input_msg = 'Please enter any number\n'
num_list = [int(input(input_msg)), int(input(input_msg)), int(input(input_msg))]

# Conditions
print(f"""1)
values: {num_list[0]} > {num_list[1]}
result: {num_list[0] > num_list[1]}""")

print(f"""2)
values: {num_list[0]} > {num_list[1]} or {num_list[0]} > {num_list[2]}
result: {num_list[0] > num_list[1] or num_list[0] > num_list[2]}
""")

print(f"""3)
values: {num_list[0]} != {num_list[1]} != {num_list[2]}
result: {num_list[0] != num_list[1] != num_list[2]}
""")

print(f"""4)
values: {sum(num_list)} > {len(num_list) * 3}
result: {sum(num_list) > (len(num_list) * 3)}
""")

# 2)
# Initial Strings
input_msg2 = 'Please enter some text'
str1 = input(input_msg2)
str2 = input(input_msg2)

# Conditions
print(f"""1)
values: {len(str1)} > {len(str2)}
result: {len(str1) > len(str2)}
""")

print(f"""2)
values: {str1}.startswith('t') or {str2}.startswith('t')
result: {str1.startswith('t') or str2.startswith('t')}
""")

print(f"""3)
values: not ({str1}.islower() and {str2}.islower())
result: {not (str1.islower() and str2.islower())}""")

print(f"""4)
values: ({len(str1)} < {len(str2)}) and ({str1}.startswith('t') or {str1}.startswith('w'))
result: {(len(str1) < len(str2)) and (str1.startswith('t') or str1.startswith('w'))}
""")

# 3)
# Creating a file
file_name = 'file.txt'

file_content = """What do computers and
Air conditioners have in common?

They both become useless
When you open windows"""

with open(file_name, mode='w') as my_file:
    my_file.write(file_content)

# Reading the file
with open(file_name, mode='r') as my_file:
    read_content = my_file.read()


# Conditions
print(f"""1)
values: {len(read_content)} >= 20
result: {len(read_content) >= 20}
""")

print(f"""2)
values: read_content.islower()
result: {read_content.islower()}
""")

all_words = read_content.split()
print(f"""3)
values: any(item.startswith('t') for item in all_words)
result: {any(item.startswith('t') for item in all_words)}
""")

with_word = [item for item in all_words if item.startswith('a')]

print(f"""4)
values: {len(with_word)} > 0 and {len(with_word[0])} >= 3
result: {len(with_word) > 0 and len(with_word[0]) >= 3}
""")


"""
Another way..
"""
# 3) 3)
for word in all_words:
    if word.startswith('t'):
        condition = True
        break
    condition = False

print("""3)
values: for word in all_words:
            if word.startswith('t'):
                condition = True
            break
            condition = False
result: {}
""".format(condition))

# 3) 4)
for word in all_words:
    if word.startswith('a'):

        condition = len(word) >= 3
        break
    condition = False

print("""3)
values: for word in all_words:
            if word.startswith('a'):
                condition = len(word) >= 3
            break
            condition = False
result: {}
""".format(condition))



