T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for t in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    now = [0, 0] # 현재 위치
    moving = 0 # 진행 방향 (d의 index)
    for n in range(1, N**2+1): # N제곱번 입력될 예정
        snail[now[0]][now[1]] = n # 현재 위치 now에 i를 입력
        if now[0] + di[moving] >= N or now[0] + di[moving] < 0 or now[1] + dj[moving] >= N or now[1] + dj[moving] < 0 or snail[now[0] + di[moving]][now[1] + dj[moving]] != 0:
            moving += 1
            if moving == 4:
                moving = 0
        # 현재 위치를 di, dj의 moving을 4로 나눈 나머지 인덱스로 이동
        now[0] += di[moving]
        now[1] += dj[moving]
    print(f'#{t}')
    for l in range(N):
        print(*snail[l])