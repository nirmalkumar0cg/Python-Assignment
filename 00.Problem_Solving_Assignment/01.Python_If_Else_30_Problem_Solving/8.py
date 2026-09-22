user_marks=int(input("Enter Your Marks:"))
if user_marks < 0:
    print("Invalid Marks")
elif user_marks < 40:
    print("Fail")
elif user_marks >= 40 and user_marks <= 100:
    print("Pass")
else:
    print("Invalid Marks")