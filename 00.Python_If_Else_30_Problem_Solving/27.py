user_hr = int(input("Enter Hours:"))
user_min = int(input("Enter Minutes:"))
user_sec = int(input("Enter Seconds:"))
if user_hr >= 0 and user_hr <= 23 and user_min >= 0 and user_min <=59 and user_sec >= 0 and user_sec <= 59:
    print("Valid Time")
else:
    print("Invalid Time")