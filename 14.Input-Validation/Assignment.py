# Part A — Intermediate Problems
# Problem 1: Valid Marks
# Ask the user to enter marks between 0 and 100, inclusive. If the marks are outside this range, keep asking until valid marks are entered. Finally, display the accepted marks.

# user_marks = int(input('Enter Your Marks: '))
# if user_marks < 0 or user_marks > 100:
#     print('Invalid Marks. Try Again')
#     while user_marks < 0 or user_marks > 100:
#         user_marks=int(input('Enter Your Marks: '))
#         if user_marks < 0 or user_marks > 100:
#             print('Invalid Marks. Try Again')
#         else:
#             print('Valid Marks')
        

# Problem 2: Positive Integer
# Keep asking the user to enter an integer until they enter a number greater than 0. Display the accepted number.

# user_num = int(input('Enter A Number: '))

# while user_num < 0:
#     user_num=int(input('Enter A Number: '))
#     if user_num > 0:
#         print('Number Greater Than 0 Ending Loop...')
#         break


# Problem 3: Age Validation
# Ask the user to enter their age. Accept ages from 0 through 120. If the age is outside this range, display an error message and ask again.

# user_age = int(input('Enter Your Age: '))
# condtion = user_age < 0 or user_age > 120
# while condtion == True:
#     print('Error, Try Again...')
#     user_age=int(input('Enter Your Age: '))
#     if 0<= user_age <= 120:
#         print('Valid Age')
#         break

# Problem 4: Menu Choice
# Display this menu repeatedly until the user enters a valid choice:

# 1. View profile
# 2. Edit profile
# 3. Settings
# 4. Exit
# Accept only the integers 1, 2, 3, and 4. Display the selected option after valid input.

# menu = int(input('===Menu===\n1. View Profile\n2. Edit Profile\n3. Settings\n4. Exit\nEnter Your Choice: '))

# while menu <=0 or menu > 4:
#     menu = int(input('===Menu===\n1. View Profile\n2. Edit Profile\n3. Settings\n4. Exit\nEnter Your Choice: '))
#     match menu:
#         case 1:
#             print('Viewing Profile...')
#         case 2:
#             print('Editing Profile...')
#         case 3:
#             print('Opening Settings...')
#         case 4:
#             print('Exiting')

# Problem 5: Password Length
# Keep asking the user for a password until it contains at least eight characters. Leading and trailing spaces should not count toward the password length. Display a success message after valid input.

# user_pass = input('Enter Password: ').strip()
# while len(user_pass) < 8:
#     user_pass = input('Enter Password: ').strip()
#     if len(user_pass) >= 8:
#         print('Success')
#         break    

# Problem 6: Temperature Range
# Ask the user to enter a temperature between -20 and 45, inclusive. Reject values outside the range and repeat the prompt until the input is valid.

# user_temp = int(input('Enter The Temp: '))
# if user_temp < -20 or user_temp > 45:
#     while user_temp < -20 or user_temp > 45:
#         user_temp=int(input('Enter The Temp: '))
#         if user_temp < -20 or user_temp > 45:
#             print('Enter Valid Temp Range...')
#         else:
#             print('Valid Temp Aborting Loop...')
    
# Problem 7: Withdrawal Validation
# Start with a bank balance of ₹5,000. Ask the user for a withdrawal amount. Reject the amount if it is zero, negative, or greater than the available balance. Keep asking until a valid amount is entered, then update and display the balance.

# bank_balance = 5000
# withdrawal_amt = int(input('Enter The Amount You Want To Widthdraw: '))
# while withdrawal_amt < 0 or withdrawal_amt > 5000 or withdrawal_amt==0:
#     withdrawal_amt = int(input('Enter The Amount You Want To Withdraw: '))
# else:
#     if 1<= withdrawal_amt <= 5000:
#      print(f'Amount Withdrawn Successfully\n Updated Balance:{bank_balance-withdrawal_amt}')
        

