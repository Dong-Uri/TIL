from collections import deque
M, N, H = map(int, input().split())

# 박스와 시작 큐를 설정
box = []
q = deque()
for i in range(H):
    floor = []
    for j in range(N):
        line = list(map(int, input().split()))
        for k in range(M):
            if line[k] == 1:
                q.append([i, j, k])
        floor.append(line)
    box.append(floor)

ans = 0
while q:
    tomato = q.popleft()
    for x, y, z in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        side_x = tomato[0] + x
        side_y = tomato[1] + y
        side_z = tomato[2] + z

        # 주변에 토마토를 익힘
        if 0 <= side_x <= H-1 and 0 <= side_y <= N-1 and 0 <= side_z <= M-1 and box[side_x][side_y][side_z] == 0:
            box[side_x][side_y][side_z] = box[tomato[0]][tomato[1]][tomato[2]] + 1
            ans = box[tomato[0]][tomato[1]][tomato[2]]
            q.append([side_x, side_y, side_z])

# 안익은 토마토 확인
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                ans = -1
                break
        if ans == -1:
            break
    if ans == -1:
        break

print(ans)