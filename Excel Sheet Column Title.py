import math
columnNumber = 703
n = 0
c = columnNumber - 1
res = ''
while c >= 0:
    k = c % 26
    res = chr(ord('A') + k) + res
    c = (c // 26) - 1
print(res)