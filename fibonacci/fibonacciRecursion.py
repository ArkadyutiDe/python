def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recursion(n-1) + fibonacci_recursion(n-2))

if __name__ == '__main__':
    n = int(input("\nEnter the number of terms : "))
    if n <= 0:
        print("Enter a positive integer please.\n")
    else:
        for i in range(n):
            print("Term number {0} is {1}".format(i+1,fibonacci_recursion(i)))
    print("\n")