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
def square(a):
    return a*a
def cube(a):
    return a*a*a
func=[square,cube]
for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val)