def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = transpose_matrix(matrix)
print(result)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
