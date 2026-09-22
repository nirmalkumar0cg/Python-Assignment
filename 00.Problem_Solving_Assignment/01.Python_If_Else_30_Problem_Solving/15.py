cost_price= float(input("Enter The Cost Price:"))
sell_price = float(input("Enter The Selling Price:"))
profit = sell_price-cost_price
loss = cost_price-sell_price
if cost_price == 0 or cost_price <= 0:
    print("Invalid")
elif cost_price < sell_price:
    print(f"The Profit Percentage Is:{profit/cost_price*100}")
else :
    if sell_price < cost_price:
     print(f"The Loss Percentage Is:{loss/cost_price*100}")

