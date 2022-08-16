T = int(input())
for t in range(1, T+1):
    N = int(input())
    meme = list(map(int, input().split()))
    last_max_idx = -1
    max_idx = 0
    ans = 0
    while max_idx < N-1:
        # 최대값의 인덱스 찾기
        for i in range(last_max_idx+1, N):
            if meme[i] > meme[max_idx]:
                max_idx = i
        # 최대값까지 차액을 더함
        for i in range(last_max_idx+1, max_idx):
            ans += meme[max_idx] - meme[i]
        last_max_idx = max_idx
        max_idx += 1
    print(f'#{t} {ans}')