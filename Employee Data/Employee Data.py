from Employee import Employee, ProductionWorker


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
