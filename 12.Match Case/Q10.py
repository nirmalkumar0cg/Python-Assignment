user_input=input('Enter payment method: ')

match user_input:
    case 'upi':
        print('upi Payment Selected')
    case 'card':
        print(' card Payment Selected')
    case 'cash':
        print('cash Payment Selected')
    case 'wallet':
        print( 'wallet Payment Selected')
    case _:
        print('Payment Selected')
        
        