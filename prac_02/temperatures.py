MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_to_fahrenheit():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def convert_to_celsius():
    global celsius
    celsius = (5 / 9) * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        convert_to_fahrenheit()
        print(f"Result: {fahrenheit:.2f} F")

    elif choice == "F":
        fahrenheit = float(input("Fahrenheit :"))
        convert_to_celsius()
        print(f"Results: {celsius:2f}Degrees")

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
