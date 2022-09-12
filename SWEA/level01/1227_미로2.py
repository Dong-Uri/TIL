for _ in range(10):
    t = input()

    # 미로를 만들면서 시작점과 도착점을 찾음
    maze = []
    for i in range(100):
        line = list(map(int, input()))
        for j in range(100):
            if line[j] == 2:
                start = [i, j]
            elif line[j] == 3:
                end = [i, j]
        maze.append(line)

    visited = [[0] * 100 for _ in range(100)]
    stack = [start]
    visited[start[0]][start[1]] = 1
    ans = 0

    # 탐색 가능한 구역을 모두 방문하며 표시
    while stack:
        now = stack.pop()
        for mx, my in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = now[0] + mx
            ny = now[1] + my
            if maze[nx][ny] != 1 and visited[nx][ny] == 0:
                stack.append([nx, ny])
                visited[nx][ny] = 1

    # 도착점의 방문 여부를 출력
    print(f'#{t} {visited[end[0]][end[1]]}')

# 하위 문제
# 1226_미로1 # 미로의 크기를 100에서 16으로