answer = []
for _ in range(10):
    _ = input()
    ladder = []
    for _ in range(99): # 마지막 라인은 빼고 할꺼라 99입니당
        line = list(map(int, input().split()))
        ladder.append(line)
    lastline = list(map(int, input().split()))
    ladder.append(lastline)
    now = [99,lastline.index(2)] # 현재 진행되는 지점을 나타낼 변수
    # 처음 2가 있는 위치에서 시작해서 거꾸로 따라 올라갈 예정입니다.
    while now[0] != 0 : # 현재 위치가 가장 위에 올라갈때까지 반복
        if now[1] != 0 and ladder[now[0]][now[1]-1] == 1: # 현재 맨 왼쪽(0)이 아니고 왼쪽에 길이 있다면
            while now[1] != 0 and ladder[now[0]][now[1]-1] == 1: # 왼쪽 길이 존재하는 동안 계속
                now[1] -= 1 # 현재 위치를 왼쪽으로 이동
            now[0] -= 1 # 이후 위로 한번 이동 (안하면 다음 반복 때 다시 오른쪽으로 갑니다.)
        elif now[1] != 99 and ladder[now[0]][now[1]+1] == 1: # 현재 맨 오른쪽(99)이 아니고 오른쪽에 길이 있다면
            while now[1] != 99 and ladder[now[0]][now[1]+1] == 1: # 오른쪽 길이 존재하는 동안 계속
                now[1] += 1 # 현재 위치를 오른쪽으로 이동
            now[0] -= 1 # 이후 위로 한번 이동 (안하면 다음 반복 때 다시 오른쪽으로 갑니다.)
        else: # 오른쪽 왼쪽에 길이 없다면
            now[0] -= 1 # 올라갑니다
    answer.append(now[1]) # 가장 위에 도달했을때 위치를 정답에 저장
for l in range(10):
    print(f'#{l+1} {answer[l]}')