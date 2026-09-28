# 17.
# Take n from the user and calculate the sum of all even numbers from 1 to n
n = int(input("Enter The Range You want from 1 to: "))
i = 1
count = 0
while i <= n:
    if i % 2 == 0:
        count=count+i
    i+=1
print(count)