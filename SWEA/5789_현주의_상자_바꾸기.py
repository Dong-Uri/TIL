T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split())
    LR_list = [list(map(int, input().split())) for _ in range(Q)]
    boxes = [0] * N # 박스들 리스트
    for i in range(Q):
        for j in range(LR_list[i][0]-1, LR_list[i][1]): # Li-1 부터 Ri-1 까지
            boxes[j] = i + 1
    print(f'#{t}', *boxes)