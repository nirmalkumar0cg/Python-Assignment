units = int(input("Enter the total units consumed: "))
total_bill = 0
if units <= 100:
    total_bill = units * 5
elif units <= 200:
    total_bill = 500 + (units - 100) * 7
else:
    total_bill = 500 + 700 + (units - 200) * 10
print("Total Electricity Bill: ₹", total_bill)