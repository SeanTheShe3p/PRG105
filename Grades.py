number = int(input('how many students are you adding?'))
outfile = open('grades.txt', 'w')
for grades in range(1, number + 1):
    name = input('what is the name of student ' + str(grades))
    grade = input('what is the grade of student ' + str(grades))
    student_grades = [name, grade]
    lineout = "'" + student_grades[0] + "', '" + student_grades[1] + "'\n"
    outfile.writelines(lineout)
outfile.close()
