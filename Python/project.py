import numpy as np
import math


def Transform_Denavit(alpha, theta, d):

    T = np.zeros((4, 4))

    T[0][0] = math.cos(theta)
    T[0][1] = -1*math.sin(theta)
    T[0][2] = 0
    T[0][3] = alpha

    T[1][0] = math.sin(theta)*math.cos(alpha)
    T[1][1] = math.cos(theta)*math.cos(alpha)
    T[1][2] = -1*math.sin(alpha)
    T[1][2] = -1*math.sin(alpha)*d

    T[2][0] = math.sin(theta)*math.sin(alpha)
    T[2][1] = math.cos(theta)*math.sin(alpha)
    T[2][2] = math.cos(alpha)
    T[2][3] = math.cos(alpha)*d

    T[3][3] = 1

    print(T, end="\n\n")



# initialize denavit dimensions:
i = int(input("enter number of i : "))
A = np.zeros((i, 4))

A[i-1][3] = 1.0

alpha = []
a = []
theta = []
d = []

for m in range(i):
    for n in range(4):
        if n==0:  
            A[m][n] = float(input(f"please enter A[{m+1}][{n+1}] as alpha({m}): (pi:3.14, pi/2:1.57)"))
            
            if A[m][n] == 3.14:
                A[m][n] = math.pi

            if A[m][n] == 1.57:
                A[m][n] = math.radians(90)

            alpha.append(A[m][n])

        if n==1:
            A[m][n] = float(input(f"please enter A[{m+1}][{n+1}] as a({m}): "))
            a.append(A[m][n])

        if n==2:
            A[m][n] = float(input(f"please enter A[{m+1}][{n+1}] as theta({m+1}): (pi:3.14, pi/2:1.57)"))
            
            if A[m][n] == 3.14:
                A[m][n] = math.pi

            if A[m][n] == 1.57:
                A[m][n] = math.radians(90)

            theta.append(A[m][n])

        if n==3:
            A[m][n] = float(input(f"please enter A[{m+1}][{n+1}] as d({m+1}): "))
            d.append(A[m][n])
    print()

# Denavit:
print("Denavit is:\n",A,end="\n\n")

for k in range(i):
    print(f"({k},{k+1})[T]: ")
    Transform_Denavit(alpha[k],theta[k], d[k])