# Problem 8: Username Validation
# Keep asking for a username until it:

# Contains at least five characters after removing leading and trailing spaces.
# Is not empty.
# Does not contain a space inside the username.
# Display the accepted username.

# user_username = input('Enter Your Username: ').strip()
# while len(user_username) < 5 or ' ' in user_username or user_username == '':
#     print('Username must be at least 5 characters long and contain no spaces.')
#     user_username = input('Enter Your Username: ').strip()

# print(f'Accepted username: {user_username}')
        
# Problem 9: Divisible Number
# Keep asking the user for a positive integer that is divisible by both 3 and 5. Reject all other values. Display the accepted number.


#M1

# user_input=int(input('Enter A Number: '))
# while user_input % 3 != 0 or user_input % 5 != 0:
#     user_input=int(input('Enter A Number: '))
#     print('Enter A Number Which is divisible by both 3 and 5')
# print(user_input)

#M2

# while True:
#     user_input=int(input('Enter A Number: '))
#     print('Enter A Number Which is divisible by both 3 and 5')
#     if user_input % 3 == 0 or user_input % 5 == 0:
#         print(user_input)
#         break



# Problem 10: Limited PIN Attempts
# Set a secret PIN to 2468. Allow the user up to three attempts to enter the correct PIN. Stop immediately when the PIN is correct. If all attempts fail, display a message that access is denied.

# secret_pin = 2468

# for i in range(3):
#     user_input=int(input('Enter The PIN: '))
#     if user_input == secret_pin:
#         print('Correct Pin Entered')
#         break
#     else:
#         print('Wrong Pin...')
# else:
#     print('Device Is Locked')


# Problem 11: Number Within a Range
# Keep asking for an integer between 10 and 50, inclusive. After accepting the value, print whether it is even or odd.

# while True:
#     user_input=int(input('Enter A Number: '))
#     if user_input not in range(10,51):
#         print('Enter A Number in range of 10-50')
#     else:
#         break
# if user_input % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
        

# Problem 12: Deposit Validation
# Start with a balance of ₹2,000. Ask the user for a deposit amount. Accept only positive amounts. Keep asking until a valid amount is entered, then add it to the balance and display the new balance.

# balance = 2000
# deposit_amt = int(input('Enter The Amount Of Money You Want to Deposit: '))
# if deposit_amt < 0:
#     while deposit_amt < 0:
#         print('Enter A Valid Deposit Amount...')
#         deposit_amt=int(input('Enter The Amount Of Money You Want To Deposit: '))
#     print(balance+deposit_amt)


# Part B — Challenging Problems
# Problem 13: Integer Between 1 and 100
# Keep asking the user for an integer between 1 and 100, inclusive. Reject numbers outside the range and continue until a valid number is entered.

# while True:
#     user_input=int(input('Enter A Number In Range 1-100: '))
#     if user_input not in range(1,101):
#         print('Cant You Read?...')
#     else:
#         break
        
# print(user_input)
        
        


# Problem 14: Marks and Result
# Keep asking the user for marks between 0 and 100, inclusive. After accepting valid marks, display:
# Distinction for marks of 75 or more.
# First Class for marks of 60 to less than 75.
# Pass for marks of 35 to less than 60.
# Fail for marks below 35.
# Do not calculate the result until the marks are valid.


# while True:
#     user_marks = int(input('Enter The Marks Between 0-100: '))
#     if user_marks >=0 and user_marks <= 100:
#         if user_marks >= 75:
#             print('Distinction')
#             break
#         elif user_marks >=60 and user_marks < 75:
#             print('First Class')
#             break
#         elif user_marks >= 35 and user_marks < 60:
#             print('Pass')
#             break
#         else:
#             print('Fail')
#             break
            
#     else:
#         print('Enter Valid Marks...')





# Problem 15: Username and Password Validation
# Ask the user for a username and password. Repeat the prompts until both fields meet all rules:

