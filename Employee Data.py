
class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = int(employee_number)

    def set_name(self, name):
        self.name = name

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

    def get_name(self):
        return self.name

    def get_employee_number(self):
        return self.employee_number

    def __str__(self):
        print("Name:", str(self.get_name()), "\nEmployee number:", format(self.get_employee_number(), "5.0f"))


class ProductionWorker(Employee):

    def __init__(self, name, employee_number, shift, hourly_wage):
        Employee.__init__(self, name, employee_number)
        self.shift = shift
        self.hourly_wage = float(hourly_wage)

    def set_shift(self, shift):
        self.shift = shift

    def set_hourly_wage(self, hourly_wage):
        self.hourly_wage = hourly_wage

    def get_shift(self):
        return self.shift

    def get_hourly_wage(self):
        return self.hourly_wage

    def __str__(self):
        print("Name:", str(self.get_name()), "\nEmployee number:", format(self.get_employee_number(), "5.0f"),
              " Shift:", str(self.get_shift()), "Hourly wage: $", format(self.hourly_wage, ".2f"))


def main():
    employee_list = []
    again = "y"
    while again == "y":
        print("Add Employee Data")
        print()
        name = input("enter the employee name")
        number = input("enter the employee number")
        production = input("is the employee production y or n")
        production = production.lower()
        if production == "y":
            shift = input("what shift is the employee on")
            wage = input("what is the hourly wage")
            employee = ProductionWorker(name, number, shift, wage)
            employee_list.append(employee)
            again = input("add another?")
        else:
            employee = Employee(name, number)
            employee_list.append(employee)
            again = input("add another?")
    print()
    print("EMPLOYEES")
    print("_________________________________")
    for employees in employee_list:
        employees.__str__()
        print()


main()
