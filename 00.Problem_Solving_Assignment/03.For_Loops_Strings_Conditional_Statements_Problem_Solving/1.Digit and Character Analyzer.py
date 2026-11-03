# 1. Digit and Character Analyzer
# Take a string containing letters, digits, spaces, and special characters.

# Using a for loop:

# Count uppercase letters.
# Count lowercase letters.
# Count digits.
# Count spaces.
# Count special characters.
# Print which category has the highest count.
# If two or more categories have the same highest count, print "Tie".



string = "rmal123"
count_uppercase = 0
count_lowercase = 0
count_digit = 0
count_spaces = 0
count_spchar = 0

for i in string:
    if i.isupper():
        count_uppercase += 1
    elif i.islower():
        count_lowercase += 1
    elif i.isdigit():
        count_digit += 1
    elif i == " ":
        count_spaces += 1
    else:
        count_spchar += 1

if count_uppercase > count_lowercase and count_uppercase > count_digit and count_uppercase > count_spaces and count_uppercase > count_spchar:
    print("Count Of Upper Case Is Highest")
elif count_lowercase > count_uppercase and count_lowercase > count_digit and count_lowercase > count_spaces and count_lowercase > count_spchar:
    print("Count Of Lower Case Is Highest")
elif count_digit > count_uppercase and count_digit> count_lowercase and count_digit > count_spaces and count_digit>count_spchar:
    print("Count Of Digit Is Highest")
elif count_spaces > count_uppercase and count_spaces>count_lowercase and count_spaces > count_digit and count_spaces>count_spchar:
    print("Count Of Spaces Is Highest")
elif count_spchar > count_uppercase and count_spchar > count_lowercase and count_spchar > count_digit and count_spchar > count_spaces:
    print("Count Of Special Character Is Highest")
else:
    print("Tie")