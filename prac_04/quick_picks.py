from random import *
number_of_picks = int(input("How many quick picks? "))
total_picks=[]

for current_row in range (1,number_of_picks+1):
    numbers=[]
    for i in range(1,7):
        random_number=randint(1,45)
        while random_number in numbers:
            random_number = randint(1,45)
        numbers.append(random_number)   
        numbers.sort()


    total_picks.append(numbers)
    for i in range (0,5):
        number=total_picks[current_row-1][i]
        print(f'{number:>2}',end=' ')
    print('')
    
