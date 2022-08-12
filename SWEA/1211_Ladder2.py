for _ in range(10):
    t = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 사다리의 시작 위치들의 인덱스를 찾음
    start = []
    for i in range(100):
        if ladder[0][i] == 1:
            start += [i]

    # 아무리 이동해도 전체 칸을 모두 돌진 않으므로 전체 칸 개수로 초기화
    min_cnt = 10000
    for s in start:
        now = [0, s] # 모든 시작 지점에 대해 시작
        cnt = 0 # 카운트는 좌우로 이동할때만 함
        while now[0] < 99:

            # 왼쪽으로 길이 있는 경우
            if now[1] != 0 and ladder[now[0]][now[1]-1] == 1: # 단축평가로 에러가 나지 않음
                while now[1] != 0 and ladder[now[0]][now[1]-1] == 1:
                    now[1] -= 1
                    cnt += 1
                now[0] += 1 # 무한루프 방지

            # 오른쪽으로 길이 있는 경우
            elif now[1] != 99 and ladder[now[0]][now[1] + 1] == 1:  # 단축평가로 에러가 나지 않음
                while now[1] != 99 and ladder[now[0]][now[1] + 1] == 1:
                    now[1] += 1
                    cnt += 1
                now[0] += 1  # 무한루프 방지

            # 좌우에 모두 길이 없는 경우 == 그냥 올라감
            else:
                now[0] += 1

        # 카운드가 최소인지 확인후 좌표 저장 (같아도 큰 좌표이므로 저장)
        if cnt <= min_cnt:
            min_cnt = cnt
            min_x = s

    print(f'#{t} {min_x}')