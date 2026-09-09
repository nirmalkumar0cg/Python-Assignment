client_username = input("Enter Your Username:") 
client_pass = input("Enter Your Password:")
if client_username == "admin":
    if client_pass == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("User not found")