# Matrix Algebra

from numpy import matrix
from numpy import linalg
import numpy
#from vectors import Point, Vector

'''
A = matrix( [[1,2,3],[11,12,13],[21,22,23]]) # Creates a matrix.
x = matrix( [[1],[2],[3]] )                  # Creates a matrix (like a column vector).
y = matrix( [[1,2,3]] )                      # Creates a matrix (like a row vector).

print(A.T)                                    # Transpose of A.
print(A*x)                                   # Matrix multiplication of A and x.
print(A.I)                                    # Inverse of A.
print(linalg.solve(A, x))     	# Solve the linear equation system.
'''

A = matrix([ [1,2,3],[2,7,4] ])
B = matrix([ [1,-1], [0,1] ])
C = matrix([ [5, -1], [9, 1], [6, 0] ])
D = matrix([ [3, -2,-1], [1, 2, 3] ])
u = matrix([ [6, 2, -3, 5] ])
v = matrix([ [3, 5, -1, 4] ])
w = matrix([ [1], [8], [0], [5] ])


print("Matrix Dimensions:")
print('(1.1) Dimensions of array A is: ' + str(A.shape))
print(A)
print('(1.2) Dimensions of array B is: ' + str(B.shape))
print(B)
print('(1.3) Dimensions of array C is: ' + str(C.shape))
print(C)
print('(1.4) Dimensions of array D is: ' + str(D.shape))
print(D)
print('(1.5) Dimensions of array u is: ' + str(u.shape))
print(u)
print('Dimensions of array v is: ' + str(v.shape))
print(v)
print('(1.6) Dimensions of array w is: ' + str(w.shape))
print(w)

'''
(1) Matrix Dimensions
(1.1) Dim of A -> 2x3
(1.2) Dim of B -> 2x2
(1.3) Dim of C -> 3x2
(1.4) Dim of D -> 2x3
(1.5) Dim of u -> 1x4
(1.6) Dim of w -> 4x1
'''

a = 6


print("\nVector Operations:")
print("(2.1) u + v = " + str(u + v) )
print("(2.2) u - v = " + str(u - v) )
print("(2.3) a * u = " + str(a * u) )

# is there a better way to do this?
u_list = [ 6, 2, -3, 5 ]
v_list = [ 3, 5, -1, 4 ]
u_v_dotproduct = sum([i*j for (i, j) in zip(u_list, v_list)])
print("(2.4) u . v = " + str(u_v_dotproduct) )

print("(2.5) ||u|| = " + str(linalg.norm(u)) )

'''
(2) Vector Operations
(2.1) u + v = [[ 9  7 -4  9]]
(2.2) u - v = [[ 3 -3 -2  1]]
(2.3) a * u = [[ 36  12 -18  30]]
(2.4) u . v = 51
(2.5) ||u|| = sqrt(74) = 8.60232526704
'''

print("\nMatrix Operations:")
# print("(3.1) A + C = ") # not defined
# print(A+C)
print("(3.2) A - C.T = ")
print(A-C.T)
print("(3.3) C.T + 3D = ") 
print(C.T+(3*D))
print("(3.4) B * A = ")
print(B*A)
#print("(3.5) B * A.T = ") # not defined
#print(B*A.T)
#print("(3.6) B * C = ") # not defined
#print(B*C)
print("(3.7) CB = ")
print(C*B)
print("(3.8) B^4 = ")
#print(B*B*B*B)
print(B**4)
print("(3.9) AA.T = ")
print(A*A.T)
print("(3.10) D.TD = ")
print(D.T*D)

'''
(3) Matrix Operations
(3.1) A + C = not defined
(3.2) A - C.T = 
	[[-4 -7 -3]
	 [ 3  6  4]]
(3.3) C.T + 3D = 
	[[14  3  3]
	 [ 2  7  9]]
(3.4) B * A = 
	[[-1 -5 -1]
	 [ 2  7  4]]
(3.5) B * A.T = not defined
(3.6) B * C = not defined
(3.7) C * B = 
	[[ 5 -6]
	 [ 9 -8]
	 [ 6 -6]]
(3.8) B**4 = 
	[[ 1 -4]
	 [ 0  1]]
(3.9) A * A.T = 
	[[14 28]
	 [28 69]]
(3.10) D.T * D = 
	[[10 -4  0]
	 [-4  8  8]
	 [ 0  8 10]]
=
'''


