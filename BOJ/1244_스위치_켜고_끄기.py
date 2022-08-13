# arr에서 num을 스위치를 누르는 함수
def change_switch(arr, num):
    if arr[num] == 0:
        arr[num] = 1
    else:
        arr[num] = 0

N = int(input())
switch = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    stu_sex, stu_num = map(int, input().split())

    # 남학생 배수마다 스위치를 누름
    if stu_sex == 1:
        change = stu_num
        while change <= N:
            change_switch(switch, change-1)
            change += stu_num

    # 여학생 양쪽이 대칭인 동안 스위치를 누름
    else:
        change_switch(switch, stu_num-1)
        i = 1
        while stu_num - i >= 1 and stu_num + i <= N:
            if switch[stu_num-i-1] == switch[stu_num+i-1]:
                change_switch(switch, stu_num-i-1)
                change_switch(switch, stu_num+i-1)
            else:
                break
            i += 1

# 20줄씩 출력
for i in range((N-1)//20+1):
    print(*switch[i*20:(i+1)*20])