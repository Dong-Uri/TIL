for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    state = [0, 0] # 두 사각형의 상태

    # x좌표의 경우
    if x1 > p2 or x2 > p1:
        state[0] = 0
    elif x1 == p2 or x2 == p1:
        state[0] = 1
    else:
        state[0] = 2
        
    # y좌표의 경우
    if y1 > q2 or y2 > q1:
        state[1] = 0
    elif y1 == q2 or y2 == q1:
        state[1] = 1
    else:
        state[1] = 2
        
    # 경우에 따른 출력
    if state == [2, 2]:
        print('a')
    elif state == [1, 2] or state == [2, 1]:
        print('b')
    elif state == [1, 1]:
        print('c')
    else:
        print('d')