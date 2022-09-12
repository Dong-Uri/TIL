T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())

    # 고객들이 오는 시간들을 정렬
    come = list(map(int, input().split()))
    come.sort()
    come += [-1]    # 마지막 체크값   
    i = 0           # 손님 idx
    
    time = bab = 0
    while True:
        
        # M초마다 K개의 붕어빵 생성 (0초 제외)
        if time != 0 and time % M == 0:
            bab += K

        # 손님이 오면 붕어빵 1개 제거
        while time == come[i]:
            bab -= 1
            i += 1

        # 붕어빵이 음수가 된다면 불가능하다는 뜻
        if bab < 0:
            ans = 'Impossible'
            break

        # 고객이 모두 와서 마지막 -1에 도달한 경우
        if come[i] == -1:
            ans = 'Possible'
            break

        time += 1

    print(f'#{t} {ans}')