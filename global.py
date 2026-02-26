"""
x=12 #This is Global Variable.
#Any variable outside ( of functions or anything) is called global variable
def darpan():
    x=19 #This is local variable
    print (x) #This print is inside local variable so whenever this function is called it will 
              # print the value of x inside local variable

darpan() # function is called
print (x) #It will print global variable since it needs specific command to change g.v inside function
"""
#here after calling global command in nested funcion the global value was changed 
"""

x=13
def draxal():
    x=17
    def dangit():
        global x
        x=18
    dangit()
    print(x)
draxal()
print(x)
"""

#Here to change the local variable from nested function we use nonlocal command
#using global command will only change the varibale of outside

def first():
    x=12
    def second():
        nonlocal x
        x=13
    print (f"Brefore x value was {x}")
    second()
    print(f"After x value was {x}")
first()
