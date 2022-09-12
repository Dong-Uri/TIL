# 입력을 받으며 키의 총합도 저장
tall_list = []
tall_sum = 0
for _ in range(9):
    tall = int(input())
    tall_list += [tall]
    tall_sum += tall

# 가짜 난쟁이 둘을 찾아내 값을 0으로 바꿈
for i in range(8):
    for j in range(i+1, 9):
        if tall_list[i] + tall_list[j] == tall_sum - 100: # 가짜 난쟁이 둘을 빼면 키의 합이 100이므로
            tall_list[i] = tall_list[j] = 0
            if i == 0:
                tall_list[1], tall_list[j] = tall_list[j], tall_list[1]
            else:
                tall_list[0], tall_list[j] = tall_list[j], tall_list[0]
            break
    if tall_list[i] == 0:
        tall_list[1], tall_list[i] = tall_list[i], tall_list[1]
        break

# 선택정렬
for i in range(2, 8): # 0이된 가짜 난쟁이 둘은 미리 정렬했으므로
    min_V = 100
    for j in range(i, 9):
        if tall_list[j] < min_V:
            min_V = tall_list[j]
            min_idx = j
    tall_list[i], tall_list[min_idx] = tall_list[min_idx], tall_list[i]

for i in range(2, 9):
    print(tall_list[i])