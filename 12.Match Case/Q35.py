# Q35. Restaurant Ordering System
# Create a restaurant ordering system.

# First select a category:

# 1 → Starters
# 2 → Main Course
# 3 → Desserts
# 4 → Drinks
# Then show different items for each category.

# Example:

# Starters:

# 1 → Soup
# 2 → Spring Roll
# 3 → Garlic Bread
# Main Course:

# 1 → Pizza
# 2 → Pasta
# 3 → Biryani
# Desserts:

# 1 → Ice Cream
# 2 → Cake
# 3 → Gulab Jamun
# Drinks:

# 1 → Coffee
# 2 → Tea
# 3 → Juice
# Use nested match-case.

category = int(input('----Restaurant Ordering System----\n1.Starters\n2.Main Course\n3.Desserts\n4.Drinks\n: '))

match category:
    case 1:
        item = int(input('----Starters----\n1.Soup\n2.Spring Roll\n3.Garlic Bread\n: '))
        match item:
            case 1:
                print("Soup selected")
            case 2:
                print("Spring Roll selected")
            case 3:
                print("Garlic Bread selected")
    case 2:
        item = int(input('----Main Course----\n1.Pizza\n2.Pasta\n3.Biryani\n: '))
        match item:
            case 1:
                print("Pizza selected")
            case 2:
                print("Pasta selected")
            case 3:
                print("Biryani selected")
    case 3:
        item = int(input('----Desserts----\n1.Ice Cream\n2.Cake\n3.Gulab Jamun\n: '))
        match item:
            case 1:
                print("Ice Cream selected")
            case 2:
                print("Cake selected")
            case 3:
                print("Gulab Jamun selected")
    case 4:
        item = int(input('----Drinks----\n1.Coffee\n2.Tea\n3.Juice\n: '))
        match item:
            case 1:
                print("Coffee selected")
            case 2:
                print("Tea selected")
            case 3:
                print("Juice selected")