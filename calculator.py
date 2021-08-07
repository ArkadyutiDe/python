def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    product = num1 * num2
    return product

def division(num1, num2):
    q = num1 / num2
    r = num1 % num2
    quotient1 = int(q)
    quotient = [quotient1, r]
    return quotient

def exponential(num1, num2):
    eVal = num1 ** num2
    return eVal

if __name__ == '__main__':
    restart = 'y'

    while restart != 'n':
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("|Enter 1 to Add                     |")
        print("|Enter 2 to Subtract                |")
        print("|Enter 3 to Multiply                |")
        print("|Enter 4 to Divide                  |")
        print("|Enter 5 to get Exponential Value   |")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

        choice = input("Enter your choice :- ")

        if choice == '1':
            n1 = int(input("\nEnter the first addend :- "))
            n2 = int(input("Enter the second addend :- "))
            sum = add(n1, n2)
            print("\n{0} plus {1}\nSum :- {2}\n".format(n1, n2, sum))

        elif choice == '2':
            n1 = int(input("\nEnter the minuend :- "))
            n2 = int(input("Enter the subtrahend :- "))
            difference = subtract(n1, n2)
            print("\n{0} minus {1}\nDifference :- {2}".format(n1, n2, difference))

        elif choice == '3':
            n1 = int(input("\nEnter the muliplicand :- "))
            n2 = int(input("Enter the muliplier :- "))
            product = multiply(n1, n2)
            print("\n{0} multiplied with {1}\nProduct :- {2}".format(n1, n2, product))

        elif choice == '4':
            n1 = int(input("\nEnter the Dividend :- "))
            n2 = int(input("Enter the Divisor :- "))
            quotient = division(n1, n2)
            print("\n{0} divided by {1} :- \nQuotient = {2}\nRemainder = {3}\n".format(n1, n2, quotient[0], quotient[1]))

        elif choice == '5':
            n1 = int(input("\nEnter the Base :- "))
            n2 = int(input("Enter the Power :- "))
            exponentialVal = exponential(n1, n2)
            print("\n{0} to the power {1}\nValue :- {2}".format(n1, n2, exponentialVal))

        else:
            print("\nOption invalid")
            choice = input("Enter your choice again :- ")

            if choice == '1':
                n1 = int(input("\nEnter the first addend :- "))
                n2 = int(input("Enter the second addend :- "))
                sum = add(n1, n2)
                print("\n{0} plus {1}\nSum :- {2}\n".format(n1, n2, sum))

            elif choice == '2':
                n1 = int(input("\nEnter the minuend :- "))
                n2 = int(input("Enter the subtrahend :- "))
                difference = subtract(n1, n2)
                print("\n{0} minus {1}\nDifference :- {2}".format(n1, n2, difference))

            elif choice == '3':
                n1 = int(input("\nEnter the muliplicand :- "))
                n2 = int(input("Enter the muliplier :- "))
                product = multiply(n1, n2)
                print("\n{0} multiplied with {1}\nProduct :- {2}".format(n1, n2, product))

            elif choice == '4':
                n1 = int(input("\nEnter the Dividend :- "))
                n2 = int(input("Enter the Divisor :- "))
                quotient = division(n1, n2)
                print("\n{0} divided by {1} :- \nQuotient = {2}\nRemainder = {3}\n".format(n1, n2, quotient[0], quotient[1]))

            elif choice == '5':
                n1 = int(input("\nEnter the Base :- "))
                n2 = int(input("Enter the Power :- "))
                exponentialVal = exponential(n1, n2)
                print("\n{0} to the power {1}\nValue :- {2}".format(n1, n2, exponentialVal))

            else:
                print("\nOption invalid")

        restart = input("\nWould you like to start again? [Y,n] :- ")
        if (restart == 'y' or restart == 'Y' or restart == ' ' or restart == ''):
            print("\n*-*-* Hurrah!! it starts again!!! *-*-*\n")
        else:
            print("\nThanks....Bye for now....\n")
            restart = 'n'