nums = [0,3,7,2,5,8,4,6,0,1]
n = len(nums)
if n==0 or n==1:
    print (n)
    exit()
d = {}
for i in nums:
    k = i%n
    if k in d.keys():
        d[k].append(i)
    else:
        d[k] = [i]
print(d)