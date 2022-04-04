"""
Design a class that holds the following personal data: name, address, age, and phone number. Write appropriate
 accessor and mutator methods (get and set). Write a program that creates three instances of the class. One
 instance should hold your information and the other two should hold your friends' or family members' information.
  Just add information, don't get it from the user.  Print the data from each object, make sure to format the
  output for clarity and ease of reading.
"""


class Person:

    def __init__(self, name, address, age, phone):
        self.in_name = name
        self.in_address = address
        self.in_age = age
        self.in_phone = phone

    def set_name(self, name):
        self.in_name = name

    def set_address(self, address):
        self.in_address = address

    def set_age(self, age):
        self.in_age = age

    def set_phone(self, phone):
        self.in_phone = phone

    def get_name(self):
        return self.in_name

    def get_address(self):
        return self.in_address

    def get_age(self):
        return self.in_age

    def get_phone(self):
        return self.in_phone

    def __str__(self):
        print('name: ', str(self.get_name()), "\n", 'address: ', str(self.get_address()), '\n', 'age: ', str(self.get_age()), '\n', 'phone: ', str(self.get_phone()))
        print()


def main():
    person1 = Person('Sean', '2224 Missouri Ave', 26, '451-7386')
    person2 = Person('Karen', '4 Oxford Ct', 59, '814-5501')
    person3 = Person('Alan', '15493 Queen Elizabeth Court', 67, '814-5502')
    person1.__str__()
    person2.__str__()
    person3.__str__()
    person2.set_age(17)
    person2.__str__()


main()
