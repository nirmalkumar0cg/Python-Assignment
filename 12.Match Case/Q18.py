
# Q18. E-Commerce Application
# First ask for a category:

# 1 → Electronics
# 2 → Clothing
# For Electronics:

# 1 → Mobile
# 2 → Laptop
# 3 → Headphones
# For Clothing:

# 1 → Shirt
# 2 → Jeans
# 3 → Shoes
# Use nested match-case.





category = int(input('Choose a category:\n1. Electronics\n2. Clothing\n: '))

match category:
    case 1:
        product = int(input('Choose a product:\n1. Mobile\n2. Laptop\n3. Headphones\n: '))
        match product:
            case 1:
                print('Opening Mobile section')
            case 2:
                print('Opening Laptop section')
            case 3:
                print('Opening Headphones section')
    case 2:
        product = int(input('Choose a product:\n1. Shirt\n2. Jeans\n3. Shoes\n: '))
        match product:
            case 1:
                print('Opening Shirt section')
            case 2:
                print('Opening Jeans section')
            case 3:
                print('Opening Shoes section')

