user_input=input('Enter Weather: ')

match user_input:
    case 'sunny':
        print('Wear sunglasses')
    case 'rainy':
        print('Carry an umbrella')
    case 'cloudy':
        print('Weather may change')
    case 'snowly':
        print('Wear warm clothes')
    case _:
        print('Unknown Weather')