# Username must contain at least five characters after trimming outer spaces.
# Username must not contain internal spaces.
# Password must contain at least eight characters.
# Password must not be blank or consist only of spaces.
# Display a success message only when both fields are valid.

# while True:
#     user_username=input('Enter Your Username: ').strip()
#     while len(user_username) < 5:
#         print('Username should be 5 or more characters....')
#         user_username=input('Enter Your Username: ').strip()
#     user_password=input('Enter Your Password: ').strip()
#     while len(user_password) < 8 or user_password == ' ':
#         print('The Password Length Should Be 8 or more and it should not be blank....')
#         user_password=input('Enter The Password: ').strip()
#     else:
#         break
# print('Success')
        





# Problem 16: Calculator Input Validation
# Build a calculator that asks for two numbers and an operator (+, -, *, or /).

# Validate the following:

# The operator must be one of the four supported operators.
# Division by zero must be rejected.
# If the operator is invalid, ask for the operator again.
# If the divisor is zero, ask for the second number again.
# Display the result only when all required values are valid.

# while True:
#     a=int(input('Enter the First Number: '))
#     b=int(input('Enter The Second Number: '))
#     user_operation=int(input('Select the operation you want to perform----\n1.Add(+)\n2.Substraction(-)\n3.Multiplication(*)\n4.Division(/)\n:'))
#     while user_operation not in range(1,5):
#         user_operation=int(input('Select the operation you want to perform----\n1.Add(+)\n2.Substraction(-)\n3.Multiplication(*)\n4.Division(/)\n:'))
#     else:
#         break
                
                
# match user_operation:
#     case 1:
#         print('Result:', a + b)
#     case 2:
#         print('Result:', a - b)
#     case 3:
#         print('Result:', a * b)
#     case 4:
#         while b == 0:
#             print('Enter The Second Number Again Not Zero: ')
#             b=int(input('Enter The Second Number: '))
#         print('Result:', a / b)
        

# Problem 17: Banking Menu
# Create a menu-driven banking program with these options:

# 1. Check balance
# 2. Deposit money
# 3. Withdraw money
# 4. Exit
# Start with a balance of ₹10,000.

# Requirements:

# Keep displaying the menu until the user chooses Exit.
# Reject invalid menu choices.
# Deposits must be greater than zero.
# Withdrawals must be greater than zero and must not exceed the balance.
# Update the balance only after a transaction passes validation.


# balance = 10000
# while True:
#     menu = int(input('===Banking Menu===\n1. Check Balance\n2. Deposit money\n3. Withdraw money\n4. Exit\n: '))
#     if menu > 4:
#         print('Enter A Valid Choice...')
#     if menu <= 4:
#         match menu:
#             case 1:
#                 print(balance)
#             case 2:
#                 deposit = int(input('Enter The Money You Want To Deposit: '))
#                 while deposit <=0:
#                     print('Enter A Valid Deposit Amount...')
#                     deposit = int(input('Enter The Money You Want To Deposit: '))
#                 else:
#                     balance = balance+deposit
#                     print(balance)
#             case 3:
#                 withdraw = int(input('Enter The Amt Of Money You Want To Withdraw: '))
#                 while withdraw > balance or withdraw <= 0:
#                     print('Insufficent Balance...Try Again')
#                     withdraw = int(input('Enter The Amt Of Money You Want To Withdraw: '))
#                 else:
#                     balance = balance-withdraw
#                     print(balance)
#             case 4:
#                 print('Exiting...')
#                 break
            
            
# Problem 18: Validate Month and Day
# Ask the user to enter a month number from 1 to 12 and a day number from 1 to 31. Keep asking until both values are within their individual ranges.

# user_month_number = int(input('Enter the month number (1-12): '))
# while user_month_number < 1 or user_month_number > 12:
#     print('Enter a valid month number.')
#     user_month_number = int(input('Enter the month number (1-12): '))

# user_day_number = int(input('Enter the day number (1-31): '))
# while user_day_number < 1 or user_day_number > 31:
#     print('Enter a valid day number.')
#     user_day_number = int(input('Enter the day number (1-31): '))

