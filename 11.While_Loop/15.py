# 15.
# Take n from the user and count how many numbers from 1 to n are even.

n = int(input("Enter The Range You want from 1 to: "))
i = 1
count = 0
while i <= n:
    if i % 2==0:
        count+=1
    i+=1
print(count)