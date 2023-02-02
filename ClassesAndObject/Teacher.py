class Teacher:
    age = 12

    def getSubject(self):
        print("AP")


class JunTeacher1(Teacher):
    name = "hero"

    def getSubject(self):
        print("CG")


class JunTeacher2(JunTeacher1):
    def getSubject(self):
        print("CA")


don = JunTeacher2()
don.getSubject()
print(don.name)
print(don.age)

