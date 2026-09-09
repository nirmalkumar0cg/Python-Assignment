user_num= int(input("Enter A Number:"))
user_num2 = int(input("Enter A Second Number:"))
if user_num > user_num2:
    print(f"{user_num} is larger than {user_num2}")
elif user_num2 > user_num:
    print(f"{user_num2} is larger than {user_num}")
elif user_num == user_num2:
    print("Both Are Equal")
else:
    print("Enter A Valid Number")

