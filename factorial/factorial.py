def factorial(a):
    f = 1
    for i in range(1, a+1):
        f = f*i
    return f

a = int(input("\nEnter a number : "))
if a>0:
    b = factorial(a)
    print("Factorial of {0} is {1}".format(a,b))
elif a == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial doesn't exist in negative numbers.")
print("\n")