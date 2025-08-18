correct_userid= "FBS"
correct_pass = "fbs@123"

userid = input("Enter userid :")
password = input("enter password :")

if(userid==correct_userid and password ==correct_pass):
    print("Login successful !!!")
else:
    print("Invalid user and pass , enter valid data")