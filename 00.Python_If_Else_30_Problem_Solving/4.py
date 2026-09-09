user_num1= int(input("Enter The First Number:"))
user_num2 = int(input("Enter A Second Number:"))
user_num3 = int(input("Enter A Third Number:"))
if user_num1 < user_num2 and user_num1 < user_num3:
    print(f"{user_num1} Is The Smallest")
elif user_num2 < user_num3 and user_num2 < user_num1:
    print(f"{user_num2} Is The Smallest")
else:
    print(f"{user_num3} Is the smallest")