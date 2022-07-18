T = int(input())
answer = []
for t in range(T):
    N = int(input())
    NxN = []
    for _ in range(N):
        Nx = [x for x in input().split()]
        NxN.append(Nx)
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
    answer.append(ans)
for t in range(T):
    print('#%d%s'%((t+1), answer[t]))