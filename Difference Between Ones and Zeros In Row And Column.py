grid = [[0,1,1],[1,0,1],[0,0,1]]
m = len(grid[0])
n = len(grid)
diff = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    one = 0
    for j in range(n):
        if grid[j][i] == 1:
            one += 1
        else:
            one -= 1
    for j in range(n):
        diff[j][i] += one

for j in range(n):
    one = 0
    for i in range(m):
        if grid[j][i] == 1:
            one += 1
        else:
            one -= 1
    for i in range(m):
        diff[j][i] += one

print(diff)