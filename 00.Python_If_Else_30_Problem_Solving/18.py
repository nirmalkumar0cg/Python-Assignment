user_temp = float(input("Enter A Temp In °C:"))
if user_temp < 0 :
    print("Freezing")
elif user_temp >=0 and user_temp <=15:
    print("Very Cold")
elif user_temp >= 16 and user_temp <= 25:
    print("Cold")
elif user_temp >=26 and user_temp <= 35:
    print("Normal")
else:
    print("Hot")

