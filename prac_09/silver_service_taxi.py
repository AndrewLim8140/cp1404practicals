from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    # additional charges for flagging down
    flagfall = 4.50

    def __init__(self,name,fuel,fanciness):
        super().__init__(name,fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.current_fare_distance = 0

    # def drive(self, distance):
    #     self.current_fare_distance = super().drive(distance)
    #     return self.current_fare_distance

    def get_fare(self,flagfall=flagfall):
        return super().get_fare(price_per_km=self.price_per_km) + flagfall

    def __str__(self, flagfall=flagfall):
        return (f"{super().__str__(price_per_km=self.price_per_km)}, flagfall ={flagfall}")

