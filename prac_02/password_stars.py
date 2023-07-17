
"""
ask user for pw
check if meet min length
if not met reinput
if met output pw as *
"""

MINIMUM_LENGTH = 6
password_length = 0

while password_length < MINIMUM_LENGTH:
    print("Please input the desired password")
    print("Password must be ",MINIMUM_LENGTH," characters or more")
    user_password = input(">>>")
    password_length = len(user_password)
    if password_length >=MINIMUM_LENGTH:
        print("*"*password_length)
        break
    else:
        print("password length is too short")
