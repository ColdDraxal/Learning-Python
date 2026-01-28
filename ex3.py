# n=18
# # number of guesses: 9
# # print no of guesses left
# # if finished game over:
# #Wap to enter a number and match it with the secret number i.e n=18
# # if user puts 12 says Its higher than this and if users says 22 say its lower than this

j=1
while j<=9:
    i=int(input("Enter a number: "))
    if i>18:
        print("You have to guess lower.")
    elif i<18:
        print("You have to guess higher.")
    else:
        print("You won")
        print("It took him ",j," number go guesses to finish")
        break
    print(9-j," Guesses left")
    j=j+1
if j>9:
    print("Game over")

# n=18
# j=1
# print("Number of guesses is limited to only 9 times: ")
# while (j<=9):
#     i = int(input("Guess the number :\n"))
#     if i<18:
#         print("you enter less number please input greater number.\n")
#     elif i>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(j,"no.of guesses he took to finish.")
#         break
#     print(9-j,"no. of guesses left")
#     j = j + 1

# if(j>9):
#     print("Game Over")