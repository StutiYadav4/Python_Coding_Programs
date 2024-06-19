def replace_negatives_with_column_max(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    column_max = [-float('inf')] * cols
    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] != -1:
                column_max[j] = max(column_max[j], matrix[i][j])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                matrix[i][j] = column_max[j]

    return matrix

matrix = [
    [1, 2, -1],
    [4, -1, 6],
    [-1, 8, 9]
]
answer = replace_negatives_with_column_max(matrix)
print(answer)



