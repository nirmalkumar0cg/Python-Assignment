# Q25. Movie Ticket System
# Create a movie ticket menu:

# 1 → Regular
# 2 → Premium
# 3 → VIP
# Ask for the customer's age after selecting the ticket type.

# If age is below 5, display:

# Free Entry
# Otherwise display the selected ticket type.

choice = int(input('----Ticket Type----\n1.Regular\n2.Premium\n3.VIP\n: '))

match choice:
    case 1:
        age = int(input("Enter Your Age: "))
        if age < 5:
            print('Free Entry')
        else:
            print('Regular')
    case 2:
        age = int(input("Enter Your Age: "))
        if age < 5:
            print('Free Entry')
        else:
            print('Premium')
    case 3:
        age = int(input("Enter Your Age: "))
        if age < 5:
            print('Free Entry')
        else:
            print('V.I.P')
