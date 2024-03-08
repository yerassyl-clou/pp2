class Teacher:                              #same funcs for different classes
    def __init__(self, university, prof):
        self.university = university
        self.prof = prof
    
    def prnt(self):
        print("Teachong " + str(self.prof) + " in " + str(self.university))
    
class Student:
    def __init__(self, university, major):
        self.university = university
        self.major = major

    def prnt(self):
        print("Studying " + str(self.major) + " in " + str(self.university))

Teacher1 = Teacher("KBTU", "Information Systems")
Student1 = Student("KBTU", "Information Systems")

for x in (Teacher1, Student1):
    x.prnt()