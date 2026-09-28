# 12.
# Take n from the user and print only the odd numbers from 1 to n

n = int(input("Enter The Range You want from 1 to: "))
i=1
while i <= n:
    if i % 2!=0:
        print(i)
    i+=1