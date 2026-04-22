import numpy as np
arr=np.array([10,20,30,40])
print("1D Array:",arr)

#Element-wise opperation

print("Array+5:",arr+5)#add 5 to all elements
print("Array squared:",arr**2)

#Mean ,Standard deviation

print("Mean:",np.mean(arr))
print("Standard deviation:",np.std(arr))

#Matrix Opperations

A=np.array([[1,2],[3,4]])
B=np.array([[2,0],[1,3]])
print("A Matrix:\n:",A)
print("\nB Matrix:\n",B)

#Matrix addition and Subtraction

print("Sum of A+B:\n")
print(A+B)

print("\nDifference of A and B:\n")
print(A-B)

#Element wise multiplication

print("\nMultiplication\n")
print(A*B)

#Matrix Multiplication

print("\nMatrix multiplication:\n")
print(np.dot(A,B))

#Transpose of A

print("\nTranspose of A\n")
print(A.T)
