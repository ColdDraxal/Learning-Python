students={1:"Draxal",2:"Harry",3:"Darpan"}

def fun_students():
    choose_students=int(input("Which student\n1)Draxal\n2)Harry\n3)Darpan\n-> "))
    if choose_students not in students:
        print("Students not found")
        return
    students_ord=students[choose_students]+".txt"
    return students_ord

def add_marks(students_ord):
    marks=[]
    for x in range(1,6):
        marks.append(input(f"Subject {x}: "))
    with open(students_ord,"w") as f:
        f.write("\n".join(marks))

def view_marks(students_ord):
    try:
        with open(students_ord,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No files found")
        return
    
def show_average(students_ord):
    try:
        with open(students_ord,"r") as f:
            data=f.read().splitlines()
            marks1=[int(x) for x  in data]
            if not marks1:
                print("Numbers not found")
                return
        average=sum(marks1)/len(marks1)
        print(f"The average of {students_ord.replace('.txt','')} is {average}")
        return average
    except FileNotFoundError:
        print("It doesn't exist.")
        return     
    
def find_topper():
    topper=""
    top_avg=0
    for i in students:
        student_file=students[i]+".txt"
        avg=show_average(student_file)
        if avg is None:
            continue
        elif avg>top_avg:
            topper=student_file
            top_avg=avg
    if topper:
        print(f"The topper is {topper.replace('.txt','')} with average marks of {top_avg}")
    else:
        print("No data.")




print("Menu:")
while True:
    try:
        choose=int(input("1)Add marks\n2)View marks\n3)Show average\n4)Show topper\n5)Exit\nchoose: "))
        if choose==1:
            student_name=fun_students()
            if student_name is None:
                continue
            add_marks(student_name)
            print("Marks added successfully.")
        elif choose==2:
            student_name=fun_students()
            if student_name is None:
                continue
            view_marks(student_name)
        elif choose==3:
            student_name=fun_students()
            if student_name is None:
                continue
            show_average(student_name)
        elif choose==4:
            find_topper()
        elif choose==5:
            break
        else:
            print("Choose a valid option.")
    except ValueError:
        print("Enter a valid number")
        continue


print("You have exited the program.")