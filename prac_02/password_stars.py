
"""
ask user for pw
check if meet min length
if not met reinput
if met output pw as *
"""
global MINIMUM_LENGTH

MINIMUM_LENGTH = 6
password_length = 0

def main(password_length):
    while password_length < MINIMUM_LENGTH:
        password_length = get_password(password_length)
        if password_length >= MINIMUM_LENGTH:
            censor_password(password_length)
            break
        else:
            print("password length is too short")


def censor_password(password_length):
    print("*" * password_length)


def get_password(password_length):
    print("Please input the desired password")
    print("Password must be ", MINIMUM_LENGTH, " characters or more")
    user_password = input(">>>")
    password_length = len(user_password)
    return password_length


main(password_length)