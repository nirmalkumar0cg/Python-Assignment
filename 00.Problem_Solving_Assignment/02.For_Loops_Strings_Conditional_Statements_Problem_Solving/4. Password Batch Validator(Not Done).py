# Take passwords for 5 users using a for loop.

# For every password, check:

# Minimum length of 8.
# At least one uppercase letter.
# At least one lowercase letter.
# At least one digit.
# At least one special character.
# Print "Strong", "Medium", or "Weak" based on the number of conditions satisfied.

for password in range(5):
    user_pass=input("Enter Your Password: ").strip()
    length_of_pass=len(user_pass)
        