# print n to 1
"""
def count(x):
    if x==0:
        return 
    print(x)
    count(x-1)
count(10)

"""
# print 1 to n

"""
def count(x):
    if x == 0:
        return
    else:
        count(x-1)
    print(x)

count(10)

"""

# Sum of numbers from 1 to n

"""

def sum1(x):
    if x==0:
        return x
    return x + sum1(x-1)
print(sum1(5))

"""
# Sum of digits
"""

def sumdigits(x):
    if x<10:
        return x
    return sumdigits(x//10) + x%10
print(sumdigits(12345))

"""
#  count digits

"""
def count(x,c=0):
    if x==0:
        return c
    return count(x//10,c+1)
print(count(1234))

"""

"""
def count(n):
    if n < 10:
        return 1
    return 1 + count(n//10)
print(count(1234))

"""
#  reversing a number
"""
def rev(x,i=0):
    if x==0:
        return i
    return rev(x//10,x%10+i*10)
print(rev(1234))
"""
# subsets of a string

def subsets(x,i=0,c=""):
    if i==len(x):
        print(c)
        return
    subsets(x,i+1,c)
    subsets(x,i+1,c+x[i])
word=input("Enter a word: ")
subsets(word)