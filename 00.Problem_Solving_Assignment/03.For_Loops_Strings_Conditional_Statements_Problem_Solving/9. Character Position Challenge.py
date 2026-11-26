# Take a string.

# For every character, print:

# Character
# Position
# Whether position is even or odd
# Whether character is vowel, consonant, digit, or special character
# At the end, count how many characters fall into each category.

    
user_string=input("Enter Your String: ").upper()
vowel = 0
consonant = 0
digit = 0
sp_char = 0
        
for i in range(0,len(user_string)):
    if i % 2 == 0:
        print(user_string[i],'Even Position')
    else:
        print(user_string[i],'Odd Position')
        
for char in user_string:
    if char in 'AEIOU':
        print(f"Vowel's-{char}")
        vowel+=1
    if char in 'BCDFGHJKLMNPQRSTVWXYZ':
        print(f"Consonant-{char}")
        consonant+=1
    if char in '1234567890':
        print(f'Digit-{char}')
        digit += 1
    if char in '!@#$%^&*()':
        print(f"Special Character-{char}")
        sp_char+=1

    

print('Vowel Count=',vowel)
print('Consonant Count=',consonant)
print('Digit Count=',digit)
print('Special Character=',sp_char)
    
    
