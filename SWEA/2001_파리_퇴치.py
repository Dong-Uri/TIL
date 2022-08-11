T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    NxN = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for n in range(N-K+1):
        for m in range(N-K+1):
            hap = 0
            for i in range(K):
                for j in range(K):
                    hap += NxN[n+i][m+j]
            if ans < hap :
                ans = hap
    print(f'#{t} {ans}')