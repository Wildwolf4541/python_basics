def transpose_matrix(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Transpose of Matrix:")
for row in transpose_matrix(matrix):
    print(row)