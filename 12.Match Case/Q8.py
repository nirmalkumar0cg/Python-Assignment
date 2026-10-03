user_input=int(input('Enter Choice: '))

match user_input:
    case 1:
        print('Morning Show')
    case 2:
        print('Afternoon Show')
    case 3:
        print('Evening Show')
    case 4:
        print('Night Show')
    case _:
        print('Invalid Input')