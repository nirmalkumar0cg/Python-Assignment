user_input = input("Enter The Character:")
if user_input.isupper():
    print("Uppercase")
elif user_input.islower():
    print("Lowercase")
elif user_input.isdigit():
    print("Digit")
else:
    print("Special Character")