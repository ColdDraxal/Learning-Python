# -------------------------------Join---------------------------------
"""
WWE=["John Cena","Great Khali","Roman Reings","Dean Ambrose","Seth Rollins",
     "Undertaker","Kane","HHH"]
# a=" ".join(WWE)
a=" and ".join(WWE)
print(a," Your favourite stars are coming to Nepallllllllllllll")
"""

# a= ("Draxal")
# b=", ".join(a)
# print(b)


# ------------------------------MAP--------------------------------
"""
numbers=[1,2,3,4,5,6]
b=",".join(map(str,numbers))
print(b)
"""
"""
numbers=["1","2","3","4","5"]
# numbers=list(map(int,numbers))
numbers=(map(int,numbers))
# print(numbers[0])
print(numbers) #returns iterator p.s google itreator
"""

"""
def square(a):
    return a*a
def cube(a):
    return a*a*a
func=[square,cube]
for i in range(5):
    val=list(map(lambda x:x(i),func)) #x:x(i),func means xis both functions so
                                      #square(i),cube(i)
    print(val)

    """
# ---------------------Filter-----------------
"""
list1=[1,2,3,4,5,6,7,7,89,9,10]
def gt5(x):
    return x>5
gt55=list(filter(gt5,list1))
print(gt55)
"""
"""
name=["Sam","Ram","Don","Draxal","Darpan"]
leng=list(filter(lambda x:len(x)>3,name))
print(leng)
"""
# --------------------Reduce------------------

from functools import reduce
list2=[1,2,3,4]
a=reduce(lambda x,y:x+y,list2) #Using Reduce
# a=0                          #Not Using Reduce
# for i in list2:
#     a=a+i
print(a)