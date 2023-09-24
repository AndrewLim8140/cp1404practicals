# setting vars
sales = 0

while sales >= 0:
    # obtaining user's input
    sales = float(input("Input user sales :$"))

    # assigning BONUS based on sales amount
    if sales >= 1000:
        BONUS = 15/100
    else:
        BONUS = 10/100
    bonus_amount = sales * BONUS
    
    # Preventing the printing of -ive number
    if sales >= 0:                  
        print(f"Your bonus is ${bonus_amount:.2f}" )
