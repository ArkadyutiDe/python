import math
pi = 3.14

def Square(side):
    print("The Diagonal of the Square is : ", side * (math.sqrt(2)))
    print("The Perimter of the Square is : ", 4 * side)
    print("The Area of the Square is : ", side ** 2)
    return(side)

def Rectangle(length, breadth):
    Diagonal = math.sqrt((length ** 2)+ (breadth ** 2))
    print("The Diagonal of the Rectangle is : ", Diagonal)
    print("The Perimeter of the Rectangle is : ", 2 * (length + breadth))
    print("The Area of the Rectangle is : ", length * breadth)
    return(Diagonal)

def Circle(radius):
    print("The Circumference of the Circle : ", 2 * pi * radius)
    print("The Area is : ", pi * (radius ** 2))
    return(radius)

def Parallelogram(base, height, adjacent):
    area = base * height
    AdjacentHeight = area/adjacent
    print("The Perimeter is : ", 2 * (base + adjacent))
    print("The Area is : ", area)
    return(AdjacentHeight)

def Trapezium(D1, D2, S1, S2):
    print("The Permimter is : ", 2 * (S1 + S2))
    print("The Area is : ", 0.5 * D1 * D2)

if __name__ == "__main__":

    start = 'y'

    while start != 'n':
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Press 1 for Square")
        print("Press 2 for Rectangle")
        print("Press 3 for Circle")
        print("Press 4 for Parallelogram")
        print("Press 5 for Trapezium")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        choice = int(input("Enter your choice : "))
        print("\n")

        if choice == 1:
            s = int(input("Enter the Side : "))
            Square(s)

        elif choice == 2:
            l = int(input("Enter the Length : "))
            b = int(input("Enter the Breadth : "))
            Rectangle(l, b)

        elif choice == 3:
            r = int(input("Enter the Radius : "))
            Circle(r)

        elif choice == 4:
            b = int(input("Enter the Base : "))
            h = int(input("Enter the Height : "))
            a = int(input("Enter the Adjacent Side : "))
            Parallelogram(b, h, a)

        elif choice == 5:
            Diagonal1  = int(input("Enter the first diagonal : "))
            Diagonal2  = int(input("Enter the second diagonal : "))
            Side1  = int(input("Enter the first side : "))
            Side2  = int(input("Enter the second side : "))
            Trapezium(Diagonal1, Diagonal2, Side1, Side2)

        else :
            print("....Option Not Valid....")
            choice = int(input("Enter your choice : "))
            print("\n")

            if choice == 1:
                s = int(input("Enter the Side : "))
                Square(s)

            elif choice == 2:
                l = int(input("Enter the Length : "))
                b = int(input("Enter the Breadth : "))
                Rectangle(l, b)

            elif choice == 3:
                r = int(input("Enter the Radius : "))
                Circle(r)

            elif choice == 4:
                b = int(input("Enter the Base : "))
                h = int(input("Enter the Height : "))
                a = int(input("Enter the Adjacent Side : "))
                Parallelogram(b, h, a)

            elif choice == 5:
                Diagonal1  = int(input("Enter the first diagonal : "))
                Diagonal2  = int(input("Enter the second diagonal : "))
                Side1  = int(input("Enter the first side : "))
                Side2  = int(input("Enter the second side : "))
                Trapezium(Diagonal1, Diagonal2, Side1, Side2)

        start = (input("\nDo you want to start again? [Y/n] = "))

        if (start == 'y' or start == 'Y' or start == ''):
            print("*-*-*-*-*-*-* Hurrah!!!!!!  The Calculator starts again *-*-*-*-*-*-*\n")
        else:
            print("Thanks !!")
            start = 'n'