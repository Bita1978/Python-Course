class SimplePerson:

    name = 'Avner'

    def print_hello(self):
        print(f'Hello {self.name}')


person = SimplePerson()
# person.print_hello()


class PersonConstructor:

    def __init__(self):
        self.name = 'Avner'

    def print_hello(self):
        print(f"Hello {self.name}")


person = PersonConstructor()
# print(person.name)
# person.print_hello()


class PersonInitial:

    def __init__(self, outside_name):
        self.inside_name = outside_name

    def print_hello(self):
        print(f'Hello {self.inside_name}')


person1 = PersonInitial('Efrat')
person2 = PersonInitial('Itay')

# person1.print_hello()
# person2.print_hello()
# print(person1)


class PersonToString:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Person - [name: {self.name}]'


person = PersonToString(name='Itay')
# print(person)


class PersonLength:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person - [name: {self.name}, age: {self.age}]'

    def __len__(self):
        return self.age


person = PersonLength(name="Avner", age=34)
# print(person)
# print(len(person))


class PersonOverLoad:

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'


p1 = PersonOverLoad()
p2 = PersonOverLoad("Itay")
p3 = PersonOverLoad('Efrat', 32)

# print(p1)
# print(p2)
# print(p3)


class PersonAccess:

    def __init__(self):
        self.public = 'I\'m public!'
        self.__name = 'Avner'


person = PersonAccess()
# print(person.public)
# print(person.__name)


class PersonGetter:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


person = PersonGetter(name="Itay")
person_name = person.get_name()
# print(person_name)


class PersonGettersSetters:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f'Person - name: {self.get_name()}'


person = PersonGettersSetters(name="Enosh")
# print(person)
person.set_name("Itay")
# print(person.get_name())
# print(person)


class Person:

    def __init__(self, name, age):
        self.__name = name.title()
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            print(f'Name is empty {name}')
            return
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0 or age > 120:
            print(f'Age illegal -> {age}')
            return
        self.__age = age

    def __str__(self):
        return f'Person - [name: {self.name}, age: {self.age}]'


a = Person(name="itay", age=28)
print(a)
print(a.name)
print(a.age)
a.name = ''
a.name = 'Efrat'
print(a.name)
print(a)
a.age = 990
a.age = -90
a.age = 32
print(a)