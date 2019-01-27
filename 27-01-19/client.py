class Client:

    def __init__(self, name, discount, money):
        self.name = name
        self.discount = discount
        self.money = money

    def print_details(self):
        print(f"{self.__class__.__name__} - \n"
              f"Name: {self.name}\n"
              f"Discount:{self.discount}\n"
              f"Money: {self.money}")


class Premium(Client):

    def __init__(self, name):
        super().__init__(name=name, discount="20%", money=2000)


class Gold(Client):

    def __init__(self, name):
        super().__init__(name=name, discount="50%", money=5000)


class Bronze(Client):

    def __init__(self, name, smiley):
        super().__init__(name=name, discount="1%", money=100)
        self.smily = smiley

    def print_details(self):
        print(f"{self.__class__.__name__}: It's not my day... {self.smily}")


premium = Premium("Yoav")
gold = Gold("Avner")
bronze = Bronze("Koko", ":(")

for client in (premium, gold,bronze):
    client.print_details()