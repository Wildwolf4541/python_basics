def add_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("Matrix Addition Result:")
for row in add_matrices(matrix1, matrix2):
    print(row)