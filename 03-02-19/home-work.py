import logging
"""
Logger !!!
"""
# set up logging to file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# add the handler to the root logger
logging.getLogger('').addHandler(console)


"""
First Task !!!
"""


class Phone:
    """
    Phone Class
    """

    def __init__(self, memory, memory_operation):
        self.memory = memory
        self.__memory_operation = memory_operation
        self.__contacts = []

    @property
    def memory_operation(self):
        return self.__memory_operation

    @property
    def contacts(self):
        return self.__contacts

    def add_to_contact(self, contact):

        if contact in self.contacts:
            logging.warning(f"{contact} already exists")

        elif self.memory < self.memory_operation:
            logging.error(f"{self.__class__.__name__}: Not enough memory!, Memory: {self.memory}")

        else:
            self.contacts.append(contact)
            self.memory -= self.memory_operation
            logging.info(f"{self.__class__.__name__}: {contact} added successfully , Memory: {self.memory}")

    def add_many_contacts(self, *args):
        for contact in args:
            self.add_to_contact(contact)

    def remove_from_contacts(self, contact):
        if contact not in self.contacts:
            logging.warning(f"{self.__class__.__name__}: {contact} does not exists")
        else:
            self.contacts.remove(contact)
            self.memory += self.memory_operation
            logging.info(f"{self.__class__.__name__}: {contact} removed successfully , Memory: {self.memory}")

    def remove_many_contacts(self, *args):
        for contact in args:
            self.remove_from_contacts(contact)

    def print_contacts(self):
        for c in self.contacts:
            print(c)

    def __str__(self):
        return f"IPhone (\n\tmemory: {self.memory}\n\tcontact: {self.contacts}\n)"


class IPhone(Phone):
    """
    IPhone class
    """
    def __init__(self):
        super().__init__(memory=150, memory_operation=35)


class Android(Phone):
    """
    Android class
    """
    def __init__(self):
        super().__init__(memory=200, memory_operation=20)


p1 = {'Enosh', '0525758999'}
p2 = {'Itay', '0529778319'}
p3 = {'Ehud', '0523748198'}
p4 = {'Sivan', '0544251900'}
p5 = {'Kobi', '0523054131'}


# iphone = IPhone()
# iphone.add_many_contacts(p1, p2, p3, p4)
# iphone.remove_many_contacts(p5, p3)
#
# android = Android()
# android.add_many_contacts(p1, p2, p3, p4)
# android.remove_many_contacts(p5, p3)

"""
Second Task
"""


class Bank:
    """
    Bank class
    """

    money = 0

    def __init__(self, fee):
        self.__fee = fee

    @property
    def fee(self):
        return self.__fee

    def withdraw(self, money_amount):
        if self.money <= (money_amount + self.fee):
            logging.error(f"{self.__class__.__name__}: Not enough money in the bank: {self.money}")
        else:
            self.money -= (money_amount + self.fee)
            logging.info(f"{self.__class__.__name__} withdraw operation succeeded, Money: {self.money}")
            return money_amount

    def deposit(self, money_amount):
        self.money += (money_amount - self.fee)
        logging.info(f"{self.__class__.__name__} deposit operation succeeded, Mony: {self.money}")


class GoldBank(Bank):

    def __init__(self):
        super().__init__(fee=2.90)


class SilverBank(Bank):

    def __init__(self):
        super().__init__(fee=4.90)


class BronzeBank(Bank):

    def __init__(self):
        super().__init__(fee=6.90)


gold = GoldBank()
silver = SilverBank()
bronze = BronzeBank()

gold.deposit(100)
silver.deposit(100)
bronze.deposit(100)

gold.withdraw(96)
silver.withdraw(95)
bronze.withdraw(93)

money = gold.withdraw(50)
print(money)
