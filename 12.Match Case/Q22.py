# Q22. Unit Converter
# Create a unit conversion menu:

# 1 → Kilometers to Meters
# 2 → Meters to Kilometers
# 3 → Kilograms to Grams
# 4 → Grams to Kilograms

choice = int(input('What Do You Want To Do?\n1.Kilometers to Meters\n2.Meters to Kilometers\n3.Kilograms to Grams\n4.Grams to Kilograms\n: '))

match choice:
    case 1:
        km=float(input('Enter The Distance In Kilometers: '))
        print('Distance in Meters=',km*1000)
    case 2:
        m=float(input('Enter The Distance In Meters: '))
        print('Distance in Kilometers=',m/1000)
    case 3:
        kg=float(input('Enter The Weight In Kilograms: '))
        print('Weight in Grams=',kg*1000)
    case 4:
        g=float(input('Enter The Weight In Grams: '))
        print('Weight in Kilograms=',g/1000)
    case _:
        print('Enter A Valid Range')