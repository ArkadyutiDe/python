def factor(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def perfect(num):
    f = factor(num)
    total = 0
    for i in range(len(f)):
        total = total + f[i]

    if total / 2 == num:
        return 'perfect'
    else:
        return 0

if __name__ == '__main__':
    restart = 'y'
    while restart != 'n':
        a = int(input("\nEnter the number :- "))
        val = perfect(a)

        if val == 'perfect':
            print("{0} is a perfect number\n".format(a))
        else:
            print("{0} is not a perfect number\n".format(a))

        restart = input("Would you like to start again? [Y,n] :- ")

        if (restart == 'Y' or restart == 'y' or restart == '' or restart == ' '):
            print("Hurrah!!! It starts again!!!")
        else:
            print("Thanks!! See you later!!")
            restart = 'n'