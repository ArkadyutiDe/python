def fibonacciSeries(num):
    n1 = 0
    n2 = 1
    series = [n1, n2]

    while len(series) != num:
        ne = n1 + n2
        series.append(ne)
        n1 = n2
        n2 = ne

    return series

if __name__ == '__main__':
    a = int(input("\nEnter number of terms needed :- "))
    print("\n")
    b = fibonacciSeries(a)

    for i in range(len(b)):
        print("Term number {0} is {1}".format(i + 1, b[i]))