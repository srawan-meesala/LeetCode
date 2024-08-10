def num_spaces(matrix):
    res = 0
    m, n = len(matrix), len(matrix[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i, j):
        if visited[i][j]: return
        visited[i][j] = True
        for nx, ny in directions:
            nx += i
            ny += j
            if 0<=nx<m and 0<=ny<n and matrix[nx][ny]==0 and not visited[nx][ny]:
                dfs(nx, ny)
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and matrix[i][j]==0:
                res += 1
                dfs(i, j)
    
    return res

def regionsBySlashes(grid) -> int:
    rows, cols = len(grid), len(grid[0])
    matrix = [[0 for _ in range(cols*3)] for _ in range(rows*3)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '/':
                matrix[i*3][j*3 + 2] = 1
                matrix[i*3 + 1][j*3 + 1] = 1
                matrix[i*3 + 2][j*3] = 1
            elif grid[i][j] == '\\':
                matrix[i*3][j*3] = 1
                matrix[i*3 + 1][j*3 + 1] = 1
                matrix[i*3 + 2][j*3 + 2] = 1

    res = num_spaces(matrix)
    return res

grid = [" /\\"," \\/","\\  "]
print(regionsBySlashes(grid))