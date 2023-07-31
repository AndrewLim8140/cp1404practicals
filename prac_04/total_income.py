"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of number_of_month."""
    incomes,monthly_totals = [],[]
    number_of_month = int(input("How many number_of_month? "))

    for month in range(1, number_of_month + 1):
        income = float(input(f"Enter income for month {str(month)} : "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print_report(incomes, number_of_month,monthly_totals)


    for month in range(1,number_of_month + 1):
        income = incomes[month-1]
        current_total = monthly_totals[month-1]
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, current_total))


def print_report(incomes, number_of_month,monthly_totals):
    total = 0
    for month in range(1, number_of_month + 1):
        income = incomes[month - 1]
        total += income
        monthly_totals.append(total)
        print(monthly_totals)
    return(monthly_totals)


main()
