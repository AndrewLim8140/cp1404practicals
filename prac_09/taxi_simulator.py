from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
current_cost = 0.00

MENU = '\n(C)hoose taxi \n(D)rive\n(Q)uit \n'

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
taxi = None


user_action = input(f'Total trip cost :${current_cost}\n{MENU}\n Enter desired action :').upper()
while user_action != 'Q':

    # List taxis
    if user_action == 'C':
        taxi = None
        counter = 0
        print('Available Taxis :')
        for taxi_list in taxis:
            print(f'{counter} - {taxi_list}')
            counter += 1

        user_taxi = int(input('Choose Taxi :'))
        while user_taxi > (len(taxis)-1) or user_taxi < 0:
            print('Invalid choice')
            user_taxi = int(input('Choose Taxi :'))

        user_taxi = int(user_taxi)


        while taxi is None:
            try:
                taxi = taxis[user_taxi]

                taxi_components = str(taxi_list).split(',')
                taxi_name = taxi_components[0]
            except IndexError:
                print('Invalid number')



    if user_action == 'D':
        if taxi is not None:
            taxi.drive(0)
            distance = int(input('Input distance :'))
            taxi.drive(distance)
            current_cost = taxi.get_fare()
            print(f'Your {taxi_name} trip costed you {taxi.get_fare()}')
        else:
            print('You need to choose a taxi first')


    print()
    user_action = input(f'Total trip cost :${current_cost}\n{MENU} \n Enter desired action :').upper()



counter = 0
print(f'Total trip cost :${current_cost}\nThe current status of the taxis are :')
for taxi_list in taxis:
    print(f'{counter} - {taxi_list}')
    counter += 1