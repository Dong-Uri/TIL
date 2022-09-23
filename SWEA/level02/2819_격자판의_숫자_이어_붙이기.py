di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
T = int(input())
for t in range(1, T+1):
    pan = [list(input().split()) for _ in range(4)]
    ans_list = []

    # 각 시작점에서 깊이탐색
    for i in range(4):
        for j in range(4):
            stk = [[i, j, pan[i][j]]]
            k = 0
            while stk:
                now = stk.pop()

                # 6번 이동했다면 완성 된 수 중복 확인 후 저장
                if len(now[2]) == 7:
                    if now[2] not in ans_list:
                        ans_list.append(now[2])
                
                # 이동
                else:
                    for m in range(4):
                        ni = now[0] + di[m]
                        nj = now[1] + dj[m]
                        if 0 <= ni < 4 and 0 <= nj < 4:
                            stk.append([ni, nj, now[2] + pan[ni][nj]])
                            
    print(f'#{t} {len(ans_list)}')