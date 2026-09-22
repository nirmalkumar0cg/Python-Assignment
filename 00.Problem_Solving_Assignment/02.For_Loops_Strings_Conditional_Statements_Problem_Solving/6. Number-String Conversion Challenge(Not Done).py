# 6. Number-String Conversion Challenge
# Take 5 numbers from the user.

# For each number:

# Convert it to a string.
# Examine every digit using a loop.
# Count even and odd digits.
# Print which type occurs more.
# If equal, print "Equal".
count_even = 0
count_odd = 0
for user_num in range(5):
    user_num = int(input("Enter Numbers: "))
    string_num = str(user_num)
    for examine in string_num:
        if user_num % 2 == 0:
            count_even+=1
        elif user_num % 2 != 0:
            count_odd+=1

if count_even > count_odd:
    print("Even Is More")
elif count_odd > count_even:
    print("Odd Is More")
elif count_odd == count_even:
    print("Equal")