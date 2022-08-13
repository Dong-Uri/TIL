# 아랫면 숫자와 주사위를 받아 윗면 숫자와 옆면의 최대 숫자를 리턴받는 함수
def stack_dice(bottom_num, dice):
    for i in range(6):
        if dice[i] == bottom_num:
            bottom_idx = i
            if bottom_idx == 0:
                top_idx = 5
            elif bottom_idx == 1:
                top_idx = 3
            elif bottom_idx == 2:
                top_idx = 4
            elif bottom_idx == 3:
                top_idx = 1
            elif bottom_idx == 4:
                top_idx = 2
            else:
                top_idx = 0
            break
    top_num = dice[top_idx]
    max_num = 0
    for i in range(6):
        if i != bottom_idx and i != top_idx and dice[i] > max_num:
            max_num = dice[i]
    return top_num, max_num

N = int(input())
dice_list = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 초기 밑면 6가지에 대해
for i in range(1, 7):
    max_sum = 0
    for j in range(N):
        i, max_n = stack_dice(i, dice_list[j])
        max_sum += max_n
    if max_sum > ans:
        ans = max_sum

print(ans)