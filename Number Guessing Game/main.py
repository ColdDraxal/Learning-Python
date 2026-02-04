import random
guess=random.randint(1,50)
attempt=1
Win=False
while attempt<=9:
    num=int(input("Enter a number: "))
    rem_attempt=9-attempt
    if num == guess:
        print(f"Congratulations!!! The correct number was: {guess}")
        print(f"You guessed it in {attempt} time.")
        Win=True
        break
    elif num>guess:
        print("Wrong!!! You have to guess lower.")
        print(f"You have {rem_attempt} left")
    else:
        print("Wrong!!! You have to guess higher.")
        print(f"You have {rem_attempt} left")
    attempt=attempt+1
if Win:
    print(f"The correct number was indeed {guess}")
else:
    print(f"The correct number was {guess}. Better luck next time.")

