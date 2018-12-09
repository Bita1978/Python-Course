num1 = int(input('num1\n'))
num2 = int(input('num2\n'))

if num1 > num2:
    print('num1 is greater than num2')
    if num1 > 5:
        print('num1 is greater than 5')
elif num2 != 3:
    print('num2 != 3')
elif num2 == 3:
    print('num2 must be 3')
else:
    print('how did i got here?')

str1 = input('some text')
str1 = str1.lower()

print(str1)

if 'a' in str1:
    print('nice!')

my_list = [3, 's', 7]

if 3 in my_list:
    print('yay!')

person = {
    'name': input('Enter your name'),
    'age': int(input('Enter your age'))
}


if 'a' in person['name'].lower():
    person['name'] = 'itay'

if person['age'] < 17:
    print(f"You can't drive {person['name']}")

print(person['name'])




