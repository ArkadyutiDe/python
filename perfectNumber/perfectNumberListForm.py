def factor(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def primeNumber(num):
    f = factor(num)
    if len(f) == 2:
        return num
    else:
        return 0

def perfectNumber(nu, num):
    n1 = 2 ** (nu-1)
    n = n1 * num
    return n

if __name__ == '__main__':
    a = int(input("\nEnter number of perfect numbers needed :- "))
    lPerfect = []
    i = 0

    while len(lPerfect) != a:
        b = ( 2 ** (i + 1) ) - 1
        h = primeNumber(b)

        if h == 0:
            p = 0

        else:
            p = perfectNumber(i+1, h)

        if p != 0:
            lPerfect.append(p)

        i = i + 1

    for i in range(len(lPerfect)):
        print("\nNumber {1} :- {0}".format(lPerfect[i], i+1))
    print("\n")