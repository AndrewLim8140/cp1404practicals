"""
-ask for no. scores
-generate said scores
-export results to txt
"""
from random import randint

outcome = ""

from random import *
def main(outcome):
        # Creating / Accessing results.txt
    with open('results.txt', 'a') as f:

            # obtaining user's input
        score_count = int(input("Enter the desired number of scores :"))

        for x in range(score_count):
            generated_score = randint(0,100)
            outcome = decide_outcome(outcome,generated_score)
            final_output = ("{score} is an {result} mark \n").format(score = generated_score, result = outcome)
            f.write(final_output)


def decide_outcome(outcome,generated_score):
    if generated_score > 100 or generated_score < 0:
        outcome = "Invalid Score"
    # computation of scores
    elif generated_score > 90:
        outcome = "Excellent"
    elif generated_score > 50:
        outcome = "Passable"
    else:
        outcome = "Bad"
    return outcome


main(outcome)
