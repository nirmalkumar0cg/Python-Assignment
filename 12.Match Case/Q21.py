# Q21. Temperature Converter
# Create a converter:

# 1 → Celsius to Fahrenheit
# 2 → Fahrenheit to Celsius
# Take the temperature and perform the selected conversion.

choice = int(input('What Do You Want To Do?\n1.Celcius to Fahrenheit\n2.Fahrenheit To Celsius\n: '))

match choice:
    case 1:
        cel_temp=float(input('Enter The Temp In Celcius: '))
        print('Temperature in Fahrenheit=',(cel_temp*9/5)+32)
    case 2:
        fah_temp=float(input('Enter The Temp In Fahrenheit: '))
        print('Temperature in Celcius=',(fah_temp-32)*5/9)