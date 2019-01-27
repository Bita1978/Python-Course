class Entity:

    def __init__(self, name, health, xp):
        self.name = name
        self.health = health
        self.xp = xp

    def speak(self):
        print(f"Hi i'm {self.name}\nmy health is {self.health}\nmy xp: {self.xp}")


class Player(Entity):

    def __init__(self, name):
        super().__init__( name=name, health=100, xp=0)

    def who_am_i(self):
        return self.__class__.__name__


player = Player(name="Avner")
print(player.who_am_i())