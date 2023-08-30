from csv import *
from datetime import *
from guitar import Guitar

""" Option to sort using lambda (not sure if can use or not) """
sort_with_lambda = False
def main():
    guitars = []
    guitar_checked = []
    sorted_guitars=[]
    age_score = {}


    in_file = open('guitars.csv', 'r')
    for current_guitar in in_file:
        guitar_stats = []
        parts = current_guitar.strip().split(',')

        # Sending current guitar data to guitar.py
        guitar = Guitar(parts[0],int(parts[1]),parts[2])

        # Obtaining Current Year
        today_date = str(date.today())
        current_year = int(today_date[:4])

        # Obtaining guitar's age and checking if its vintage
        guitar_age = guitar.get_age(current_year)
        is_vintage = guitar.is_vintage()

        # assigning vintage tag
        if is_vintage == True:
            vintage_tag = 'Vintage'
        else:
            vintage_tag = ''

        # Extending guitar stats to guitars list
        guitar_stats.extend([parts[0], parts[1], parts[2], vintage_tag, guitar_age])
        guitars.append(guitar_stats)

        """For Debugging"""
        # print('current :',guitars)
        # print('total :',guitar_stats)
        # print('age :', guitar_age)
        # print('vintage :', is_vintage)

    # Obtaining len of longest guitar name
    for guitar_1 in guitars:
        guitar_checked.append(guitar_1)
        for guitar_2 in guitars:
            if (guitar_1 != guitar_2) and (guitar_2 not in guitar_checked):

                if len(guitar_1[0]) > len(guitar_2[0]):
                    longest_name_len = len(guitar_1[0])

                if len(guitar_1[0]) < len(guitar_2[0]):
                    longest_name_len = len(guitar_2[0])
    # Resetting checked list
    guitar_checked=[]

    # Sorting by age (using lambda)
    if sort_with_lambda == True:
        guitars.sort(key= lambda x:x[4])
        sorted_guitars = guitars

    # Sorting by age (less than)
    if sort_with_lambda == False:

        # Adding guitar tally to dictionary
        for guitar in guitars:
            age_score[guitar[0]] = 0

        # comparing and counting the age
        for guitar_1 in guitars:
            # check to remove duplicated results
            guitar_checked.append(guitar_1)
            for guitar_2 in guitars:

                # checking if both guitar isnt a duplicate or has been checked before
                if (guitar_1 != guitar_2) and (guitar_2 not in guitar_checked):
                    """ For Debugging """
    #                print('1:',guitar_1)
    #                print('2:',guitar_2)

                    lesser_check = guitar_1[4] < guitar_2[4]
                        # if guitar1 is lesser than guitar2
                    if lesser_check == True:
                        age_score[guitar_1[0]] += 1

                        # if guitar2 is lesser than guitar1 but not equal age
                    if (lesser_check == False) and (guitar_1[4] != guitar_2[4]):
                        age_score[guitar_2[0]] += 1

        # sorting by the oldest first, getting sort order
        guitars_sort_order=list(age_score.items())
        guitars_sort_order.sort(key=get_second_element)

        """Debugging To show sorted list"""
        print('\n list ', guitars_sort_order)

        """For Debugging"""
        print('\n',guitars_sort_order)

        # sorting guitar with respect to sort order
        for guitar_1 in guitars_sort_order:
            for guitar_2 in guitars:
                # if both guitars are same, append guitar stats to final list
                if guitar_1[0] == guitar_2[0]:
                    guitar_2=guitar_2
                    sorted_guitars.append(guitar_2)

        print('\n',sorted_guitars)

    # printing all guitars' stats
    for guitar in sorted_guitars:
        print(f'{guitar[0]:>{longest_name_len}} ({guitar[1]}) : ${guitar[2]} {guitar[3]}')

    in_file.close()

# Define to obtain second element in list
def get_second_element(iterable):
    return iterable[1]


main()

