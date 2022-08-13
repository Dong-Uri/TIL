T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 룸 번호를 방이 위치한 index 방식으로 저장
    back_room = [[(x-1)//2 for x in list(map(int, input().split()))] for _ in range(N)]

    # 복도를 지날 사람 수를 corridor에 넣음
    corridor = [0] * 200
    for br in back_room:
        if br[0] < br[1]:
            for i in range(br[0], br[1]+1):
                corridor[i] += 1
        else:
            for i in range(br[1], br[0] + 1):
                corridor[i] += 1

    # 가장 많이 겹치는 복도의 값값
    ans = 0
    for i in corridor:
        if i > ans:
            ans = i

    print(f'#{t} {ans}')

    # # 출발할 방과 도착할 방을 앞 뒤로 정렬
    # for i in range(N):
    #     if back_room[i][0] > back_room[i][1]:
    #         back_room[i][0], back_room[i][1] = back_room[i][1], back_room[i][0]
    #
    # # 앞방을 기준으로 버블정렬
    # for i in range(N-1, 0, -1):
    #     for j in range(i):
    #         if back_room[j] > back_room[j+1]:
    #             back_room[j], back_room[j+1] = back_room[j+1], back_room[j]
    #
    # back_stu = N # 돌아가야할 학생 수
    # cnt = 0 # 각 단위시간 카운트
    # while back_stu > 0:
    #     cnt += 1
    #     now_back = -1 # 0 이상을 찾기 위한 초기 뒷방값
    #     for i in range(N):
    #         if back_room[i][0] > now_back: # 뒷방값 이상의 앞방값을 가진 학생이라면
    #             back_stu -= 1
    #             now_back = back_room[i][1] # 현재 학생의 뒷방값을 저장
    #             back_room[i][0] = -1 # 이미 돌아갔으므로 찾지 못하게함
    # print(f'#{t} {cnt}')