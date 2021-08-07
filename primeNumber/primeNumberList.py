def PrimeNumber(n):
    factors = []
    for i in range(1, n+1):
        if n%i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    restart = 'y'

    while restart != 'n':
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Enter 1 for giving a range for list")
        print("Enter 2 for giving ur own list")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

        option = int(input("Enter your option : "))

        if option == 1:
            upper = int(input("\nEnter the starting point of the list : "))
            end = int(input("Enter the ending point of the list : "))
            print("\n")

            num = list(range(upper, end+1))

            for i in range(len(num)):
                if num[i] < 1:
                    print("Prime Number can be only checked when the number is a natural number.\n")
                else:
                    f = PrimeNumber(num[i])
                    if len(f) == 2:
                        print("{0} is a Prime Number.".format(num[i]))
                    if len(f) > 2:
                        print("{0} is a Composite Number.".format(num[i]))
                    if len(f) == 1:
                        print("{0} is a Special Number.".format(num[i]))
            print("\n")

        elif option == 2:
            n = int(input("Enter the number of numbers needed : "))

            if n < 0:
                print("This option are invalid")

            else:
                num = []
                for i in range(n):
                    nu = int(input("Enter number {0} : ".format(i+1)))
                    num.append(nu)
                print("\n")

                for i in range(len(num)):
                    if num[i] < 1:
                        print("Prime Number can be only checked when the number is a natural number.\n")
                    else:
                        f = PrimeNumber(num[i])
                        if len(f) == 2:
                            print("{0} is a Prime Number.".format(num[i]))
                        if len(f) > 2:
                            print("{0} is a Composite Number.".format(num[i]))
                        if len(f) == 1:
                            print("{0} is a Special Number.".format(num[i]))
            print("\n")

        else:
            print("Option is invalid.")

        restart = input("Do you want to start again[Y/n] : ")

        if (restart == 'y' or restart == 'Y' or restart == ''):
            print("\nHurrah!! It starts again")
        else:
            print("\nThanks!! Bye for now!!\n")
            restart = 'n'