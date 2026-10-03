

user_nav=int(input('Enter Your Choice: '))

match user_nav:
    case 1:
        print('Wi-Fi Selected')
    case 2:
        print('Bluetooh Selected')
    case 3:
        print('Mobile Data Selected')
    case 4:
        print('Airplane Mode Selected')
    case default:
        print('Exit')