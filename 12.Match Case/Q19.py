# Q19. Food Delivery Application
# First ask:

# 1 → Vegetarian
# 2 → Non-Vegetarian
# If Vegetarian:

# 1 → Paneer
# 2 → Dal
# 3 → Veg Biryani
# If Non-Vegetarian:

# 1 → Chicken Biryani
# 2 → Chicken Curry
# 3 → Fish Fry
# Use nested match-case.


category = int(input('Choose a category:\n1. Vegetarian\n2. Non-Vegetarian\n: '))

match category:
    case 1:
        food = int(input('Choose a dish:\n1. Paneer\n2. Dal\n3. Veg Biryani\n: '))
        match food:
            case 1:
                print('Opening Paneer section')
            case 2:
                print('Opening Dal section')
            case 3:
                print('Opening Veg Biryani section')
    case 2:
        food = int(input('Choose a dish:\n1. Chicken Biryani\n2. Chicken Curry\n3. Fish Fry\n: '))
        match food:
            case 1:
                print('Opening Chicken Biryani section')
            case 2:
                print('Opening Chicken Curry section')
            case 3:
                print('Opening Fish Fry section')

