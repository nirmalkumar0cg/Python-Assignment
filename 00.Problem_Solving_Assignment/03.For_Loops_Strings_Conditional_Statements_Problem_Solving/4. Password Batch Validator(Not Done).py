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
for password in range(5):
    user_pass=input("Enter Your Password: ").strip()
    length_of_pass=len(user_pass)
    if length_of_pass >= 8:
        for char in user_pass:
            if char in char.isupper():
                has_upper = True
            if char in char.islower():
                has_lower = True
            if char in char.isdigit():
                has_digit = True
                