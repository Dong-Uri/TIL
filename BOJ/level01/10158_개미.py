w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
p_origin, q_origin = p, q
moving = [1, 1] # 이동 방향
repeat_place = []

# x좌표
for i in range(t % (2*w)):      # 반복 제거
    if p + moving[0] > w:       # 오른쪽 경계면을 넘을때
        moving[0] = -1
        p += moving[0]
    elif p + moving[0] < 0:     # 왼쪽 경계면을 넘을때
        moving[0] = 1
        p += moving[0]
    else:
        p += moving[0]

# y좌표
for i in range(t % (2*h)):      # 반복 제거
    if q + moving[1] > h:       # 위쪽 경계면을 넘을때
        moving[1] = -1
        q += moving[1]
    elif q + moving[1] < 0:     # 아래쪽 경계면을 넘을때
        moving[1] = 1
        q += moving[1]
    else:
        q += moving[1]

print(p, q)