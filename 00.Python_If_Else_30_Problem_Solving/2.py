user_num = int(input("Enter Your Number:"))
if user_num > 0 and user_num % 2 == 0:
    print("Positive Even")
    if user_num % 2 == 1:
     print("Positive Odd")
elif user_num < 0 and user_num % 2 == 0:
   print("Negative Even")
elif user_num % 2 == 1:
   print("Negative Odd")
else:
   print("Zero")


