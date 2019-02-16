class Book:

    def __init__(self, name, author ,id=None):
        self.__name = name
        self.__author = author
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def name(self, new_id):
        if not new_id:
            return
        else:
            self.__id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name:
            return
        else:
            self.__name = new_name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        if not new_author:
            return
        else:
            self.__author = new_author

    def __str__(self):
        return f"Book: (ID: {self.id}, Name: {self.name}, Author: {self.author})"