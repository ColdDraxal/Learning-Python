"""

def fun1():
    print("Hello world!!!")
fun2=fun1
# del fun1 
fun2()
"""
"""
def funrec(a,c):
    if a==0:
        return print(c)
    elif a==1:
        return list(c) #this doesnt work lmao

b=funrec(0,"This is Draxal")

"""
"""
def executor(func):
    return func((1,3))
print(executor(sum))
"""

def dec1(fun1):
    def exc(*args,**kwargs):
        print("executing")
        y=fun1(*args,**kwargs)
        print(y)
        print("executed")
        return y
    return exc
"""
@dec1
def rev(x,a=0):
    if x==0:
        return a
    return rev(x//10,a*10+x%10)
a=int(input("Enter a number: ")) #output maybe be weird but its because i used recrusion
print(rev(a))

# @dec1
# def fun2():
#     print("Man IS Gay")
# # fun2=dec1(fun2)
# fun2()
"""
@dec1
def sum(a,b):
    return a+b
sum(8,12)
