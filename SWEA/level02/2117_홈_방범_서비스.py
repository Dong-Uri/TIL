T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    dosi = [list(map(int, input().split())) for _ in range(N)]
    home_max = 0
    # i, j : 방범 서비스를 할 위치
    for i in range(N):
        for j in range(N):
            # K가 N+1 일때 NxN의 모든 도시에 서비스를 제공할 수 있음
            for K in range(1, N+2):
                home = 0
                # a, b : 방범 서비스를 받는지 확인할 위치
                for a in range(N):
                    for b in range(N):
                        # a, b에 집이 있고 방범 서비스 범위라면 집 추가
                        if dosi[a][b] and abs(a-i) + abs(b-j) <= K - 1:
                            home += 1
                # 더 많은 집에 서비스를 제공하면서 손해가 아닌 경우
                if home > home_max and home * M >= K**2 + (K-1)**2:
                    home_max = home
    print(f'#{t} {home_max}')