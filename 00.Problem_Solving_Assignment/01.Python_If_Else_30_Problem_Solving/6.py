num = 110
if num % 11 == 0 and num % 5 == 0:
    print("Divisible By Both 5 and 11")
elif num % 11 == 0:
    print("Divisible By 11")
elif num % 5 == 0:
   print("Divisible By 5")
else:
    print("Divisible By Neither")