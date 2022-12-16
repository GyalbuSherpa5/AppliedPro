from datetime import date

stdName = input("Enter your name ")
intake = input("Enter your intake ")

subjects = int(input("Enter total number of subjects "))


def initialDisplay():
    print(f"""
                    Sunway Int'l College Grading System
                            Maitidevi,Kathmandu
                                    
                                                Date : {date.today()}
    Name:       {stdName}
    Intake:     {intake}
    Programme : BCS
    Faculty:    Faculty of engineering, science and technology
""")


def grade(score):
    if score >= 90:
        return "A+"
    elif 80 <= score < 90:
        return "A"
    elif 70 <= score < 80:
        return "B+"
    elif 60 <= score < 70:
        return "B-"
    elif 50 <= score < 60:
        return "B"
    elif 40 <= score < 50:
        return "C+"
    elif 30 <= score < 40:
        return "D"
    else:
        return "F"


courseName = []
courseCode = []
marks = []
grades = []

for i in range(subjects):
    name = input(f"Enter subject name ({i + 1}): ")
    name = name.upper()
    courseName.append(name)

    code = input(f"Enter course code ({i + 1}): ")
    code = code.upper()
    courseCode.append(code)

    mark = int(input(f"Enter mark obtained ({i + 1}): "))
    marks.append(mark)

    grades.append(grade(mark))

initialDisplay()

print(f"""
    Course Code      Course Description          Marks Obtained        Grade
    
    """)

for i, j, k, l in zip(courseCode, courseName, marks, grades):
    print(f"""
    {i:<10}        {j:25}        {k:<10}        {l:<10}
    """)


def gpa(percentage):
    if percentage >= 90:
        return 4.0
    elif 80 <= percentage < 90:
        return 3.6
    elif 70 <= percentage < 80:
        return 3.2
    elif 60 <= percentage < 70:
        return 2.8
    elif 50 <= percentage < 60:
        return 2.4
    elif 40 <= percentage < 50:
        return 2.0
    elif 30 <= percentage < 40:
        return 1.6
    else:
        return 0.8


total = 0

for i in marks:
    total += i

per = total / subjects

gpa = gpa(per)
gra = grade(per)
print(f"Student {stdName} got GPA : {gpa} and Grade: {gra}")
