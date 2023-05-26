import numpy as np

def trace(a):
    a = np.array(a)
    if a.shape[0] == a.shape[1]:
        return np.array(np.sum([a[i,i] for i in range(a.shape[0])]))
    else:
        raise ValueError("Input matrix is not square")

def multiply(a,b):
    a = np.array(a)
    b = np.array(b)
    return np.array([[a[i,:].dot(b[:,j]) for j in range(b.shape[1])] for i in range(a.shape[0])])

def transpose(a):
    a = np.array(a)
    p = np.zeros([a.shape[1], a.shape[0]], dtype = complex)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            p[j,i] = a[i,j]
    return p

def determinant(a):
    if a.shape[0] == a.shape[1]:
        if a.shape == (2,2):
            return a[0,0]*a[1,1]-a[0,1]*a[1,0]
        elif a.shape == (3,3):
            one = a[0,0]*determinant(a[1:,[1,2]])
            second = -1*a[0,1]*determinant(a[1:,[0,2]])
            third = a[0,2]*determinant(a[1:,[0,1]])
            return (one+second+third)
        else:
            raise "Work in progress"
    
    else:
        raise ValueError("Input Matrix is not a square matrix")

