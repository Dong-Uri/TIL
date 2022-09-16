T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    # 초기 보드 배치
    NxN = [[0] * N for _ in range(N)]
    NxN[N // 2 - 1][N // 2 - 1] = 2
    NxN[N // 2 - 1][N // 2] = 1
    NxN[N // 2][N // 2 - 1] = 1
    NxN[N // 2][N // 2] = 2

    # 델타 값을 대칭이 되도록 설정
    dx = [1, 0, 1, 1, -1, -1, 0, -1]
    dy = [0, 1, 1, -1, 1, -1, -1, 0]
    for _ in range(M):
        y, x, c = map(int, input().split())
        x -= 1
        y -= 1
        NxN[x][y] = c   # 인덱스 값에 맞도록 좌표값 조절 후 배치
        origin_x = x    # 기준 x좌표 저장
        origin_y = y    # 기준 y좌표 저장
        for d in range(8):
            x = origin_x    # 기준 x좌표에서 시작
            y = origin_y    # 기준 y좌표에서 시작
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                
                # 방향에 있는 돌이 상대 돌인 경우 그 방향으로 탐색 계속 진행
                if 0 <= nx < N and 0 <= ny < N and NxN[nx][ny] == 3 - c:
                    x = nx
                    y = ny
                    
                # 방향에 있는 돌이 내 돌인 경우 다시 되돌아오며 내 돌로 바꿈
                elif 0 <= nx < N and 0 <= ny < N and NxN[nx][ny] == c:
                    while x - origin_x or y - origin_y: # 기준 좌표로 돌아올때까지
                        NxN[x][y] = c                   # 돌을 내 돌로 바꿈
                        x += dx[7 - d]                  # 대칭되는 델타 x값으로 이동
                        y += dy[7 - d]                  # 대칭되는 델타 y값으로 이동
                    break
                    
                # 그외 좌표 밖이거나 돌이 없는 경우 아무것도 하지 않음
                else:
                    break
                    
    # 돌 세는 과정
    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if NxN[i][j] == 1:
                white += 1
            elif NxN[i][j] == 2:
                black += 1

    print(f'#{t} {white} {black}')