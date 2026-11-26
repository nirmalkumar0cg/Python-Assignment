# 12. Vowel-Consonant Battle
# Take a sentence.

# Count vowels and consonants.

# Then:

# Print "Vowels Win" if vowels are greater.
# Print "Consonants Win" if consonants are greater.
# Print "Draw" if equal.
# Also print the frequency of each vowel.

user_sentence = input('Enter Your Sentence: ').lower() #.split()

vowel_count = 0
consonant_count = 0
# n= 0
for char in user_sentence:#[n]
    if char in 'aeiou':
        vowel_count+=1
    if char in 'bcdfghjklmnpqrstvwxyz':
        consonant_count+=1
# n+=1
        
if vowel_count > consonant_count:
    print('Vowel Wins','Vowel Count=>',vowel_count)
elif consonant_count > vowel_count:
    print('Consonant Wins','Consonant Count=>',consonant_count)
elif consonant_count == vowel_count:
    print('Draw')