garo, sero = map(int, input().split())
N = int(input())
cut_x = []
cut_y = []

# 자르는 부분과 종이의 끝을 리스트에 저장
for i in range(N):
    cut_axis, cut_num = map(int, input().split())
    if cut_axis:
        cut_y.append(cut_num)
    else:
        cut_x.append(cut_num)
cut_x.append(sero)
cut_y.append(garo)

garo_max = sero_max = 0

# 가로의 최대 길이 찾기
cnt = 0
for i in range(1, garo+1):
    cnt += 1
    if i in cut_y:
        if cnt > garo_max:
            garo_max = cnt
        cnt = 0

# 세로의 최대 길이 찾기
cnt = 0
for i in range(1, sero+1):
    cnt += 1
    if i in cut_x:
        if cnt > sero_max:
            sero_max = cnt
        cnt = 0
        
print(garo_max*sero_max)