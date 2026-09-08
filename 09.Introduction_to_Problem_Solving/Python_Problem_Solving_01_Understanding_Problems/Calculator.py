#For Taking Input From The User In Integar Format As By Default Input Is String.
user_num1=int(input("Enter Your 1st Number:").strip())
user_num2=int(input("Enter Your 2nd Number:").strip())
# user_num1,user_num2=map(int,input("Enter Your Both Number:").split())
calculation_method = int(input("What Method Do You Want To Use?:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Floor Division\n:"))
if calculation_method == 1:
    print(f"Addition:{user_num1+user_num2}")
elif calculation_method == 2:
    print(f"Substraction:{user_num1-user_num2}")
elif calculation_method == 3:
    print(f"Multiplication:{user_num1*user_num2}")
elif calculation_method == 4:
    print(f"Division:{user_num1/user_num2}")
elif calculation_method == 5:
    print(f"Flood Division:{user_num1//user_num2}")
else:
    print("Enter A Valid Value")
