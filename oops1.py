class Students:
    name="Unknown"
    age="Unknown"
    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
stud1=Students()
stud2=Students()

stud1.name="Darpan Basyal"
stud1.age=21

stud2.name="Brody Kaluwa"
stud2.age=35

stud1.show_details()
stud2.show_details()
stud1.Holiday_leaves=8
print(stud1.__dict__)