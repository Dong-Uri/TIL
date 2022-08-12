T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N <= M:
        ans = 0
        for i in range(N): # 초기값 설정
            ans += A[i] * B[i]
        for i in range(1, M-N+1):
            hap = 0
            for j in range(N):
                hap += A[j] * B[j+i]
            if ans < hap:
                ans = hap
    if N > M:
        ans = 0
        for i in range(M): # 초기값 설정
            ans += A[i] * B[i]
        for i in range(1, N-M+1):
            hap = 0
            for j in range(M):
                hap += B[j] * A[j+i]
            if ans < hap:
                ans = hap
    print(f'#{t} {ans}')