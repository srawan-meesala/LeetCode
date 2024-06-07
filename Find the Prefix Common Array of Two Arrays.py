def solve(A, B):
    C = [2 for _ in range(len(A))]
    res = [0 for _ in range(len(A))]
    for i in range(len(A)):
        C[A[i]-1] -= 1
        C[B[i]-1] -= 1
        if C[A[i]-1] == 0: res[i] += 1
        if C[B[i]-1] == 0: res[i] += 1
        if i!=0:
            res[i] += res[i-1]       
    return res