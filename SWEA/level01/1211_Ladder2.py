for _ in range(10):
    t = int(input())
    # 양쪽 끝에 0을 붙여서 사다리를 입력받는다.
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # 사다리의 출발점 인덱스 리스트
    start_list = []
    for idx, start in enumerate(ladder[0]):
        if start:
            start_list.append(idx)

    min_dist = 10000
    for i in start_list:
        now = [0, i]    # 현재 위치
        dist = 0        # 거리
        while now[0] < 99:

            # 오른쪽 길로 가는 경우
            if ladder[now[0]][now[1]+1] == 1:
                while ladder[now[0]][now[1]+1] == 1:
                    now[1] += 1
                    dist += 1
                now[0] += 1 # 왼쪽 길로 다시 가지 않도록 아래로
                dist += 1

            # 왼쪽 길로 가는 경우
            elif ladder[now[0]][now[1]-1] == 1:
                while ladder[now[0]][now[1]-1] == 1:
                    now[1] -= 1
                    dist += 1
                now[0] += 1 # 오른쪽 길로 다시 가지 않도록 아래로
                dist += 1

            # 밑으로 내려가는 경우
            else:
                now[0] += 1
                dist += 1

        # 최소거리인지 확인
        if dist < min_dist:
            min_dist = dist
            ans = i-1

    print(f'#{t} {ans}')