from random import *
def main():
    outcome = ""
    # obtaining user's input
    score = float(input("Enter score: ")
                  )
    # if number isnt within 0 to 100
    outcome = decide_outcome(outcome, score)

    print(outcome)

    # generating random score
    score=randint(0,100)
    print("the random score is ",score)
    outcome = decide_outcome(outcome, score)
    print(outcome)

def decide_outcome(outcome, score):
    if score > 100 or score < 0:
        outcome = "Invalid Score"
    # computation of scores
    elif score > 90:
        outcome = "Excellent"
    elif score > 50:
        outcome = "Passable"
    else:
        outcome = "Bad"
    return outcome


main()