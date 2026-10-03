user_input=int(input('Enter Choice: '))

match user_input:
    case 1:
        print('Opening Account Balance')
    case 2:
        print('Opening Mini Statement')
    case 3:
        print('Opening Fund Transfer')
    case 4:
        print('Opening Bill Payment')
    case 5:
        print('Opening Customer Support')
    case _:
        print('Invalid Input')