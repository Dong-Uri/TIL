from collections import deque
M, N = map(int, input().split())

# 박스와 시작 큐를 설정
box = []
q = deque()
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            q.append([i, j])
    box.append(line)

ans = 0
while q:
    tomato = q.popleft()
    for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        side_x = tomato[0] + x
        side_y = tomato[1] + y

        # 옆에 토마토를 익힘
        if 0 <= side_x <= N-1 and 0 <= side_y <= M-1 and box[side_x][side_y] == 0:
            box[side_x][side_y] = box[tomato[0]][tomato[1]] + 1
            ans = box[tomato[0]][tomato[1]]
            q.append([side_x, side_y])

# 안익은 토마토 확인
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            ans = -1
            break
    if ans == -1:
        break

print(ans)