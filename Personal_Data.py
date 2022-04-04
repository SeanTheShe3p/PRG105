class Personal_data:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone


    def set_name(self, name):
        name = self.__name


    def set_age(self, age):
        age = self.__age


    def set_address(self, address):
        address = self.__address


    def set_phone(self, phone):
        phone = self.__phone


    def get_name(self):
        return self.__name


    def get_age(self):
        return self.__age


    def get_address(self):
        return self.__address


    def get_phone(self):
        return self.__phone


    def get_info(self):
        print("The users info is", str(self.get_name()), str(self.get_age()), str(self.get_address()), str(self.get_phone()), sep=" ")



def main():
    person_1 = Personal_data("Sean", 26, "2224", "8154517386")
    person_2 = Personal_data("Karen", 59, "4 Oxford Court", "8158145501")
    person_3 = Personal_data("Alan", 67, "15493 Queen Elizabeth Court", "8158145502")
    person_1.get_info()
    person_2.get_info()
    person_3.get_info()


main()
