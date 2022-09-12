K = int(input())
farm_line = [list(map(int, input().split())) for _ in range(6)]

# 방향의 개수를 찾음
way_num = [0] * 5
for i in range(6):
    way_num[farm_line[i][0]] += 1

ans = 1
only_way = []
for i in range(6):
    if way_num[farm_line[i][0]] == 1: # 방향으로 가는 경우가 한번 뿐일 때
        ans *= farm_line[i][1]
        only_way += [i]

# 단방향인 경우와 반대편으로 떨어져있는 경우들을 곱하여 빼줌
ans -= farm_line[(only_way[0]+3)%6][1] * farm_line[(only_way[1]+3)%6][1]
ans *= K
print(ans)