"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    count_length = 0
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    """ Checking password length """
    password_length = len(password)
    if MIN_LENGTH <= password_length <= MAX_LENGTH:
        count_length = 1

    """ Checking characters """
    for char in password:
        if char.isdigit() == True:
            count_digit = 1

        elif char.isupper() == True:
            count_upper = 1

        elif char.islower() == True:
            count_lower = 1

        for symbol in SPECIAL_CHARACTERS:
            if char == symbol:
                count_special = 1
    ]
    if (count_length, count_digit, count_upper, count_lower, count_special) == (1, 1, 1, 1, 1):
        print("PASS")
    return True


main()
