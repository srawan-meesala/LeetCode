def perimeter(matrix, row_start, row_end, column_start, column_end):
    arr = []
    print(row_start, row_end, column_start, column_end)
    if row_start<0 or row_end<0 or column_start<0 or column_end<0 or row_start>row_end or column_start>column_end:
        return []
    if row_end-row_start==0:
        return matrix[row_start][column_start:column_end+1]
    if column_end-column_start==0:
        for i in range(row_start, row_end+1):
            arr.append(matrix[i][column_start])
        return arr
    for j in range(column_start, column_end+1):
        arr.append(matrix[row_start][j])
    for i in range(row_start+1, row_end+1):
        arr.append(matrix[i][column_end])
    for j in range(column_end-1, column_start-1, -1):
        arr.append(matrix[row_end][j])
    for i in range(row_end-1, row_start, -1):
        arr.append(matrix[i][column_start])
    arr += perimeter(matrix, row_start+1, row_end-1, column_start+1, column_end-1)
    return arr

def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    return perimeter(matrix, 0, m-1, 0, n-1)

matrix = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
print(spiralOrder(matrix))