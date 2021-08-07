def factor(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def primeNumber(n):
    f = factor(n)
    if len(f) == 2:
        return n
    else:
        return 0

def perfectNumber(nu, num):
    n1 = 2 ** (nu-1)
    n = n1 * num
    return n

if __name__ == '__main__':
    a = 2
    b = (2**a) - 1
    h = primeNumber(b)

    if h == 0:
        p = 0
    else:
        p = perfectNumber(a, h)

    if p == 0:
        print("\nChange the number in the code\n")
    else:
        print("\n{0} is your answer\n".format(p))