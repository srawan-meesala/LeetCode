arr = [2, 0, 0, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 1]

def algo(arr):
    low = mid = 0
    high = len(arr)-1
    while(mid <= high):
        if arr[mid] == 0:
            k = arr[low]
            arr[low] = arr[mid]
            arr[mid] = k
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            k = arr[high]
            arr[high] = arr[mid]
            arr[mid] = k
            high -= 1

algo(arr)
print(arr)