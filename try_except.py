# Try Except Exception

n1=input("Enter 1st number: ")
n2=input("Enter 2nd number: ")
try:
    print(f"Sum is {float(n1)+float(n2):g}")
# except Exception as e:
# except ValueError as e:
#     print(e)
# OR
except ValueError:
    print("Please Enter numbers only.\n")
print("This must be printed")
    

