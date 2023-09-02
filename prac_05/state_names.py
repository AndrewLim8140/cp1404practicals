"""
 CP1404/CP5632 Practical
 State names in a dictionary
 File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
##print(CODE_TO_NAME)

for i in range(0,len(CODE_TO_NAME)):
    state_abbreviations=list(CODE_TO_NAME.keys())[i]
    state_long_ver=CODE_TO_NAME.get(state_abbreviations)
    print(f"{state_abbreviations:<3} is {state_long_ver:<}")

state_code = input("Enter short state: ").upper()

##while state_code != "":
##    state_code = state_code.upper()
##    if state_code in CODE_TO_NAME:
##        print(f"{state_code:<3} is {CODE_TO_NAME[state_code]:<}")
##    else:
##        print("Invalid short state")
##    state_code = input("Enter short state: ")

while state_code != "":

    try :
        print(f"{state_code:<3} is {CODE_TO_NAME[state_code]:<}")


    except KeyError:
        print('invalid short state')

    state_code = input("Enter short state: ").upper()

