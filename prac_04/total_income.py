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
    total = 0
    for month in range(1, number_of_month + 1):
        monthly_components=[]
        income = incomes[month - 1]
        total += income
        monthly_components.extend([month,income,total])
        monthly_totals.append(monthly_components)
    print_report(monthly_totals)

def print_report(monthly_totals):
    for i in range(0,len(monthly_totals)):
        print(f"Month{monthly_totals[i][0]:2} - Income: ${monthly_totals[i][1]:.2f} Total: ${monthly_totals[i][2]:.2f}")


main()
