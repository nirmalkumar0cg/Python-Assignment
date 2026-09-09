user_input = input("Enter The Word You Want To Know How Many Times A Was Printed:")
cont = 0
for i in user_input:
    if i == "a":
     cont = cont+1
print(f"{cont}")