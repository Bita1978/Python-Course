counter = 0

while counter <= 5:
    print(f'Iteration number {counter}')
    counter = counter + 1

name = ''

while name.lower() != 'avner':
    name = input('Enter your name, should be avner')

print('finally you are avner')

my_bool = True

while my_bool:
    num1 = int(input('Enter a number'))
    num2 = int(input('Enter a number'))

    if (num1 + num2) > 6:
        my_bool = False

    print('-------------------')

print('I have exit the loop')


counter = 0
my_bool = True

while (counter < 5) and (my_bool):
    print(counter)

    counter += 1
    if counter == 3:
        my_bool = False


content = 'abcdefg'

for letter in content:
    print(letter)

my_list = [2, 5, 'hi' , True]

for element in my_list:

    print(type(element))

    if type(element) is str:
        element = element.upper()

    if type(element) is int:
        element += 100

    if type(element) is bool:
        element = not element

    print(element)


my_list = ['Efrat', 'Avner', 'Itay']

for name in my_list:
    if name == 'Avner':
        print(name)


for x in range(10):
    print(x)


for x in range(1, 11):
    print(x)


for x in range(1, 12, 2):
    print(x)
