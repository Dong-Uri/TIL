T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if N // 2 <= i + j < N + N // 2 and i - j <= N // 2 and j - i <= N // 2:
                ans += farm[i][j]
    print(f'#{t} {ans}')