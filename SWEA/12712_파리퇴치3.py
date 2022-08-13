T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # 입력받은 배열에 M-1 만큼의 0을 씌워준다.
    NxN = [[0]*(N+2*M-2)]*(M-1) + [[0]*(M-1)+list(map(int, input().split()))+[0]*(M-1) for _ in range(N)] + [[0]*(N+2*M-2)]*(M-1)
    ans = 0 # 초기값

    for i in range(M-1, N+M-1):
        for j in range(M-1, N+M-1):
            hap_plus = hap_x = NxN[i][j] # 기준 위치는 미리 더해줌
            for p in range(1, M):
                hap_plus += NxN[i+p][j] + NxN[i-p][j] + NxN[i][j+p] + NxN[i][j-p]
                hap_x += NxN[i+p][j+p] + NxN[i+p][j-p] + NxN[i-p][j+p] + NxN[i-p][j-p]
            if hap_plus > ans:
                ans = hap_plus
            if hap_x > ans:
                ans = hap_x

    print(f'#{t} {ans}')