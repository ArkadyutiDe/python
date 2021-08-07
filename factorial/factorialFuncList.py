def factorial(a):
    f = 1
    for i in range(1, a+1):
        f = f*i
    return f

restart = 'y' # here, we are entering the value of 'y' in the variable 'restart'

while restart != 'n': # here, this loop will run only when the value of the variable 'restart' isn't 'n'
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Enter 1 for giving a range for list") # here, we are asking the user to give a range of numbers
    print("Enter 2 for giving ur own list") # here, we are asking to give numbers
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

    option = int(input("Enter your option : ")) # here, the user will write their choice..

    if option == 1: # if choice says that they will enter a range of number, then this loop will be running..
        upper = int(input("\nEnter the starting point of the list : ")) # we will be asking for the first number..
        end = int(input("Enter the ending point of the list : ")) # we will be asking for the last number..
        print("\n")

        num = list(range(upper, end+1)) # in the list num, we will be storing all the integers from the range given by the user..

        for i in range(len(num)):
            if num[i] > 0: # here, they are checking whether the number is Natural..
                f = factorial(num[i]) # if yes, then they will send the number to the function of factorial and the function will send the factorial..
                print("Factorial of {0} is {1}.".format(num[i], f))
            elif num[i] == 0: # if the number is not Natural but a whole number, then they will print the line given below..
                print("Factorial of 0 is 1.")
            else: # if the number is negative then they will print the line below..
                print("Factorial doesn't exist in Negative Numbers.")
        print("\n")

    elif option == 2: # if choice says that they will enter the numbers they need..
        n = int(input("\nHow many numbers do you need : ")) # here, they will ask that how many numbers do you need..
        print("\n")
        num = [] # here, we are saying that num is a list and we will append all the numbers given by the user in this list 'num'..

        for i in range(n):
            nu = int(input("Enter number {0} : ".format(i+1)))
            num.append(nu) # here, we are entering all those numbers..

        for i in range(len(num)):
            if num[i] > 0: # here, they are checking whether the number is Natural..
                f = factorial(num[i]) # if yes, then they will send the number to the function of factorial and the function will send the factorial..
                print("Factorial of {0} is {1}.".format(num[i], f))
            elif num[i] == 0: # if the number is not Natural but a whole number, then they will print the line given below..
                print("Factorial of 0 is 1.")
            else: # if the number is negative then they will print the line below..
                print("Factorial doesn't exist in Negative Numbers.")
        print("\n")

    else: # if the choice is given invalid then, the line below will be printed..
        print("Option not available")

    restart = input("Do you want to start again[Y/n] : ") # here, we are changing the value in the variable 'restart'..

    if (restart == 'y' or restart == 'Y' or restart == ''): # if the input in 'restart' is of the inputs stated in the line, the next line is printed..
        print("\nHurrah!! It starts again")
    else: # otherwise, the next line is printed and then we are entering 'n' in variable 'restart' to stop the loop..
        print("\nThanks!! Bye for now!!\n")
        restart = 'n'