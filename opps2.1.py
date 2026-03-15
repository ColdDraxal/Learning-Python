# Practising classmethod (@classmethod) cls.

class College:
    college_name= "Bhairahaw Multiple Campus"
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def student_detail(self):
        print(f"{College.college_name}\nStudent Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\n")
    @classmethod
    def change_clg(cls,newclg):
        cls.college_name=newclg

s1=College("Darpan",21,10)
s1.change_clg("Lumbini City")
# print(s1.college_name)
College.change_clg("Butal Multiple Campus")
print(s1.college_name)
