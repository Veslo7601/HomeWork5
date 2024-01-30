"""Module providing a function """

from collections import UserDict

class Field:
    """Class representing a default class"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Class representing a Name"""

class Phone(Field):
    """Class representing a Phone"""

    def __init__(self, value):

        if len(str(value)) != 10:
            raise ValueError ("Номер не має 10 цифр")
        elif not value.isdigit():
            raise ValueError ("У номері є зайві символи ")
        else:
            self.value  = value

class Record:
    """Class representing a Record"""

    def __init__(self, name):

        self.name = Name(name)
        self.phones = []

    def add_phone(self,value):
        """function for adding phones"""

        self.phones.append(Phone(value))

    def remove_phone(self,value):
        """function for remove phones"""

        if self.find_phone(value):
            self.phones.remove(self.find_phone(value))

    def edit_phone(self,value,value_two):
        """function for edit phones"""

        if self.find_phone(value):
            self.remove_phone(value)
            self.add_phone(value_two)
        else:
            raise ValueError("Номер не існує")

    def find_phone(self,value):
        """function for find phones"""

        for phone in self.phones:
            if str(phone) == str(value):
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """Class representing a AddressBook"""

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def add_record(self,Record):
        """function for add record"""

        return super().__setitem__(Record.name.value,Record)

    def find(self,Name):
        """function for find record"""

        for key in self.data:
            if str(key) == str(Name):
                return super().__getitem__(key)

    def delete(self,Name):
        """function for delete record"""

        for key in self.data:
            if str(key) == str(Name):
                return super().__delitem__(key)
#The file ends
