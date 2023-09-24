print("Electricity bill estimator 2.0")
# Setting vars
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# Obtaining inputs from user
tariff_used = int(input("Which tariff? 11 or 31 :"))

####"""For cost input"""
#####cost = int(input("Enter cents per kWh :"))

usage = float(input("Enter daily use in kWh :"))
days = int(input("Enter number of billing days :"))

# Calculations
if tariff_used == 11:
    bill = TARIFF_11*usage*days
elif tariff_used == 31:
    bill = TARIFF_31*usage*days

####"""for cost input"""
######bill = (cost/100)*usage*days

# Printing Estimated bill
print(f"Estimated bill :${bill:.2f}")
