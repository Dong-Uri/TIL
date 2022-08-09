# 이전 코드
# answer = []
# for _ in range(10):
#     dump_len = int(input())
#     box_list = list(map(int, input().split()))
#     for _ in range(dump_len): # 입력받은 dump_len만큼 실행
#         max_idx = box_list.index(max(box_list)) # 가장 높은 박스의 index
#         min_idx = box_list.index(min(box_list)) # 가장 낮은 박스의 index
#         box_list[max_idx] -= 1 # 가장 높은 박스는 하나 낮춘다.
#         box_list[min_idx] += 1 # 가장 낮은 박스는 하나 높인다.
#     answer.append(max(box_list)-min(box_list)) # max와 min의 차이를 answer에 저장
# for l in range(10):
#     print(f'#{l+1} {answer[l]}')

for t in range(1, 11):
    dump_len = int(input())
    box_list = list(map(int, input().split()))
    # 버블정렬
    for i in range(99, 0, -1):
        for j in range(i):
            if box_list[j] > box_list[j+1]:
                box_list[j], box_list[j + 1] = box_list[j+1], box_list[j]
    for _ in range(dump_len): # 입력받은 dump_len만큼 실행
        box_list[99] -= 1
        box_list[0] += 1
        for i in range(1, 99):
            if box_list[i] >= box_list[0]:
                box_list[i-1], box_list[0] = box_list[0], box_list[i-1]
                break
        for i in range(98, 0, -1):
            if box_list[i] <= box_list[99]:
                box_list[i+1], box_list[99] = box_list[99], box_list[i+1]
                break
        if box_list[99]-box_list[0] <= 1:
            break
    print(f'#{t} {box_list[99]-box_list[0]}')