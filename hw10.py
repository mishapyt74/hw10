from collections import UserDict


class Record:
    def __init__(self, name: str, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("1234567890")
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    print(ab)