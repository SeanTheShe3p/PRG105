"""
You are writing a program to determine if a student is eligible for financial aid for the next semester. To qualify,
the student must either be a new student, or a current student with a GPA of 2.0 or higher.  Additionally, the student
may not have a criminal record for drugs, must enroll in a minimum of six credit hours of classes, and must have
a gross yearly income of less than $50,000.  You will gather information from the student, and you will let them
know if they are eligible for financial aid or not.
"""
financial_aid = True
status = input('Are you a new student or current student? please enter n or r.')
if status == 'r' or status == 'R':
    gpa = float(input('what is your current gpa?'))
    if gpa < 2.0:
        financial_aid = False
record = input('do you have a criminal record? y or n')
if record == 'y' or record == 'Y':
    financial_aid = False
credit = int(input('how many credit hours are you enrolled in?'))
if credit < 6:
    financial_aid = False
income = float(input('what is your yearly income?'))
if income > 50000:
    financial_aid = False
if financial_aid:
    print('Financial aid approved!')
else:
    print('Not qualified for financial aid.')
