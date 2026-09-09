cost_price = 500
selling_price = 999
if cost_price < selling_price:
    print(f"The Profit Is:{selling_price-cost_price}")
elif selling_price < cost_price:
    print(f"The Loss Is:{selling_price-cost_price}")
else:
    print("No Profit No Loss")