img = [[2,3,4],
       [5,6,7],
       [8,9,10],
       [11,12,13],
       [14,15,16]]
m = len(img)
n = len(img[0])
res = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        total = 0
        count = 0
        top = max(i-1, 0)
        bottom = min(i+1, m-1)
        left = max(j-1, 0)
        right = min(j+1, n-1)
        for k in range(top, bottom+1):
            for l in range(left, right+1):
                total += img[k][l]
                count += 1
        res[i][j] = total//count
print(res)