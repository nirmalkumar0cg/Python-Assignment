user_signal=input('Enter The Traffic Light Color: ')

match user_signal:
    case 'red':
        print('Stop')
    case 'yellow':
        print('Wait')
    case 'green':
        print('Go')
    case _:
        print('Invalid Signal')