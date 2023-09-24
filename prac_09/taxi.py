"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car



class Taxi(Car):
    # taxi fees
    price_per_km = 1.23

    """Specialised version of a Car that includes fare costs."""
    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)

        self.current_fare_distance = 0

    def __str__(self, price_per_km=price_per_km):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${price_per_km:.2f}/km"

    def get_fare(self,price_per_km=price_per_km):
        """Return the price for the taxi trip."""
        # rounding to nearest 10c
        return round(price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven