T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    ameba = [list(map(int, input().split())) for _ in range(K)]
    while M > 0:
        NxN = [[[] for _ in range(N)] for _ in range(N)]
        for a in ameba:

            # 이동
            if a[3] == 1:
                a[0] -= 1
            elif a[3] == 2:
                a[0] += 1
            elif a[3] == 3:
                a[1] -= 1
            else:
                a[1] += 1

            # 약품
            if a[0] == 0:
                a[2] //= 2
                a[3] = 2
            elif a[0] == N-1:
                a[2] //= 2
                a[3] = 1
            elif a[1] == 0:
                a[2] //= 2
                a[3] = 4
            elif a[1] == N-1:
                a[2] //= 2
                a[3] = 3

            # 합체
            NxN[a[0]][a[1]].append(a)
        for i in range(N):
            for j in range(N):
                if len(NxN[i][j]) >= 2:
                    max_a = 0
                    sum_a = [i, j, 0, 0]
                    for a in NxN[i][j]:
                        sum_a[2] += a[2]
                        if a[2] > max_a:
                            max_a = a[2]
                            sum_a[3] = a[3]
                    NxN[i][j] = [sum_a]

                # 죽음
                elif (i == 0 or i == N - 1 or j == 0 or j == N - 1) and NxN[i][j]:
                    if NxN[i][j][0][2] == 0:
                        NxN[i][j] = []
        
        # 미생물 리스트를 새로 만듦
        ameba = []
        for i in range(N):
            for j in range(N):
                ameba += NxN[i][j]

        M -= 1

    # 최종 미생물 수 출력
    ans = 0
    for a in ameba:
        ans += a[2]
    print(f'#{t} {ans}')