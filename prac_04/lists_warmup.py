numbers = [3,1,4,1,5,9,2]

##numbers[0] = 3
##numbers[-1] = 2
##numbers[3] = 1
##numbers[:-1] = [3,1,4,1,5,9]
##numbers[3:4] = [1]
##5 in numbers = True
##7 in numbers = False
##"3" in numbers = False
##numbers + [6, 5, 3] = [3,1,4,1,5,9,2,6,5,3]

""" First element to ten """
numbers[0]='ten'
print(numbers)

""" Last element to 1"""
numbers[-1]=1
print(numbers)

""" all except first 2 elemet """
print(numbers[2:])

""" 9 is a element of numbers """
print(9 in numbers)
