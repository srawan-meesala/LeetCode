n = 10

def count(n):
    MOD = (10**9+7)
    if n == 1:
        return 5
    elif n == 2:
        return 20
    else:
        k = bin(n)[2:][::-1]
        print(k)
        res = 1
        for i, bit in enumerate(k):
            if bit == '1':
                if i == 0:
                    res = (res*5) % MOD
                elif i == 1:
                    res = (res*20) % MOD
                else:
                    p = int(('1'+'0'*(i-1)), 2)
                    print(p)
                    res = res*(count(p) ** 2) % MOD
        return res % MOD

print(count(n))