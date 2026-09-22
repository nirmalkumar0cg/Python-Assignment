user_num1 = int(input("Enter Your First Number:"))
user_num2 = int(input("Enter Your Second Number:"))
operator = int(input("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n:"))
if operator == 1:
    print(f"{user_num1+user_num2}")
elif operator == 2:
    print(f"{user_num1-user_num2}")
elif operator == 3:
    print(f"{user_num1*user_num2}")
elif operator == 4 and user_num2 == 0:
    print("Not Divisiable")
else:
    print({user_num1/user_num2})