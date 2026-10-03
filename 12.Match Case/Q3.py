user_atm_choice = int(input('Enter Choice: '))

match user_atm_choice:
    case 1:
        print('Check Balance')
    case 2:
        print('Withdraw Money Selected')
    case 3:
        print('Deposit Money')
    case 4:
        print('Change Pin')
    case default:
        print('Exit')