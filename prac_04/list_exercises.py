def main():
##    numbers=[]
##    
##    for i in range(1,6):
##        user_number=int(input("Number: "))
##        numbers.append(user_number)
##        
##    average_number = sum(numbers)/len(numbers)
##        
##    print('The first number is {first}'.format(first=numbers[0]))
##    print('The last number is {last}'.format(last=numbers[-1]))
##
##    print('The smallest number is {smallest}'.format(smallest=min(numbers)))
##    print('The largest number is {largest}'.format(largest=max(numbers)))
##
##    print('The average of the number is {average:.2f}'.format(average=average_number))


    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'] 
    username_input = input('Input your username :')
    
    if (username_input in usernames) == True:
        print('Access granted')
    else:
        print('Access denied')
main()
