"""
-1000 start
-randint 10-20 & 5-25
-output
"""
# Imports
from time import *
from random import *

# Vars
birth = ""
death = ""


# Defines
def main(birth, death):
    gopher_population = 1000

    print("Welcome to the Gopher Population Simulator!\nStarting population: {start_pop}\nYear 1".format(
        start_pop=gopher_population))
    create_spacing()
    for x in range(9):
        # birth amount
        birth = calculate_birth(birth, gopher_population)

        # death amount
        death = calculate_death(death, gopher_population)

        # current population
        gopher_population = gopher_population + birth - death
        print("{birth} gophers were born. {death} died.".format(birth=birth, death=death))
        print("population: {pop}".format(pop=gopher_population))
        print("Year {yr}".format(yr=x + 2))
        create_spacing()

        sleep(.5)  # delay


def calculate_birth(birth, gopher_population):
    birth_percent = randint(10, 20)
    birth_percent /= 100
    birth = round(gopher_population * birth_percent)

    return (birth)


def calculate_death(death, gopher_population):
    death_percent = randint(5, 25)
    death_percent /= 100
    death = round(gopher_population * death_percent)

    return (death)


def create_spacing():
    print("\n\n")


# Main cmd
main(birth, death)
