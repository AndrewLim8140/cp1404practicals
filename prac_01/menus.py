# setting vars
choice = ""

# obtaining user's name
name = input("Enter name :")

while choice != 'Q':
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    
    # obtaining user's decision
    choice = input(">>> ")
    if choice == 'H':
        print("Hello ",name)
    elif choice == 'G':
        print("Goodbye ",name)
    elif choice != 'Q':
        print("Invalid choice")
        
print("Finished")
