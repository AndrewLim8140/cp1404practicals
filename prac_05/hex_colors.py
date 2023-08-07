"""
___Sequence___
Request color
color.upper
refernce to dict
try Print hexa code
if error reinput color
"" to exit
"""

COLORS_TO_HEXA = {"amethyst": "#9966cc", "aqua": "#00ffff", "asparagus": "#87a96b", "barn red": "#7c0a02",
                  "bitter lemon": "#cae00d", "black coffee": "#3b2f2f", "boysenberry": "#873260",
                  "british racing green": "#004225", "fuzzy wuzzy": "#87421f", "papayawhip": "#ffefd5"}

""" Printing menu """
for i in range(0, len(COLORS_TO_HEXA)):
    color_name = list(COLORS_TO_HEXA.keys())[i]
    hexa_code = COLORS_TO_HEXA.get(color_name)
    print(f"{color_name:<20} is {hexa_code:<}")

print("")
color_input = input("Enter your desired color :").lower()

while color_input != '':

    try:
        print(f"The hexa code for {color_input} is {COLORS_TO_HEXA[color_input]}")

    except KeyError:
        print("Invalid color")

    color_input = input("Enter your desired color :").lower()
