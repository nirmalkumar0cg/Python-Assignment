# Take a sentence.

# For every word:

# Vowel = 2 points.
# Consonant = 1 point.
# Digit = 3 points.
# Special character = 4 points.
# Calculate the score of every word and print the word with the highest score.

# Do not use max().
user_sentence = input("Enter Your Sentence")
words = user_sentence.split()
highest_score = 0
highest_word = ''

for word in words:
    score = 0
    for ch in word:
        if ch in 'aeiou':
            score +=2
        elif ch in 'abcedfghijklmnopqrstuvwxyz':
            score+=1
        elif ch in '1234567890':
            score+=3
        else:
            score+=4
    print(word,"=",score)
    
    if score > highest_score:
        highest_score = score
        highest_word =  word
        
print("highest scoring word",highest_word)
print("Total Score",highest_score)
        
    