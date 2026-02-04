pass_word=input("Create a password: ").strip()
check_0=any(x in "@#$%&_!" for x in pass_word)
if not pass_word:
    print("Please enter a password.")
elif len(pass_word)<8:
    print(f"Your password {pass_word} is weak.")
elif len(pass_word)>=8 and check_0:
    print(f"Your password {pass_word} is strong.")
elif len(pass_word)>=8:
    print(f"Your password is medium.")