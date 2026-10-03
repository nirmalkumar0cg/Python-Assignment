customer_priority = 1

match customer_priority:
    case 1:
        print('Low')
    case 2:
        print('Medium')
    case 3:
        print('High')
    case 4:
        print('Critical')
    case _:
        print('Invalid Input')