"""
You are writing a program to determine if a student is eligible for financial aid for the next semester. To qualify,
the student must either be a new student, or a current student with a GPA of 2.0 or higher.  Additionally, the student
may not have a criminal record for drugs, must enroll in a minimum of six credit hours of classes, and must have
a gross yearly income of less than $50,000.  You will gather information from the student, and you will let them
know if they are eligible for financial aid or not.
"""
financial_aid = True
gpa = float(2.0)
criminal_history = False
credit_hours = int(6)
yearly_income = float(50000)
status = input('Are you a new student or current student?')
if status == 'new':
    print('welcome to school!')
elif status == 'current':
    if gpa > float(input('what is your gpa?')):
        financial_aid = False
else:
    financial_aid = False
if input('Do you have a drug related criminal record?') != 'no':
    Financial_aid = False
if credit_hours > int(input('how many credit hours are you enrolled in?')):
    financial_aid = False
if yearly_income <= float(input('what is your annual income?')):
    financial_aid = False
if financial_aid:
    print('Financial aid approved!')
else:
    print('Not qualified for financial aid.')