# print(user_month_number, user_day_number)




# Problem 19: Product Quantity and Price
# Ask the user for a product quantity and unit price.

# Requirements:
# Quantity must be a positive integer.
# Unit price must be greater than zero.
# Repeat only the prompt for the field that has an invalid value.
# Calculate and display the total cost after both values are valid.

quantity = int(input('Enter product quantity: '))
while quantity <= 0:
    print('Quantity must be a positive integer.')
    quantity = int(input('Enter product quantity: '))

unit_price = float(input('Enter unit price: '))
while unit_price <= 0:
    print('Unit price must be greater than zero.')
    unit_price = float(input('Enter unit price: '))

total_cost = quantity * unit_price
print(f'Total cost: ₹{total_cost:.2f}')


# Problem 20: Safe Average Calculator
# Ask the user how many numbers they want to enter. The count must be an integer from 1 to 20. Then ask for that many numeric values and calculate their average.

# Requirements:
# Keep asking until the count is valid.
# If a value is outside any range specified by your instructor, ask for that value again.
# Display the average after all required values have been entered.

count = int(input('How many numbers do you want to enter? (1-20): '))
while count < 1 or count > 20:
    print('Count must be between 1 and 20.')
    count = int(input('How many numbers do you want to enter? (1-20): '))

numbers = []
for i in range(count):
    value = float(input(f'Enter number {i + 1}: '))
    numbers.append(value)

average = sum(numbers) / count
print(f'Average: {average}')


# Problem 22: Input Validation Without break
# Solve the following task without using break:
# Keep asking for an integer from 1 to 10 until a valid value is entered.
# Requirement: Use a suitable loop condition and update the condition so the loop ends when valid input is received.

valid_number = False
while not valid_number:
    user_number = int(input('Enter an integer from 1 to 10: '))
    valid_number = 1 <= user_number <= 10
    if not valid_number:
        print('Invalid input. Please enter a value from 1 to 10.')

print(f'Valid number entered: {user_number}')


# Problem 23: Three Valid Scores
# Ask the user to enter three scores, each between 0 and 100, inclusive. Validate each score separately and repeat only the invalid score prompt. After all three scores are valid, display the total and average.

scores = []
for i in range(3):
    score = int(input(f'Enter score {i + 1} (0-100): '))
    while score < 0 or score > 100:
        print('Score must be between 0 and 100.')
        score = int(input(f'Enter score {i + 1} (0-100): '))
    scores.append(score)

total_score = sum(scores)
average_score = total_score / 3
print(f'Total score: {total_score}')
print(f'Average score: {average_score}')


# Problem 24: ATM Withdrawal With Denomination Rules
# Start with a balance of ₹10,000. Ask the user for a withdrawal amount.

# Requirements:
# Amount must be positive.
# Amount must not exceed the balance.
# Amount must be a multiple of ₹100.
# Repeat until a valid amount is entered.
# Deduct the amount only after all validation rules pass.
# Display the withdrawn amount and remaining balance.

balance = 10000
valid_withdrawal = False

while not valid_withdrawal:
    withdrawal_amount = int(input('Enter the withdrawal amount: '))

    if withdrawal_amount <= 0:
        print('Amount must be positive.')
    elif withdrawal_amount > balance:
        print('Amount must not exceed the balance.')
    elif withdrawal_amount % 100 != 0:
        print('Amount must be a multiple of ₹100.')
    else:
        valid_withdrawal = True

balance -= withdrawal_amount
print(f'Withdrawn amount: ₹{withdrawal_amount}')
print(f'Remaining balance: ₹{balance}')

# Problem 21: Stronger Password Rules
# Keep asking for a password until all conditions are met:

# At least eight characters.
# At least one uppercase letter.
# At least one lowercase letter.
# At least one digit.
# No whitespace characters.
# Display which rules are not satisfied after each invalid attempt.