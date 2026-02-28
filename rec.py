"""
def factorial_itreation(n):
    f=1
    for i in range(n):
        f=f*(i+1)
    return f
def factorial_recursion(n):
    if n==1:
        return n
    else:
        return n*factorial_recursion(n-1)
number=int(input("Enter a number: "))
print(factorial_itreation(number))
print(factorial_recursion(number))

"""
"""
def walk(steps):
    if steps == 0:
        return
    walk(steps-1)
    print("The number of steps is ",steps)

walk(100)
"""
#  sum of integers in a number
"""
def sum1(x):
    if x<10:
        return x
    return sum1(x//10)+(x%10)
print(sum1(123456))

"""

# reversing a integer
"""

def rev(x,r=0):
    if x==0:
        return r
    return rev(x//10, r*10 + x%10)
print(rev(1234))
"""
# check if palindrome or not
"""
def is_pali(x):
    if len(x)<=1:
        return True
    elif x[0]!=x[-1]:
        return False
    return is_pali(x[1:-1])
wordd=input("Enter a word: ")
print(is_pali(wordd))
    
"""
# Print all subsets of a string (power set)

def subsets(s, i=0, current=""):
    if i == len(s):
        print(current)
        return
    
    subsets(s, i+1, current)          # exclude character
    subsets(s, i+1, current + s[i])   # include character

subsets("ab")