import random

from prac_09.car import Car
from random import *
class UnreliableCar(Car):
    def __init__(self,name,fuel,reliability):

        # inherit __init__ from car.py
        super().__init__(name,fuel)

        # setting reliability
        self.reliability = reliability
        # self.reliability = random.uniform(1,100)

        self.distance_traveled = 0

    def __str__(self):
        return f"{super().__str__()}, reliability={self.reliability}"
    def drive(self, distance):
        # if reliability check
        if self.reliability > (uniform(1,100)):
            # overwritting car's drive
            self.distance_traveled = super().drive(distance)

        else:
            self.distance_traveled = 0

        return self.distance_traveled
