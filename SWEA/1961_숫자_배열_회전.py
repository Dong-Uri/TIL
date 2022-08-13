T = int(input())
for t in range(1, T+1):
    N = int(input())
    NxN = [list(input().split()) for _ in range(N)]
    ans = ''
    for n in range(N):
        ans += '\n'
        for m in range(N):
            ans += NxN[N-1-m][n]
        ans += ' '
        for m in range(N):
            ans += NxN[N-1-n][N-1-m]
        ans += ' '
        for m in range(N):
            ans += NxN[m][N-1-n]
    print(f'#{t} {ans}')