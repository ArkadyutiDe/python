a = int(input("\nEnter number of terms needed : "))
b = 0
n1 = 0
n2 = 1
while a > b:
    print('Value of element number {0:4d} is {1:4d}'.format(b+1,n1))
    ne = n1 + n2
    n1 = n2
    n2 = ne
    b = b+1