import numpy

l = [[1,2,3],[4,5,6],[7,8,9]]
matrixA = numpy.array(l)

print("Size of matrix is ",matrixA.size)
print("Shape of matrix is ",matrixA.shape)
print("Datatype of matrix is ",matrixA.dtype)
print("Dimension of matrix is ",matrixA.ndim)
print("Rank of matrix is ",numpy.linalg.matrix_rank(matrixA))
print("Flattened matrix is: ", matrixA.flatten())