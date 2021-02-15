
#NOTE:
#Problem Code:FCIPL


# cook your dish here

# because each room is equal so we put p footballers into first i room and q crickers into the last r-i rooms.
# no just caculate the number of ways to puts i people into n rooms such that no room has no people
# we have n blocks
# with each unique block, their will be n! permutatinons of these block, that means with each sequence of blocks, these block will repate n! times
# so just divide the result by n! we get the number of unique ways

from functools import lru_cache
mod = 998244353
f = [1]
for i in range(1, 201):
    f.append(f[-1] * i % mod)
inv = [pow(i, mod-2, mod) for i in f]    
C = lambda k, n : f[n] * inv[n-k] * inv[k] % mod

@lru_cache(None)
def dp(n, k , offset = 1):
    if n == 0:
        return k == 0
    ans = 0
    for i in range(offset, k+1):
       
        ans += C(i, k) * dp(n-1, k-i, offset) 
        ans %= mod
    return ans 
        
t = int(input())
for _ in range(t):
    p,q,r = map(int ,input().split()) 
    print (sum (dp(i, p, 1) * dp(r-i, q, 2) * inv[i] * inv[r-i] % mod for i in range(1, r)) % mod)
    
