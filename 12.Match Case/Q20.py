# Q20. Simple Calculator
# Take two numbers and an operator:

# +
# -
# *
# /
# Use match-case to perform the selected operation.

num1, num2 = map(int, input('Enter the first and second numbers: ').split())
operator = input('Enter an operator (+, -, *, /) To Exit Type "0": ')

while operator !='0':
    match operator:
        case '+':
            print(num1+num2)
        case '-':
            print(num1-num2)
        case '*':
            print(num1*num2)
        case '/':
            print(num1/num2)
    operator = input('Enter an operator (+, -, *, /) To Exit Type "0": ')

            
