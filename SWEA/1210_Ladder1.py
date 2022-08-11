for _ in range(10):
    t = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 사다리가 도착하는 위치의 인덱스를 찾음
    for i in range(100):
        if ladder[-1][i] == 2:
            end = i

    # 처음 2가 있는 위치에서 시작해서 거꾸로 사다리를 올라감
    now = [99, end] # 따라 올라가는 위치를 나타낼 변수
    while now[0] != 0 : # 현재 위치가 가장 위에 올라갈때까지 반복

        # 왼쪽으로 길이 있는 경우
        if now[1] != 0 and ladder[now[0]][now[1]-1] == 1: # 단축평가로 에러가 나지 않음
            while now[1] != 0 and ladder[now[0]][now[1]-1] == 1:
                now[1] -= 1
            now[0] -= 1 # 무한루프 방지

        # 오른쪽으로 길이 있는 경우
        elif now[1] != 99 and ladder[now[0]][now[1]+1] == 1: # 단축평가로 에러가 나지 않음
            while now[1] != 99 and ladder[now[0]][now[1]+1] == 1:
                now[1] += 1
            now[0] -= 1 # 무한루프 방지

        # 좌우에 모두 길이 없는 경우 == 그냥 올라감
        else:
            now[0] -= 1

    print(f'#{t} {now[1]}') # 가장 위에 도달했을때 위치를 print