arr = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 5, 5, 7, 7, 8, 8, 9, 9, 10, 11, 12]
# arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 9, 9, 9, 10, 10, 10]
def search(l, r, arr, target):
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
    return r

def solve_binary(arr):
    curr, res = 0, 0
    while curr < len(arr):
        right = search(curr, len(arr)-1, arr, arr[curr])
        res += 1
        curr = right + 1
    return res

def divide_conquer(arr):
    res = 0
    

print(solve_binary(arr))