def sumation(n):
    if n==1:
        return 1
    else:
        return n + sumation(n-1)
    
number=int(input("Enter a number: "))
print(f"The sumation of first {number} natural number is: {sumation(number)}")