#Setting vars
total_price = 0

# obtaining number of items
item_count = int(input("Number of items :"))

# if item_count is -ive
while item_count < 0:
    print("Invalid number of items!")
    item_count = int(input("Number of items :"))

# obtaining price of items
for i in range(0,item_count):
    item_price = float(input('Price of item :$'))
    total_price = total_price + item_price
    print(total_price)

# Calculating total price after discount
if total_price >= 100:
    total_price = total_price * (90/100)

# Printing output
print(f"Total price for {item_count} items is ${total_price: .2f}")