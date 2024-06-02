import numpy as np
import math



#--matrixs--


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

    
    return T


def Rotation_Transform(T:list) -> list:
   
    R = np.zeros((3, 3))
    
    R[0][0] = T[0][0]
    R[0][1] = T[0][1]
    R[0][2] = T[0][2]
    
    R[1][0] = T[1][0]
    R[1][1] = T[1][1]
    R[1][2] = T[1][2]
    
    R[2][0] = T[2][0]
    R[2][1] = T[2][1]
    R[2][2] = T[2][2]
    
    return R 
    



def Transpose_Rotation(R:list) -> list:
    
    R_i = np.zeros((3, 3))
    
    R_i[0][0] = R[0][0]
    R_i[0][1] = R[1][0]
    R_i[0][2] = R[2][0]
    
    
    R_i[1][0] = R[0][1]
    R_i[1][1] = R[1][1]
    R_i[1][2] = R[2][1]
    
    R_i[2][0] = R[0][2]
    R_i[2][1] = R[1][2]
    R_i[2][2] = R[2][2]
    
    return R_i



def P_matrix(T:list) -> list:
    
    Z = np.zeros((3, 1))
    Z[0][0] = T[0][3]
    Z[1][0] = T[1][3]
    Z[2][0] = T[2][3]
    
    return Z
    
   
    
#--formoules--



def W(R_i, i, t):
    
    Z = np.zeros((3, 1))
    Z[2][0] = 1
    
    theta = np.zeros((3, 1))
    theta[2][0] = t
    
    if i==0:
        return np.dot(theta, Z)
    
    return np.sum(np.dot(R_i, W(R_i, i-1, theta)), np.dot(theta, Z))



def V(R_i, i, theta, W, d, P):
    
    def W(R_i, i, t):
    
        Z = np.zeros((3, 1))
        Z[2][0] = 1
        
        theta = np.zeros((3, 1))
        theta[2][0] = t
        
        if i==0:
            return np.sum(np.dot(R_i, np.zeros((3,1))), np.dot(theta, Z))
        
        return np.sum(np.dot(R_i, W(R_i, i-1, theta, Z)), np.dot(theta, Z))

    
    Z = np.zeros((3, 1))
    Z[2][0] = 1
    
    D = np.zeros((3, 1))
    D[2][0] = d
    
    if i==0:
        return np.sum(np.dot(R_i, np.inner(0,P)), np.dot(D, Z))

    np.dot(R_i, np.sum(0,P))
    return np.sum(np.dot(R_i, (np.sum(V(R_i, i-1, theta, W, d, P), W(R_i, i-1, theta)))), np.dot(D, Z))

    
    

#--main--

def main():
        

    # initialize denavit dimensions:
    i = int(input("enter number of i : ")) # number of line
    A = np.zeros((i, 4)) # Denavit Matrix

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
    print('-----------------------------')
    print("Transform matix:", end="\n\n")
    
    T_list = [] # Transform matrix
    R = [] # Rotation matrix
    P = []
    for k in range(i):
        
        print(f"({k},{k+1})[T]: ")  
        T = Transform_Denavit(alpha[k],theta[k], d[k])
        T_list.append(T)
        print(T, end="\n\n")
        
        R.append(Rotation_Transform(T=T))
        P.append(P_matrix(T=T))
       
    
    print('-----------------------------')
    print("Rotation matix:", end="\n\n")
    
    R_i = [] # Transpose Rotation matrix   
    for k in range(i):
        print(f"({k},{k+1})[R]: ")
        print(f'R{k}\n', R[k], end='\n\n')  
        R_i.append(Transpose_Rotation(R=R[k]))
    
    
    print('-----------------------------')
    print("Transpose Rotation matix:", end="\n\n")
    
    # Display R^T and P matrixes
    for k in range(i):
        print(f"({k+1},{k})[R]: ")
        print(f'R{k}\n', R_i[k], end='\n\n')
    print('-----------------------------')
    print("P matrix: ", end="\n\n")
    for k in range(i):  
        print(f"({k})[P]: ")
        print(f'P{k}\n', P[k], end='\n\n') 
    
    print('-----------------------------')
    print("V - W calculation: ", end="\n\n")      
    
        
    Z = np.zeros((3, 1))
    Z[2][0] = 1
    
    t = np.zeros((3, 1))
    t[2][0] = theta[0]

    D = np.zeros((3, 1))
    D[2][0] = d[0]

    W=[]
    W.append(np.multiply(t, Z))
        
    for k in range(1,i):
        t[2][0] = theta[k]
        W.append(np.add(np.dot(R_i[k], W[k-1]), np.multiply(t, Z)))


    V = []
    V.append(np.add(np.dot(R_i[0], np.inner(W[0], P[0])), np.multiply(D, Z)))
    
    for k in range(1,i):
        D[2][0] = d[k]
        V.append(np.add(np.dot(R_i[k], np.add(V[k-1], np.inner(W[k-1], P[k]))), np.multiply(D, Z)))
        
    
    for k in range(i):
        
        print(f"({k})[W]: ")
        print(W[k],end='\n\n')      
        
        print(f"({k})[V]: ")
        print(V[k]) \
            
        print(end='\n\n\n')     
        
        
if __name__ == '__main__':
    main()      