class Students:
    def __init__(self,name,grade,roll):
        self.name=name
        self.grade=grade
        self.roll=roll
    def intro(self):
        return f"Name: {self.name}\nGrade: {self.grade}\nRoll no: {self.roll}"
    @classmethod
    def student_details(cls,string):
        return cls(*string.split("-"))
student1=Students.student_details("Darpan Basyal-5th Semester-6")
print(student1.intro())