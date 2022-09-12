C, R = map(int, input().split())
K = int(input())

# 좌석 배정 불가
if C*R < K:
    print('0')
else:

    # 이동 방향 설정값
    move_x = [0, 1, 0, -1]
    move_y = [1, 0, -1, 0]
    moving = 0

    # 좌석이 차있는지 확인하고 차게되면 0에서 1로 채움
    check = [[0]*R for _ in range(C)]
    now = [1, 1]
    check[now[0]-1][now[1]-1] = 1
    for _ in range(K-1):

        # 현재 방향쪽에 앉을수 있다면
        if 1 <= now[0] + move_x[moving] <= C and 1 <= now[1] + move_y[moving] <= R and check[now[0] + move_x[moving] - 1][now[1] + move_y[moving] - 1] == 0:
            now[0] += move_x[moving]
            now[1] += move_y[moving]
            check[now[0] - 1][now[1] - 1] = 1

        # 현재 방향쪽에 앉을수 없다면 방향을 튼다
        else:
            moving = (moving+1)%4
            now[0] += move_x[moving]
            now[1] += move_y[moving]
            check[now[0] - 1][now[1] - 1] = 1
            
    print(*now)