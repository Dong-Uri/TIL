import math

answer = []
for _ in range(10):
    _ = input()
    ladder = []
    for _ in range(99): # 마지막 라인은 빼고 할꺼라 99입니당
        line = list(map(int, input().split()))
        ladder.append(line)
    lastline = list(map(int, input().split()))
    ladder.append(lastline)
    min_count = math.inf # 최소 값을 업데이트 할 예정이라 첫 기준값을 무한으로 줌
    min_x = None # 업데이트된 최소 이동거리의 출발지점 x좌표
    for _ in range(lastline.count(1)): # 1의 개수 (사다리의 다리 수) 만큼 반복
        now = [99,lastline.index(1)] # Ladder1과 같이 아래서부터 위로 올라갑니다.
        lastline[lastline.index(1)] = 2 # 다음번엔 안찾도록 숫자를 바꿈
        count = 0 # 이동거리 count, 참고로 올라가는 거리는 일정하므로 세지 않을 예정
        while now[0] != 0 : # 현재 위치가 가장 위에 올라갈때까지 반복
            if now[1] != 0 and ladder[now[0]][now[1]-1] == 1: # 현재 맨 왼쪽(0)이 아니고 왼쪽에 길이 있다면
                while now[1] != 0 and ladder[now[0]][now[1]-1] == 1: # 왼쪽 길이 존재하는 동안 계속
                    now[1] -= 1 # 현재 위치를 왼쪽으로 이동
                    count += 1 # 이동거리를 늘린다.
                now[0] -= 1 # 이후 위로 한번 이동 (안하면 다음 반복 때 다시 오른쪽으로 갑니다.)
            elif now[1] != 99 and ladder[now[0]][now[1]+1] == 1: # 현재 맨 오른쪽(99)이 아니고 오른쪽에 길이 있다면
                while now[1] != 99 and ladder[now[0]][now[1]+1] == 1: # 오른쪽 길이 존재하는 동안 계속
                    now[1] += 1 # 현재 위치를 오른쪽으로 이동
                    count += 1 # 이동거리를 늘린다.
                now[0] -= 1 # 이후 위로 한번 이동 (안하면 다음 반복 때 다시 오른쪽으로 갑니다.)
            else: # 오른쪽 왼쪽에 길이 없다면
                now[0] -= 1 # 올라갑니다
        if count < min_count: # 이동거리가 기존 최소 이동거리보다 짧았다면
            min_count = count # 최소 이동거리 업데이트
            min_x = now[1] # 출발 x좌표 업데이트
        elif count == min_count: # 이동거리가 기존 최소 이동거리와 같다면
            mix_x = max(min_x, now[1]) # 더 큰 x좌표로 저장 (문제조건임)
    answer.append(min_x) # 가장 위에 도달했을때 위치를 정답에 저장
for l in range(10):
    print(f'#{l+1} {answer[l]}')