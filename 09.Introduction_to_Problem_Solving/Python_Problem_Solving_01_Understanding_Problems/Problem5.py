user_price = float(input("Enter Your Price To Check Eligibility For Discount:"))
if user_price >= 1000:
    print(f"You're Eligible For Discount Pay:{user_price*0.9}")
else:
    print(f"You're Not Eligible For Discount Pay:{user_price}")