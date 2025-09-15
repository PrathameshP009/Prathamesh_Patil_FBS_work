correct_userid = "admin"
correct_password = "1234"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")
    if userid == correct_userid and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect User ID or Password , please try again.")
        attempts += 1

if attempts == max_attempts:
    print("Too many failed attempts...")