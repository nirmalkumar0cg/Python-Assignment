# 13.
# Take n from the user and print all numbers from 1 to n that are divisible by 3

n = int(input("Enter The Range You want from 1 to: "))

i=1

while i <= n:
    if i % 3==0:
        print(i)
    i+=1