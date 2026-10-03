# Q33. Travel Booking System
# Create a travel booking system.

# Select transport:

# 1 → Flight
# 2 → Train
# 3 → Bus
# Then show options:

# Flight:

# 1 → Economy
# 2 → Business
# Train:

# 1 → Sleeper
# 2 → AC
# Bus:

# 1 → Ordinary
# 2 → Volvo
# Use nested match-case.

transport = int(input('----Travel Booking System----\n1.Flight\n2.Train\n3.Bus\n: '))

match transport:
    case 1:
        option = int(input('----Flight Options----\n1.Economy\n2.Business\n: '))
        match option:
            case 1:
                print("Economy class selected")
            case 2:
                print("Business class selected")
    case 2:
        option = int(input('----Train Options----\n1.Sleeper\n2.AC\n: '))
        match option:
            case 1:
                print("Sleeper class selected")
            case 2:
                print("AC class selected")
    case 3:
        option = int(input('----Bus Options----\n1.Ordinary\n2.Volvo\n: '))
        match option:
            case 1:
                print("Ordinary bus selected")
            case 2:
                print("Volvo bus selected")