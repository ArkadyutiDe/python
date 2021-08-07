restart = 'y'  # here, we entered 'y'in the variable 'restart'
while restart !='n':  # this loop will run untill the value of variable 'restart' is not equal to 'n'.
    b = int(input("\nEnter a number : "))
    c = []  # here, the factors will be entered in this list.
    for i in range(1 , b+1):
        if b%i == 0:
            c.append(i)  # here, factors are entered in the list 'c'
    if len(c) == 2:  # if the number has two factors, it will be printed that it is a prime number.
        print("{0} is a prime number".format(b))
    elif len(c) == 1:  # if the number has only one factor, it will be printed that it is a special number.
        print("{0} is a special number".format(b))
    else:  # if the number has more than two factors, it will be printed that it is a composie number.
        print("{0} is a composite number".format(b))
    print("\n")

    restart = input("Do you want to start again? {y/n(any number or letter can also be used in place of n)} : ")

    if restart == 'y':
        print("Hurrah!! It starts again!!")
    elif restart == 'n':
        print("...Thanks...")
    else:
        print("...Thanks...")
        restart = 'n'