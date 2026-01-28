# n=18
# no of guesses is 9
# print no of guesses is left
# game over


# Pattern Priniting
# Input = integer n
# Boolean = true or false
# True n=4
# *
# **
# ***
# ****
# False
# ****
# ***
# **
# *
"""
# 1
guess=1
correct=False
while guess<=9:
    n=int(input("guess a number:"))
    if n<18:
        print("You need to guess higher")
    elif n>18:
        print("You need to guess lower")
    else:
        print("You guessed it correctly")
        print("You guessed it in",guess,"time")
        correct=True
        break
    guess+=1
    print("You have",10-guess,"guesses left")
    
if correct:
    print("congratulations the correct number was indeed 18")
else:
    print("The correct number was 18. You can try again later.")
"""

# 2
n=int(input("Enter a number: "))
choice=int(input("Enter boolean 1 or 0: "))
choice=bool(choice)
if choice:
    for x in range(n):
        print((x+1)*"*")
else:
    for x in range(n,0,-1):
        print((x)*"*")