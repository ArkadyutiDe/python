import math
pi = 3.14

def Cuboid(length, breadth, height):
    print("\nPerimeter of the Cuboid is : ", 4 * (length + breadth + height))
    print("The Diagonal of the Cuboid is : ", math.sqrt((length ** 2) + (breadth ** 2) + (height ** 2)))
    print("The volume of the Cuboid is : ", length * breadth * height)
    print("The Lateral Surface Area of the Cuboid is : ", 2 * (length + breadth) * height)
    print("The Total Surface Area of the Cuboid is : ", 2 * ((length * breadth) + (breadth * height) + (height * length)))

def Cube(side):
    print("\nThe Perimeter of the Cube is : ", 12 * side)
    print("The Diagonal of the Cube is : ", side * (math.sqrt(3)))
    print("The volume of the Cube is : ", side ** 3)
    print("The Total Surface Area of the Cube is : ", 6 * (side ** 2))
    print("The Lateral Surface Area of the Cube is : ", 4 * (side ** 2))

def Sphere(radius):
    print("\nThe Volume of the Sphere is : ", (4 * pi * (radius ** 3)) / 3)
    print("The Total Surface Area of the Sphere is : ", 4 * pi * radius * radius)

def Hemisphere(radius):
    print("\nThe Volume of the Hemisphere is : ", (2 * pi * (radius ** 3)) / 3)
    print("The Curved Surface Area of the Hemisphere is : ", 2 * pi * radius * radius)
    print("The Total Surface Area of the Hemisphere is : ", 3 * pi * radius * radius)

def Cone(radius, height):
    SlantingHeight = math.sqrt((radius ** 2) + (height ** 2))
    print("\nThe Slanting Height of the Cone is : ", SlantingHeight)
    print("The Volume of the cone is : ", pi * radius * radius * height/3)
    print("The Curved Surface Area of the Cone is : ", pi * radius * SlantingHeight)
    print("The Total Surface Area of the Cone is : ", pi * radius * (radius + SlantingHeight))

def Cylinder(radius, height):
    print("\nThe Volume of the Cylinder is : ", pi * radius * radius * height)
    print("The Curved Surface Area of the Cylinder is : ", 2 * pi * radius * height)
    print("The Lateral Surface Area of the Cylinder is : ", 2 * pi * radius * radius)
    print("The Total Surface Area of the Cylinder is : ", 2 * pi * radius * (radius + height))

if __name__ == "__main__":
    start = 'y'

    while start != 'n':
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Enter 1 for Cuboid")
        print("Enter 2 for Cube")
        print("Enter 3 for Sphere")
        print("Enter 4 for Hemisphere")
        print("Enter 5 for Cone")
        print("Enter 6 for Cylinder")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        choice = int(input("Enter your choice : "))
        print("\n")

        if choice == 1:
            l = int(input("Enter the Length = "))
            b = int(input("Enter the Breadth = "))
            h = int(input("Enter the Height = "))
            Cuboid(l, b, h)

        elif choice == 2:
            s = int(input("Enter the Side = "))
            Cube(s)

        elif choice == 3:
            r = int(input("Enter the Radius = "))
            Sphere(r)

        elif choice == 4:
            r = int(input("Enter the Radius = "))
            Hemisphere(r)

        elif choice == 5:
            r = int(input("Enter the Radius = "))
            h = int(input("Enter the Height = "))
            Cone(r,h)

        elif choice == 6:
            r = int(input("Enter the Radius = "))
            h = int(input("Enter the Height = "))
            Cylinder(r, h)

        else:
            print("...Option Not Valid...")
            choice = int(input("Enter your choice again: "))
            print("\n")

            if choice == 1:
                l = int(input("Enter the Length = "))
                b = int(input("Enter the Breadth = "))
                h = int(input("Enter the Height = "))
                Cuboid(l, b, h)

            elif choice == 2:
                s = int(input("Enter the Side = "))
                Cube(s)

            elif choice == 3:
                r = int(input("Enter the Radius = "))
                Sphere(r)

            elif choice == 4:
                r = int(input("Enter the Radius = "))
                Hemisphere(r)

            elif choice == 5:
                r = int(input("Enter the Radius = "))
                h = int(input("Enter the Height = "))
                Cone (r, h)

            elif choice == 6:
                r = int(input("Enter the Radius = "))
                h = int(input("Enter the Height = "))
                Cylinder(r, h)

            else:
                print("...Option Not Valid...")

        start = input("\nDo you want to start again? [Y/n] = ")

        if (start == 'y'or start == ''):
            print("*-*-*-*-*-*-* Hurrah!!!!!!  The Calculator starts again *-*-*-*-*-*-*\n")

        elif start == 'n':
            print("Thanks !!\n")

        else:
            print("Option is not valid")
            print("Thanks !!")
            start = 'n'