# Take prices of 8 products.

# For every price:

# Below 500 → "Budget"
# 500–1999 → "Regular"
# 2000–4999 → "Premium"
# 5000 or more → "Luxury"
# Calculate:

# Total amount.
# Number of products in each category.
# Average product price.
total = 0
budget_count = 0
regular_count = 0
premium_count = 0
luxury_count = 0

for user_input in range(8):
    price_input = int(input("Enter The Price Of Products: "))
    total += price_input
    if price_input < 500:
        budget_count+=1
        print('Budget')
    elif price_input >= 500 and price_input <= 1999:
        regular_count+=1
        print('Regular')
    elif price_input >= 2000 and price_input <= 4999:
        premium_count+=1
        print('Premium')
    else:
        luxury_count+=1
        print('Luxury')
        
print(f"Total Of The Products:{total}")
print(f'''---Number Of Products In Each Category---
        Budget Products:{budget_count}
        Regular Products:{regular_count}
        Premium Products:{premium_count}
        Luxury Products:{luxury_count}
''')
print(f"Avg Product Price: {(price_input/user_input):.2f}")
