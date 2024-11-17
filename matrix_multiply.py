def multiply_matrices(mat1, mat2):
    result = [[sum(a * b for a, b in zip(mat1_row, col)) for col in zip(*mat2)] for mat1_row in mat1]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("Matrix Multiplication Result:")
for row in multiply_matrices(matrix1, matrix2):
    print(row)