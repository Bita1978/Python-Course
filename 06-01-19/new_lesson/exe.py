
class Person:

    def __init__(self, name):
        self.name = name

    def print_hello(self):
        print(f"hi {self.inside_name}")

    def __str__(self):
        return f'Person: [name={self.name}]'


p1 = Person('Itay')
print(p1)

# p3 = p2

