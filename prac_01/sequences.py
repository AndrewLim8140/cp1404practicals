# setting vars
action = ""
MENU =  '''i.  Show the even numbers from x to y
ii. Show the odd numbers from x to y
iii.Show the squares from x to y
iv. Exit the program'''

# obtaining user inputs
number_1 = int(input("Input initial number :"))
number_2 = int(input("Input second number :"))

# creating menu
while action != 'iv':
    print(MENU)
    action = input(">>>")
    
    # checking if number 1 is odd / even
    if number_1%2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'

    """Computing logic"""
    # Even count
    if action == "i":                               
        if odd_even == 'odd':                   #-----If initial number is odd
            for i in range(number_1+1,number_2+1,2):
                print(i,end=" ")
            print()
  
        else:                                   #-----If initial number is even
            for i in range(number_1,number_2+1,2):
                print(i,end=" ")
            print()

    # Odd count        
    if action == 'ii' :                             
        
        if odd_even == 'odd':                   #-----If initial number is odd
            for i in range(number_1,number_2+1,2):
                print(i,end=" ")
            print()
        
        else:                                   #-----If initial number is even
            for i in range(number_1+1,number_2+1,2):
                print(i,end=" ")
            print()
            
    # Squares number 
    if action == "iii":                             
        for i in range(number_1,number_2):
            print(i*i,end=" ")
        print()

    # Exit                    
    if action == "iv":                              
        break
            
