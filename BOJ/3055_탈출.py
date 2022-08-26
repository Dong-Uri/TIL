from collections import deque
R, C = map(int, input().split())

# 숲과 고슴도치 큐의 시작점과 물의 위치를 저장
forest = []
q = deque()
water = deque()
for i in range(R):
    line = list(input())
    for j in range(C):
        if line[j] == 'S':
            line[j] = 0
            q.append([i, j])
        if line[j] == '*':
            water.append([i, j])
    forest.append(line)
ans = 'KAKTUS'
move = 0
while q:

    # 고슴도치가 이동하기 전에 물웅덩이 확장
    for _ in range(len(water)):
        w = water.popleft()
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            side_x = w[0] + x
            side_y = w[1] + y
            if 0 <= side_x <= R - 1 and 0 <= side_y <= C - 1:
                if forest[side_x][side_y] == '.':
                    forest[side_x][side_y] = '*'
                    water.append([side_x, side_y])

    # 고슴도치의 이동경로 큐
    move += 1
    for _ in range(len(q)):
        gosum = q.popleft()
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            side_x = gosum[0] + x
            side_y = gosum[1] + y
            if 0 <= side_x <= R-1 and 0 <= side_y <= C-1:
                if forest[side_x][side_y] == '.':
                    forest[side_x][side_y] = move
                    q.append([side_x, side_y])
                    continue

                # 비버의 굴에 도착한 경우
                if forest[side_x][side_y] == 'D':
                    ans = move
                    break
    if ans != 'KAKTUS':
        break

print(ans)