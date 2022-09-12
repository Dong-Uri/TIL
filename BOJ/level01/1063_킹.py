king, rock, N = input().split()

# 킹과 돌을 숫자 좌표로 변경
king = [ord(king[0]) - 64, int(king[1])]
rock = [ord(rock[0]) - 64, int(rock[1])]

for _ in range(int(N)):

    # 움직임도 좌표로 변경
    move = input()
    go = [0, 0]
    for m in move:
        if m == 'R':
            go[0] += 1
        elif m == 'L':
            go[0] -= 1
        elif m == 'B':
            go[1] -= 1
        elif m == 'T':
            go[1] += 1

    # 킹과 돌이 좌표를 벗어나지 않는다면 이동
    go_king = [king[0] + go[0], king[1] + go[1]]
    if go_king == rock:
        go_rock = [rock[0] + go[0], rock[1] + go[1]]
        if 0 in go_rock or 9 in go_rock:
            continue
        else:
            rock = go_rock
    if 0 in go_king or 9 in go_king:
        continue
    else:
        king = go_king

# 숫자 좌표를 다시 일반 좌표로 변경하여 출력
king = chr(king[0] + 64) + str(king[1])
rock = chr(rock[0] + 64) + str(rock[1])
print(king)
print(rock)