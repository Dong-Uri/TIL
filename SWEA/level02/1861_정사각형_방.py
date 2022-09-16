T = int(input())
for t in range(1, T+1):
    N = int(input())
    NxN = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, -1 ,0 ,0]
    dy = [0, 0, 1, -1]
    max_start = 1000000
    max_move = 0
    for i in range(N):
        for j in range(N):
            que = [[i, j]]      # 초기 큐
            start = NxN[i][j]   # 시작 지점 저장

            # 델타 방식 큐
            while True:
                now = que.pop()
                for d in range(4):
                    nx = now[0] + dx[d]
                    ny = now[1] + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and NxN[nx][ny] == NxN[now[0]][now[1]] + 1:
                        que.append([nx, ny])
                if not que:
                    end = NxN[now[0]][now[1]]   # 종료 지점 저장
                    break

            # 최종 이동거리를 계산하고 출력될 케이스인지 확인
            move = end - start+ 1
            if move > max_move or (move == max_move and start < max_start):
                max_move = move
                max_start = start
                
    print(f'#{t} {max_start} {max_move}')