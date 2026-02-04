def getdate():
    import datetime
    return datetime.datetime.now()
def nameA():
    customers=["harry","draxal","firoj"]
    name1=input("Enter a name: ").lower().strip()
    if name1 not in customers:
        print("Only registed customers allowed (Harry,Draxal,Firoj)")
        raise SystemExit
    return name1+"diet.txt"
def nameB():
    customers=["harry","draxal","firoj"]
    name2=input("Enter a name: ").lower().strip()
    if name2 not in customers:
        print("Only registed customers allowed (Harry,Draxal,Firoj)")
        raise SystemExit
    
    return name2+"exercise.txt"
def adddiet(name1):
    with open(name1,"a") as f:
        w1=input("Enter diet")+"\n"
        f.write(f"{getdate()}  {w1}")
        print("diet added")
def addexercise(name2):
    with open(name2,"a") as f:
        w2=("Enter exercise:")+"\n"
        f.write(f"{getdate()}  {w2}")
        print("exercise added")
def readdiet(name1):
    with open(name1,"r") as f:
       for line in f:
           print(line,end="")
def readexercise(name2):
    with open(name2,"r") as f:
        for line in f:
           print(line,end="")

print("Would you like to log or retrieve health data?")
try:
    c1=int(input("Press:\n1)Log\n2)Retrieve\nPress a number: "))
except ValueError:
    print("Must be a number")
    raise SystemExit
if c1 == 1:
    print("Would you like to log diet or exercise: ")
    try:
        c2=int(input("Press:\n1)Diet\n2)Exercise\nEnter a number: "))
    except ValueError:
        print("Must be a number")
        raise SystemExit
    if c2==1:
        n1=nameA()
        adddiet(n1)
    elif c2==2:
        n1=nameB()
        addexercise(n1)
    else: 
        print("Invalid choice")
        raise SystemExit
elif c1==2:
    print("Would you like to retrieve diet or exercise: ")
    try:
        c3=int(input("Press:\n1)Diet\n2)Exercise\nEnter a number: "))
    except ValueError:
        print("Must be a number")
        raise SystemExit
    if c3==1:
        n2=nameA()
        try:
            readdiet(n2)
        except FileNotFoundError:
            print("No logs yet")
    elif c3==2:
        n2=nameB()
        try:
            readexercise(n2)
        except FileNotFoundError:
            print("No logs yet")
    else: 
        print("Invalid choice")
        raise SystemExit
else: 
        print("Invalid choice")
        raise SystemExit



#Health Management System

# 3 clients - 1. Feroz 2. Sushil 3. Trishan
#Requirements:
"""
use this function:
def getdate():
    import datetime
    return datetime.datetime.now()

1. Total 6 files:
    a. 3 files for exercise
    b. 3 files for diet
2. Write a function that when executed takes as input client name and log type (exercise or diet).
[timestamp here] -> log value
3. One more function to retrieve exercise or diet for any client.

so final 
first ma ask garxa log garney ho ki retrieve garney ho?
then kasko garney ho?
then exercise ho ki diet ho?
print message accordingly
  """  
