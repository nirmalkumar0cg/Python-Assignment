user_year = int(input("Enter The Year You Want To Know If Its A Leap Year Or Not:"))
if user_year % 400 == 0 and user_year % 4 == 0 and user_year % 100 !=0:
    print("It is a leap year")
else:
    print("Not A Leap Year")