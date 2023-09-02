"""
req email-key and name-value
loop till ' '

use func to check if email is known
ask if [name] is yours
"""
names = []
emails_n_names = {}


def main():
    email = input('Email :')
    while email != '':
        name = check_email(email)
        check_name = input(f'Is your name {name}? (Y/N)').upper()
        if (check_name == 'Y') or (check_name == ' '):

            emails_n_names.update({email: name})
        elif check_name == 'N':
            name = input('Name :')
            emails_n_names[email] = name

        email = input('Email :')

    print('')
    for email in emails_n_names:
        name = emails_n_names[email]
        print(f'{name} ({email})')


def check_email(email):
    email = email.split('@')
    name = email[0]
    name = name.split('.')
    name = tuple(name)
    name = " ".join(name)
    return name


main()
