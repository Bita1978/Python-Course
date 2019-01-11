"""
##########
# Task 1 #
##########
"""


class Person:
    """
    This class makes a definition for Person object
    __init__ method takes a 3 arguments:
    Name, Age & Hobby
    Initial Person's attributes ( self attributes )
    If Age illegal ( age < 1 or age > 120 )
    Age will set up to 0 And Message will pop out to the console
    """

    def __init__(self, name, age, hobby):
        """
        Constructor - Initial parameters
        If Age illegal, age will set up to 0
        :param name: str
        :param age: int
        :param hobby: str
        """
        self.name = name
        self.hobby = hobby

        if age < 1 or age > 120:
            print(f'Age is illegal: {age}, it will set to 0')
            self.age = 0
            return
        self.age = age

    def print_person(self):
        """
        This method print to the console
        The details of the specific instance
        Who invoked this method
        *Notice: using str.format in order to multiple text
        *Using \n in order to break line,
        *Using \t in order to move 1 tab forward
        :return: None
        """
        print('{line}Person{line}'.format(line=('-' * 5)))
        print('-' * 16)

        for key, value in {
            'name': self.name,
            'age': self.age,
            'hobby': self.hobby
        }.items():
            print(f"| {key}: {value}")

        print('-' * 16)

    def __str__(self):
        """
        __str__ ( Known as to string )
        Overrides method that return string representation
        Of this specific instance
        :return: str that describes this person ( self )
        """
        return f"Person [\n\tname: {self.name}\n\tage: {self.age}\n\thobby:{self.hobby}\n]"


# person1 = Person('Yaniv', 20, 'cooking')
# person1.print_person()
# print(person1)


"""
##########
# Task 2 #
##########
"""


class Customer:
    """
    This class makes a definition for customer,
    Customer contains name & age attributes
    """

    def __init__(self, name, age):
        """
        Init method - initial customer's attributes
        :param name: str
        :param age: int
        """
        self.name = name
        self.age = age


class DisneyLand:
    """
    This class makes a definition for a disneyland
    This class holds only one method - roller coaster
    """

    # self.legal_age - class attribute
    legal_age = 18

    def roller_coaster(self, customer):
        """
        This method takes a customer argument,
        Validates it is a type customer,
        Then validates the age is legal ( 18+ )
        Finally loops over the roller coaster
        Prints to the console:
        Loop iteration number & person's age
        :param customer: Customer
        :return: None
        """
        if type(customer) is not Customer:
            print("This method handles customers only")
            return
        if customer.age < self.legal_age:
            print(f"Sorry {customer.name}, you are still young for this device.")
            print(f"Your age is {customer.age}, legal age is {self.legal_age}")
        else:
            for i in range(1, 6):
                print(f"Get ready {customer.name} this is the {i} round!")


# customer = Customer('Maor', 60)
# disney_land = DisneyLand();
# disney_land.roller_coaster(customer)


"""
##########
# Task 3 #
##########
"""


class Dog:
    """
    This class makes a definition for a dog object
    """

    def __init__(self, name, age):
        """
        __init__ method - initial dog's attributes
        Validate dog's age is a number,
        In order to multiple it later.
        :param name: str
        :param age: int / float
        """
        self.name = name
        if (type(age) is not int) and (type(age) is not float):
            print(f"Age is illegal {age}\nAge will set up to 0")
            self.age = 0
            return
        self.age = age

    def get_my_human_age(self):
        """
        This method return the age of this instance * 7
        :return: self.age * 7
        """
        return self.age * 7

    def __str__(self):
        """
        __str__ method
        *Using \ in order to write str with more than one line
        *Using \t in order to move 1 tab forward
        :return: String representation of this object's values.
        """
        return f"Dog [\n\tname: {self.name}" \
               f"\n\tage: {self.age}" \
               f"\n\thuman age: {self.get_my_human_age()}" \
               f"\n]"


# dog = Dog("Cashew", 4)
# dog.name = "Einstein"
# print(dog)
# human_age = dog.get_my_human_age()
# print(human_age)