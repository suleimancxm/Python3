
passwd = input("Password: ")
while True:

    repeat_passwd = input("Repeat password: ")
    if passwd == repeat_passwd:
        break
    print("They do not match!") 
print("User account created!")
    