def factorial_recursion(n):
    if n == 1:
        return n
    else :
        return n*factorial_recursion(n-1)

if __name__ == '__main__':
    n = int(input("\nEnter a number : "))

    if n < 0 :  # here, the code is said to check if the given number is negative or not..
        print("Factorial doesn't exist in Negative Numbers\n")  # If the number is negative, it will be shown a line something like the one given..
    elif n == 0:  # here, the code is said to check whether the whole number is 0 or not..
        print("Factorial of 0 is 1.")  # If the number is 0, it will be shown a line something like the one given..
    else:  # now the left numbers will be surely natural numbers..
        a = factorial_recursion(n)  # now the function factorial_recursion is called with the input of integer 'n'..
        print("Factorial of {0} is {1}\n".format(n,a))