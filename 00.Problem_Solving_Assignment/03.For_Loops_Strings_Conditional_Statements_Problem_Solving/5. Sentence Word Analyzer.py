# Take a sentence and examine every word.

# For each word:

# Print its length.
# Print "Short" if length ≤ 3.
# Print "Medium" if length is 4–6.
# Print "Long" if length > 6.
# At the end, print the number of short, medium, and long words.







user_sentence = input("Enter Your Sentence: ").split()

short_count = 0
medium_count = 0
long_count = 0

for word in user_sentence:
    word_length = len(word)

    if word_length <=3:
        print('Short')
        short_count+=1
    elif word_length >=4 and word_length <=6:
        print("Medium")
        medium_count+=1
    else:
        print("Long")
        long_count+=1
print("Short Words Count",short_count)
print("Medium Words Count",medium_count)
print("Long Words Count",long_count)