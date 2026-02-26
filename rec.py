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