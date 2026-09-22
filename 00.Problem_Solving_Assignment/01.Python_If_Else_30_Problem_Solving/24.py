user_cost=float(input("Enter Your Total Amount:"))
if user_cost < 500:
    print(f"Original Amount:{user_cost}\nDiscount:0%\nDiscount amount:$0\nFinal amount{user_cost}")
elif user_cost >= 500 and user_cost <= 999:
    print(f"Original Amount:{user_cost}\nDiscount:5%\nDiscount amount:{user_cost*0.05}\nFinal amount{user_cost-(user_cost*0.05)}")
elif user_cost >= 1000 and user_cost <= 1999:
    print(f"Original Amount:{user_cost}\nDiscount:10%\nDiscount amount:{user_cost*0.1}\nFinal amount{user_cost-(user_cost*0.1)}")
elif user_cost >= 2000 and user_cost <= 4999:
    print(f"Original Amount:{user_cost}\nDiscount:15%\nDiscount amount:{user_cost*0.15}\nFinal amount{user_cost-(user_cost*0.15)}")
elif user_cost >= 5000:
    print(f"Original Amount:{user_cost}\nDiscount:20%\nDiscount amount:{user_cost*0.2}\nFinal amount{user_cost-(user_cost*0.2)}")

