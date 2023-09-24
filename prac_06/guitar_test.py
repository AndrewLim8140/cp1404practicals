from prac_06.guitar import Guitar
from datetime import *

"""Get today date"""
current_year = str(date.today())
current_year = int(current_year[:4])


gibson = Guitar('Gibson L-5 CES',1922,16035.40)
another_guitar = Guitar('Another guitar',2013,200)


print('expected : 101. Got : ',gibson.get_age(current_year))
print('expected : 10. Got : ',another_guitar.get_age(current_year))

print('expected : True. Got : ',gibson.is_vintage())
print('expected : False. Got : ',another_guitar.is_vintage())