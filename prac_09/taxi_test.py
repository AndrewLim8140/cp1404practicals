from prac_09.taxi import Taxi

# initialise prius 1 with datas
taxi = Taxi('Prius 1',100)

# 1st trip -40km
travel = taxi.drive(40)

print(taxi)
print('current fare :',taxi.get_fare())

# start new fare
taxi.start_fare()

# 2nd trip -100km
travel = taxi.drive(100)

print(taxi)
print('current fare :',taxi.get_fare())

