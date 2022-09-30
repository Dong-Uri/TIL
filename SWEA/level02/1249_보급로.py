T = int(input())
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for t in range(1, T+1):
    N = int(input())
    zido = [list(map(int, input())) for _ in range(N)]
    que = []
    que.append((0, 0))
    moves = [[100000] * N for _ in range(N)]
    moves[0][0] = 0
    visited = [[0] * N for _ in range(N)]
    while que:
        i, j = que.pop(0)
        visited[i][j] = 1
        # 길을 탐색하며 길까지 가는 비용이 최소가된다면 다시 큐에 넣어 탐색
        for m in range(4):
            ni = i + di[m]
            nj = j + dj[m]
            if 0 <= ni < N and 0 <= nj < N and moves[i][j] + zido[ni][nj] < moves[ni][nj]:
                moves[ni][nj] = moves[i][j] + zido[ni][nj]
                que.append((ni, nj))
    print(f'#{t} {moves[N - 1][N - 1]}')