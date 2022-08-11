T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    NxN = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    # 퍼즐 끝에 임의의 0을 붙여줌

    count_x = 0
    count_y = 0
    ans = 0
    for i in range(N):
        for j in range(N+1):
            if NxN[i][j] == 1:
                count_x += 1
            elif count_x != 0:
                if count_x == K:
                    ans += 1
                count_x = 0
            if NxN[j][i] == 1:
                count_y += 1
            elif count_y != 0:
                if count_y == K:
                    ans += 1
                count_y = 0

    print(f'#{t} {ans}')