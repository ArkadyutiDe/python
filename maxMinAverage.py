def max(num):  # this function is created to find the largest number.
    a = num[0]
    for i in range(len(num)):
        if a < num[i]:
            a = num[i]
    return a

def min(num):  # this function is created to find the smallest number.
    a = num[0]
    for i in range(len(num)):
        if a > num[i]:
            a = num[i]
    return a

def average(num):  # this function is created to find he average of the provided numbers.
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    average = sum/len(num)
    return average

if __name__ == '__main__':
    a = int(input("\nEnter the number of numbers needed : "))
    num = []  # all the numbers will be entered in this list.

    for i in range(a):
        nu = int(input("Enter number {0} : ".format(i+1)))
        num.append(nu)  # here, all the numbers are entered in the list.

    maximum = max(num)  # here, the function max's value is stored in the variable 'maximum'.
    minimum = min(num)  # here, the function min's value is stored in the variable 'minimum'.
    mean = average(num)  # here, the function average's value is stored in the variable 'average'.

    mean = round(mean, 2) # here, we are rounding the number stored in the variable 'mean' to 2 digits.

    print("\nThe largest number is ",maximum)
    print("The smallest number is ",minimum)
    print("The average is ",mean)
    print("\n")