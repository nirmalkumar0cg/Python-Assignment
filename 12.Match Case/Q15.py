customer_membership = 1

match customer_membership:
    case 1:
        print('Basic Membership')
    case 2:
        print('Basic Membership')
    case 3:
        print('Premium Membership')
    case 4:
        print('Premmium Membership')
    case _:
        print('Invalid Input')