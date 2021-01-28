def trip(X, A, u, K):
    if A[K] != -1 and A[K] != u[-1]:
        return []
    
    if K == 0:
        return [u]
    
    S = []
    for x in X[u[-1]]:
        S += trip(X, A, u + [x], K - 1)
    
    return S


T = int(input())
for _ in range(T):
    N, M, K = [int(x) for x in input().split()]
    UV = [[int(x) for x in input().split()] for _ in range(M)]
    Q = int(input())
    AB = [[int(x) for x in input().split()] for _ in range(Q)]
    
    X = [[i] for i in range(N)]
    for u, v in UV:
        X[u - 1] += [v - 1]
        X[v - 1] += [u - 1]
    
    A = [-1 for _ in range(K)] + [0]
    for a, b in AB:
        A[K - b] = a - 1
    
    S = trip(X, A, [0], K)
    print(len(S))
