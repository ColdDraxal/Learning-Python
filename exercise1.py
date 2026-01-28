# with open("notes.txt","a") as f:
#     f.write(input("Write notes: \n")+"\n")
# print("saved")
# with open("notes.txt","r") as f:
#     for line in f:
#         print(line,end="")





"""
try:
    with open("count.txt","r") as f:
        count=int(f.read())
except FileNotFoundError:
    count=0
count+=1
with open("count.txt","w") as f:
    f.write(str(count))
print("Program has been run", count, "times")
"""

"""
try:
    with open("highscore.txt","r") as f:
        pre_hs=int(f.read())
except FileNotFoundError:
        pre_hs=0
highscore=int(input("Enter a number:"))
if highscore>=pre_hs:
    with open("highscore.txt","w") as f:
        f.write(str(highscore))
else:
    highscore=pre_hs
    with open("highscore.txt","w") as f:
        f.write(str(highscore))
print("The high score is: ",highscore)
"""



"""
try:
    with open("money.txt","r") as f:
        m=int(f.read())
except FileNotFoundError:
    m=0
money=int(input("Enter the amount of money you gotta add: "))
total_m=money+m
with open("money.txt","w") as f:
    f.write(str(total_m))
print("The total amount of money is: ",total_m)
"""
"""
ask=input("Enter a file name to read its content(must end with .txt): ")
try:
    with open(ask,"r") as f:
        for line in f:
            print(line,end="")
except FileNotFoundError:
    print("Please Enter a valid file name")
    """