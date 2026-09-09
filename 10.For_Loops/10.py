user_int=int(input("Enter A Positive Integer:"))
for i in range(1,user_int):
     if user_int % 2 == 0:
      print(f"{i+1}")
else:
 print("Enter A Positive Integer Not Negative")