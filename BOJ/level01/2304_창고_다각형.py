N = int(input())
max_H = len_L = 0
gidung_list = []

# 기둥을 입력 받으며 최대 높이 기둥과 그 기둥의 위치와 기둥 위치의 최대값을 저장
for _ in range(N):
    L, H = map(int, input().split())
    if H > max_H:
        max_H = H
        max_L = L
    if L > len_L:
        len_L = L
    gidung_list += [[L, H]]

# 기둥 위치 최대값 +1 만큼의 창고를 만들고 기둥들을 세움
storage = [0] * (len_L+1)
for gidung in gidung_list:
    storage[gidung[0]] = gidung[1]

ans = max_H # 최대 높이 기둥의 면적은 미리 더해둠

# 최대 높이로 저장된 기둥의 왼쪽 면적 계산
add_num = 0 # 더할 면적 값
for i in range(1, max_L):
    # 더 높은 기둥이 나오면 더할 면적으로
    if storage[i] > add_num:
        add_num = storage[i]
    ans += add_num
    
add_num = 0 # 더할 면적 값
# 최대 높이로 저장된 기둥의 오른쪽 면적 계산
for i in range(len_L, max_L, -1):
    # 더 높은 기둥이 나오면 더할 면적으로
    if storage[i] > add_num:
        add_num = storage[i]
    ans += add_num
    
print(ans)