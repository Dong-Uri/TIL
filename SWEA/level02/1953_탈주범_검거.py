T = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
# way[i]는 i번 터널이 갈 수 있는 방향
way = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
# ok는 i방향으로 들어갈 수 있는 터널j의 (i, j)쌍들
ok = [(0, 1), (0, 2), (0, 5), (0, 6), (1, 1), (1, 2), (1, 4), (1, 7), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 3), (3, 6), (3, 7)]
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    que = [[R, C]]
    visited[R][C] = 1
    ans = 0
    while que:
        now = que.pop(0)
        if visited[now[0]][now[1]] > L:
            break
        ans += 1
        for w in way[maps[now[0]][now[1]]]:
            ni = now[0] + di[w]
            nj = now[1] + dj[w]
            # 추가적으로 가는 방향 쪽 터널이 갈수있는 터널인지 확인
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and (w, maps[ni][nj]) in ok:
                visited[ni][nj] = visited[now[0]][now[1]] + 1
                que.append([ni, nj])
    print(f'#{t} {ans}')