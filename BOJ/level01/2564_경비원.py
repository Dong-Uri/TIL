b_garo, b_sero = map(int, input().split())
N = int(input())
spot = [list(map(int, input().split())) for _ in range(N+1)]
ans = 0
for n in range(N):

    # 동근이와 상점의 방향이 같은 경우
    if spot[n][0] == spot[-1][0]:
        if spot[n][1] > spot[-1][1]:
            ans += spot[n][1] - spot[-1][1]
        else:
            ans += spot[-1][1] - spot[n][1]

    # 동근이와 상점의 방향이 남북인 경우
    elif spot[n][0] + spot[-1][0] == 3:
        if spot[n][1] + spot[-1][1] < b_garo:
            ans += b_sero + spot[n][1] + spot[-1][1]
        else:
            ans += b_sero + 2 * b_garo - spot[n][1] - spot[-1][1]

    # 동근이와 상점의 방향이 동서인 경우
    elif spot[n][0] + spot[-1][0] == 7:
        if spot[n][1] + spot[-1][1] < b_sero:
            ans += b_garo + spot[n][1] + spot[-1][1]
        else:
            ans += b_garo + 2 * b_sero - spot[n][1] - spot[-1][1]

    # 동근이와 상점의 방향이 북서인 경우
    elif spot[n][0] + spot[-1][0] == 4:
        ans += spot[n][1] + spot[-1][1]

    # 동근이와 상점의 방향이 남동인 경우
    elif spot[n][0] + spot[-1][0] == 6:
        ans += b_garo + b_sero - spot[n][1] - spot[-1][1]

    # 동근이와 상점의 방향이 동북이거나 남서인 경우
    else:

        # 상점에서 모서리까지의 거리
        if spot[n][0] == 1:
            ans +=b_garo - spot[n][1]
        elif spot[n][0] == 3:
            ans += b_sero - spot[n][1]
        else:
            ans += spot[n][1]
            
        # 동근이부터 모서리까지의 거리
        if spot[-1][0] == 1:
            ans += b_garo - spot[-1][1]
        elif spot[-1][0] == 3:
            ans += b_sero - spot[-1][1]
        else:
            ans += spot[-1][1]
            
print(ans)