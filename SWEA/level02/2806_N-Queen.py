def N_queen(i, N, line1, line2, line3): # line은 각각 열과 두 대각선을 확인하는 용도
    global ans
    if i == N:
        ans += 1
        return
    for j in range(N):
        # 열과 대각선이 다른 퀸과 겹치지 않는 경우
        if j not in line1 and i + j not in line2 and i - j not in line3:
            N_queen(i + 1, N, line1 + [j], line2 + [i + j], line3 + [i - j])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = 0
    N_queen(0, N, [], [], [])
    print(f'#{t} {ans}')