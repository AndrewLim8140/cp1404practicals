"""_ 1 _"""
with open("name.txt", "a") as out_name:
    name_input = input("Input your name :")
    out_name.write(name_input)

"""_ 2 _"""
with open("name.txt", "r") as in_name:
    name_output = str(in_name.readline())
    print("Your name is {name:}".format(name=name_output))

"""_ 3 _"""
with open("numbers.txt", "r") as cal_numbers:
    digits = cal_numbers.readlines()
    first = int(digits[0])
    second = int(digits[1])
    total = first + second
    print("the sum of first 2 is {total}".format(total=total))

"""_ 4 _"""
with open("numbers.txt", "r") as cal_numbers:
    total = 0
    digits = cal_numbers.readlines()
    for x in range(0, 3):
        total += int(digits[x])

    print("the total is {total}".format(total=total))
