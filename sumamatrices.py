
print("Suma de matrices")
A = []
B = []
C = []

print ("Dimension, maximo 100")
S = int( input("Filas: "))
R = int( input("Columnas: "))

for i in range(S):
 A.append( [] ) 
 B.append( [] ) 
 C.append( [] ) 
for j in range(R):
 A[i].append( int( input("A{}{}: ".format(i+1,j+1))))
 B[i].append( int( input("B{}{}: ".format(i+1,j+1))))
 C[i].append( A[i][j] + B[i][j])


print(A)
print(B)
print(C)