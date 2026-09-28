# 16.
# Take n from the user and calculate:

# 1 + 2 + 3 + ... + n

n = int(input("Enter The Range You want from 1 to: "))
i = 1
count = 0
while i <= n:
    count= count+i
    i+=1
print(count)