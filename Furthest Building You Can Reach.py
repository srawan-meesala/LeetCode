heights = [4, 2, 7, 6, 9, 14, 12]
bricks, ladders = 5, 1
diff = []
res, poss = 0, 0
for i in range(1, len(heights)):
    if heights[i] > heights[i - 1]:
        diff.append(heights[i] - heights[i - 1])
        poss += 1
    else:
        res += 1

while diff:
    diff2 = sorted(diff, reverse=True)
    if sum(diff2[ladders:]) <= bricks:
        print(res + poss)
        break
    else:
        diff = diff[:-1]
        poss -= 1

print(diff, diff2)