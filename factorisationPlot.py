from matplotlib import pyplot as plt
import math

def num(con, val):
    a = (con[0]*(val**2))
    b = (con[1]*val)
    c = (con[2])
    d = a+b+c
    return d

def curve(constant, x):
    m = []
    for i in range(len(x)):
        m.append(num(constant, x[i]))
    return m

def quadraticEquations_1(a, b, c):
    val = ( (-b) - (math.sqrt((b*b) - (4*a*c)))) / (2*a)
    return val

def quadraticEquations_2(a, b, c):
    val = ( (-b) + (math.sqrt((b*b) - (4*a*c)))) / (2*a)
    return val

constants = [1, -5, 6] # (x*x) + (-5x) + 6

# n1 = int(input("Enter : "))
# n2 = int(input("Enter : "))
# n3 = int(input("Enter : "))

# constants = []
# constants.append(n1)
# constants.append(n2)
# constants.append(n3)

a = quadraticEquations_1(constants[0], constants[1], constants[2])
b = quadraticEquations_2(constants[0], constants[1], constants[2])

c = 0.5 * a * b

c1 = int(c - 20)
c2 = int(c + 20)

if a == b:
    print("\nThe value of 'x' is {0}\n".format(a))

else:
    print("\nThe values of 'x' are {0} and {1}\n".format(a, b))

x = list(range(c1, c2))
plt.plot(x, curve(constants, x),'--', label = 'parabola')
plt.grid(True)
plt.title('Quadratic Equation')
plt.legend()
plt.show()