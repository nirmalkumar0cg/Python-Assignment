user_input = input("Enter A Word:")
count = 0
for i in user_input:
    if i.isupper():
        count += 1
print(count)