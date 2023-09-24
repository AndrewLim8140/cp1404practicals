"""
-req score
-menu loop
    -req score
    -print results
    -print stars
    -quit
        -farewell
    -invalid opts

"""
score = -1
user_action = ""
outcome = ""


def main(score, user_action, outcome):
    while score < 0 or score > 100:
        print('Input your score (0-100)')
        score = int(input('>>>'))
        add_spaceing()

    while user_action != "Q":
        print('(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit')
        user_action = input(">>>").upper()
        add_spaceing()

        # _____ New Score Input _____
        if user_action == "G":
            score = -1
            while score < 0 or score > 100:
                print('Input your score (0-100)')
                score = int(input('>>>'))
                add_spaceing()

            # _____ Printing Comments _____
        elif user_action == "P":
            outcome = decide_outcome(outcome, score)
            print(outcome)
            add_spaceing()

            # _____ Printing Stars _____
        elif user_action == "S":
            remaining = (score % 10)
            count = 1

            """Neat"""
            for x in range(score):
                if count > score - remaining:
                    count = score
                elif count % 10 == 0:
                    print("☆")
                else:
                    print("☆", end=(""))
                count += 1
            print("☆" * remaining)
            add_spaceing()

            """Clumped"""
        ##            print("☆"*score)
        ##            add_spaceing()

        # _____ Quiting program _____
        elif user_action == "Q":
            print("Farewell!")

            # _____ If action is not recognised _____
        else:
            print("Invalid option entered")
            print("")


def add_spaceing():
    print("\n\n\n")


def decide_outcome(outcome, score):
    if score > 90:
        outcome = "Excellent!"
    elif score > 50:
        outcome = "Pass"
    else:
        outcome = "Fail"
    return outcome


main(score, user_action, outcome)
