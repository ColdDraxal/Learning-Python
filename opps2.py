class College:
    college_name= "Bhairahaw Multiple Campus"
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def student_detail(self):
        print(f"{College.college_name}\nStudent Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\n")
    
s1=College("Darpan Basyal",21,"5th Semester")
s2=College("Willson Banjade",0.6,"Not Started")

# s1.student_detail()
s2.student_detail()
s2.age=1
print(s2.age)
s2.student_detail()
College.college_name="Butwal Multiple Campus"
print(College.college_name)
s2.student_detail()