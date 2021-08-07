def PrimeNumber(n):
    factors = []
    for i in range(1, n+1):
        if n%i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    a = int(input("\nEnter a number : "))

    if a < 1:
        print("Prime Number can be only checked when the number is a natural number.\n")
    else:
        f = PrimeNumber(a)
        if len(f) == 2:
            print("{0} is a Prime Number.".format(a))
        if len(f) > 2:
            print("{0} is a Composite Number.".format(a))
        if len(f) == 1:
            print("{0} is a Special Number.".format(a))
        print("\n")