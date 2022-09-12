T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    pic_data = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+1)]
    cnt = max_gujo = 0
    for i in range(N):
        for j in range(M+1):
            if pic_data[i][j] == 1:
                cnt += 1
            else:
                if cnt > max_gujo:
                    max_gujo = cnt
                cnt = 0
    for j in range(M):
        for i in range(N+1):
            if pic_data[i][j] == 1:
                cnt += 1
            else:
                if cnt > max_gujo:
                    max_gujo = cnt
                cnt = 0
    print(f'#{t} {max_gujo}')