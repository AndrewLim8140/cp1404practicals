from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi('silver taxi',100,2)

taxi.drive(18)

print(taxi)
print('Total Fare :',taxi.get_fare())