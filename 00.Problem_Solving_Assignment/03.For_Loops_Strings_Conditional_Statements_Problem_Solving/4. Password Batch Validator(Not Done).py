# Take passwords for 5 users using a for loop.

# For every password, check:

# Minimum length of 8.
# At least one uppercase letter.
# At least one lowercase letter.
# At least one digit.
# At least one special character.
# Print "Strong", "Medium", or "Weak" based on the number of conditions satisfied.

sp_char = '!@#$%^&*()_+'
has_upper = False
has_lower = False
has_digit = False
has_spchar = False
score = 0
count= 0
for password in range(5):
    user_pass=input("Enter Your Password: ").strip()
    length_of_pass=len(user_pass)
    if length_of_pass >= 8:
        for char in user_pass:
            if char == char.isupper():
                has_upper = True
                count+=1
            else:
                print('At least one uppercase letter required')
            if char == char.islower():
                has_lower = True
                count+=1
            else:
                print('At least one lowercase letter required')
            if char == char.isdigit():
                has_digit = True
                count+=1
            else:
                print('At least one digit should be in the passsword')
            if char in sp_char:
                has_spchar = True
                count+=1
            else:
                print('At least one sp char is required')
    if count <=2:
        print('weak')
    elif count == 3:
        print('medium')
    else:
        print('Strong')
        