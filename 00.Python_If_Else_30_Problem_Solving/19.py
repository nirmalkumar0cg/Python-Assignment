user_num = int(input("Enter A Number:"))
if user_num >= 0 and user_num <= 10:
    print("Number Is In Between 0-10")
elif user_num >= 11 and user_num <= 50:
    print("Number Is In Between 11-50")
elif user_num >= 51 and user_num <= 100:
    print("Number Is In Between 51-100")
elif user_num > 100:
    print("Above 100")
else:
    print("Negative")