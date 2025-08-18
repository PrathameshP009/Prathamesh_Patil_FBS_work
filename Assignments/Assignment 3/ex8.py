import random
userid = input("Enter userid :")
pass1 = input("Enter password :")

if (userid == "FBS" and pass1=="fbs123"):
    captcha = random.randint(1000,9999)
    print("Captcha :",captcha)
    
    user_captcha= int(input("Enter captcha:"))
    if (captcha == user_captcha):
        print("Captcha is Correct")
        print("Successfully login ")
    else:
        print("Captcha is incorrect , please enter right captcha")
else:
    print("Incorrect password")
