"""
-generate txt with 15 temps
-convert txt to celsius
"""
# _imports
from random import uniform
import time

# _vars
celsius = ''
data = ""
databank = []
final = ""


def main(final, celsius, data):
    clear_txt()  # Clears input txt from previous text
    generate_temps()  # Generates new random temps in fahrenheit
    f.seek(0)  # Returns to start of input txt

    # Convert incoming str to list and removing \n
    data = str_to_list(data)

    # Converting fahrenheit to celsius
    for x in range(0, 15):
        time.sleep(.25)
        fahrenheit = float(data[x])
        celsius = fahrenheit_to_celsius(fahrenheit, celsius)

        final = final + celsius + "\n"
        print('f :', fahrenheit)
        print('c :', celsius)
        create_spacing()

        # Exporting celsius into txt
    with open('temps_output.txt', "w") as c:
        c.writelines("{celsius}".format(celsius=final))


def generate_temps():
    for x in range(15):
        temp_random = uniform(-200, 200)
        f.write("{temp}\n".format(temp=temp_random))


def create_spacing():
    print("\n\n")


def clear_txt():
    open("temps_input.txt", "w").close


def fahrenheit_to_celsius(fahrenheit, celsius):
    celsius = str((fahrenheit - float(32)) * float((5 / 9)))
    return celsius


def str_to_list(data):
    data = f.read().split('\n')
    return (data)


with open('temps_input.txt', 'a+') as f:
    main(final, celsius, data)


