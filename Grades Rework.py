def main():
    line = []
    student_grades = []
    count = int(input('how many students'))
    for student in range(1, count + 1):
        name = input('what is the name of student ' + str(student))
        grade = input('what is the grade of student ' + str(student))
        line.append(name)
        line.append(grade)
        student_grades.append(line)
        line = []
    print(student_grades)

    outfile = open('grades.txt', 'w')
    for line in student_grades:
        lineout = "'", line[0], "'", ",", "'", line[1], "'", "\n"
        outfile.writelines(lineout)
    outfile.close()


main()
