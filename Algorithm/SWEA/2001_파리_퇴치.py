T = int(input())
answer = []
for t in range(T):
    N, K = map(int, input().split())
    NxN = []
    for _ in range(N):
        Nx = [int(x) for x in input().split()]
        NxN.append(Nx)
    ans = 0
    for n in range(N-K+1):
        for m in range(N-K+1):
            hap = 0
            for i in range(K):
                for j in range(K):
                    hap += NxN[n+i][m+j]
            if ans < hap :
                ans = hap
    answer.append(ans)
for t in range(T):
    print('#%d %d'%((t+1), answer[t]))