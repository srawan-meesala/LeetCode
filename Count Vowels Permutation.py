class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 +7
        arr = [1 for _ in range(5)]
        arr2 = [1 for _ in range(5)]
        for i in range(2,n+1):
            arr2[0] = (arr[1]+arr[2]+arr[4])%MOD
            arr2[1] = (arr[0]+arr[2])%MOD
            arr2[2] = (arr[1]+arr[3])%MOD
            arr2[3] = (arr[2])%MOD
            arr2[4] = (arr[2]+arr[3])%MOD
            for k in range(5):
                arr[k] = arr2[k]
        
        return sum(arr)%MOD