from prac_06.guitar import Guitar
from datetime import *

# variables
guitars = []
guitar_stats = []
max_cost_length = 0
max_name_length = 0
counter = 0

print('My guitars!')
guitar_name=input('Name: ')
guitar_year=input('Year: ')
guitar_cost=input('Cost: $')
print(f'{guitar_name} ({guitar_year}) : ${guitar_cost} added.')

current_year = str(date.today())
current_year = int(current_year[:4])

while guitar_name != '':
    guitar_year = int(guitar_year)
    guitar_cost = float(guitar_cost)
    guitar_cost_rounded = str(guitar_cost).split('.')
    guitar_cost_rounded = guitar_cost_rounded[0]

    if len(guitar_name) > max_name_length:
        max_name_length = len(guitar_name)
    if len(guitar_cost_rounded) > max_cost_length:
        max_cost_length = len(guitar_cost_rounded)

    current_guitar = Guitar(guitar_name,guitar_year,guitar_cost)
    guitar_age = current_guitar.get_age(current_year)
    is_vintage = current_guitar.is_vintage()

    if is_vintage == True:
        is_vintage = '(vintage)'
    else:
        is_vintage = ''

    guitar_stats.extend([guitar_name,guitar_year,guitar_cost,is_vintage])
    guitars.append(guitar_stats)
    guitar_stats = []



        # User inputs
    guitar_name = input('Name: ')
    if guitar_name == '':
        break
    guitar_year = input('Year: ')
    guitar_cost = input('Cost: $')
    print(f'{guitar_name} ({guitar_year}) : ${guitar_cost} added.')

print('These are my guitars:')
for guitar in guitars:
    counter += 1
    print(f'Guitar {counter} : {guitar[0]:>{max_name_length}} ({guitar[1]}), worth $ {guitar[2]:>{max_cost_length},.2f} {guitar[3]}')