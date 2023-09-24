# obtaining user's input
score = float(input("Enter score: ")
              )
# if number isnt within 0 to 100
if score > 100 or score < 0:
    print("Invalid Score")
# computation of scores
elif score > 90:
    print("Excellent")
elif score > 50:
    print("Passable")
else:
    print("Bad")
