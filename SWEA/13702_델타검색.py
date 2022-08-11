T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                i_n = i + x[k]
                j_n = j + y[k]
                if 0 <= i_n < N and 0 <= j_n < N:
                    if arr[i][j] > arr[i_n][j_n]:
                        ans += arr[i][j] - arr[i_n][j_n]
                    else:
                        ans += arr[i_n][j_n] - arr[i][j]
    print(f'#{t} {ans}')