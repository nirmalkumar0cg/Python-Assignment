# user_age=int(input("Enter Your age"))
# user_marks=float(input("Enter Your Marks:"))
has_id = input("Do You Have A Id?(Yes/No)").strip().lower()
if has_id == "no":
    has_id == False
elif has_id == "yes":
    has_id == True
else:
    print("Enter A Valid Value")



# if user_age>=18 and user_marks>=60 and has_id==True:
#     print("Eligible")
# else:
#     print("Not Eligible")