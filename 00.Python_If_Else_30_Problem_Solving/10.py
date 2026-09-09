user_age = int(input("Enter Your Age:"))
if user_age < 0:
    print("Invalid Age")
elif user_age < 18:
    print("Cannot Vote")
elif user_age >= 18 and user_age < 100:
    print("Can Vote")
else:
    print("Age Is Unrealistic")