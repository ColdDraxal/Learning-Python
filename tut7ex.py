"""print("what is your name?")
name=input()
print("What is your age?")
n=input()
print("Hello ",name ,"you will be ", int(n)+7 ,"in 7 years.")
print("first number?")
num1=input()
print("second number?")
num2=input()
print("the sum is:",int(num1)+int(num2))
print("the sub is:",int(num1)-int(num2))
print("the product is:",int(num1)*int(num2))
print("the division is:",float(num1)/float(num2))
#print("Python is fun!\nIt supports\"quotes\"and\\backslashes\\")"""
#print("""Python is fun!
#It supports "quotes" and \\backslashes\\""")
#a=2
#b=3
#c=a+b
#print("sum is:",c)
#a,b,c are variables and  print displays the output c is the variable  used to sum a and b

#asking user for numbers for calculation
"""print("What is your first number?")
a=float(input())
print("What is your second number?")
b=float(input())
#performing calculations sum,product, sum*100
c=a+b
d=a*b
e=c*100
#printing the results
print(f"sum:{c}\n"*100)
print(f"product:{d}\n"*100)
print(f"sum multiplied by 100:{e}\n"*100)"""
#asking user for numbers for calculation 
print("What is your first number?")
a=float(input())
print("What is your second number?")
b=float(input()) 
#performing calculations sum,product, sum*100 
c=a+b 
d=a*b 
e=c*100 
#printing the results 
print("sum:\n",(str(c)+"\n")*5) 
print("product:\n",(str(d)+"\n")*5)
print("sum multiplied by 100:\n",(str(e)+"\n")*5)