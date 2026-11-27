# Questions
# 1. Add Two Numbers
# Create a lambda function that accepts two numbers and returns their sum.

# Sample values: 10, 20
# Expected output: 30

# sum = lambda x,y : x+y

# print(sum(10,20))

# 2. Find the Square
# Create a lambda function that accepts one number and returns its square.

# Sample value: 6
# Expected output: 36

# square = lambda x : x**2
# print(square(2))
    
# 3. Find the Cube
# Create a lambda function that accepts one number and returns its cube.

# Sample value: 3
# Expected output: 27

# cube = lambda x : x**3
# print(cube(2))

# 4. Check Even or Odd
# Create a lambda function that accepts a number and returns "Even" if the number is even, otherwise returns "Odd".

# Sample value: 7
# Expected output: "Odd"

# parity = lambda x : 'Even' if x % 2 == 0 else 'Odd'

# print(parity(3))

# 5. Find the Greater Number
# Create a lambda function that accepts two numbers and returns the greater number.

# Sample values: 45, 32
# Expected output: 45

# greater_num = lambda x,y : x if x>y else y

# print(greater_num(99,5))

# 6. Convert Celsius to Fahrenheit
# Create a lambda function that accepts a temperature in Celsius and converts it to Fahrenheit.

# Use this formula:

# Fahrenheit = (Celsius * 9/5) + 32

# Sample value: 25
# Expected output: 77.0

# c_to_f= lambda x: (x*9/5)+32

# print(c_to_f(25))

# 7. Calculate the Length of a String
# Create a lambda function that accepts a string and returns the number of characters in it.

# Sample value: "Python"
# Expected output: 6

# len_of_string = lambda x : len(x)

# print(len_of_string('Python'))

# 8. Convert a String to Uppercase
# Create a lambda function that accepts a string and returns the string in uppercase.

# Sample value: "hello world"
# Expected output: "HELLO WORLD"

# convert_up = lambda x : x.upper()

# print(convert_up('hello world'))

# 9. Find the Last Character
# Create a lambda function that accepts a non-empty string and returns its last character.

# Sample value: "Coding"
# Expected output: "g"

# last_ch = lambda x : x[-1]

# print(last_ch('Coding'))

# 10. Calculate the Final Price
# Create a lambda function that accepts the original price and discount percentage. Return the final price after applying the discount.

# Formula:

# Final Price = Original Price - (Original Price * Discount / 100)

# Sample values: Original price = 1000, Discount = 10
# Expected output: 900.0

# final_price = lambda x,y: x-(x*y/100)

# print(final_price(1000,10))